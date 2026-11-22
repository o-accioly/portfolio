// The stage: which project is on the monitor, at which screen size, and on which page.
// One state for the page; every control and readout bound to it follows.

const CYCLE_MS = 6400;
const LOADING_MS = 420;
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");

function readData() {
  const node = document.getElementById("stage-data");
  if (!node) return null;
  try {
    return JSON.parse(node.textContent);
  } catch {
    return null;
  }
}

export function initStage() {
  const data = readData();
  const rig = document.querySelector("[data-rig]");
  if (!data || !rig) return null;

  const device = rig.querySelector("[data-dv]");
  const screen = rig.querySelector("[data-screen]");
  const states = rig.querySelector("[data-states]");
  const statesTitle = rig.querySelector("[data-states-title]");
  const listeners = new Set();

  const state = {
    project: document.querySelector("[data-set-project][aria-pressed='true']")?.dataset.setProject ?? Object.keys(data.projects)[0],
    device: rig.dataset.device,
    page: 0,
  };

  const pagesNow = () => data.projects[state.project].shots[state.device]?.pages ?? [];

  // Sizes the product on stage was captured at. A product with no capture at all shows its
  // illustration at every size.
  function sizesOf(slug) {
    const captured = data.order.filter((key) => key in data.projects[slug].shots);
    return captured.length ? captured : data.order;
  }
  function nearestSize(slug, wanted) {
    const sizes = sizesOf(slug);
    if (sizes.includes(wanted)) return wanted;
    return sizes.includes("laptop") ? "laptop" : sizes[0];
  }

  // ---- screen content -----------------------------------------------------------------

  // `how` is "swap" (another product or size: cross-fade) or "nav" (the next page of the
  // same site: it slides in, the way a page arrives after a click).
  function showShot(how = "swap") {
    const project = data.projects[state.project];
    const pages = pagesNow();
    const shot = pages[state.page];
    const previous = [...screen.querySelectorAll(".dv-shot")];

    if (statesTitle) statesTitle.textContent = project.name;
    states.hidden = Boolean(shot);
    paintScreenLines(project);
    screen.toggleAttribute("data-pages", pages.length > 1);

    const leave = () => {
      for (const image of previous) {
        image.dataset.leaving = how;
        setTimeout(() => image.remove(), 560);
      }
    };
    if (!shot) return leave();
    if (previous.length === 1 && previous[0].getAttribute("src") === shot.src) return;

    const image = new Image();
    image.className = "dv-shot";
    image.alt = project.name;
    image.decoding = "async";
    image.dataset.entering = how;
    image.style.setProperty("--pan", `${shot.pan}%`);
    image.style.setProperty("--pan-dur", `${shot.dur}s`);
    image.src = shot.src;

    const enter = () => {
      // The request may be stale by the time the image decodes.
      if (pagesNow()[state.page]?.src !== shot.src) return;
      screen.insertBefore(image, states);
      requestAnimationFrame(() => requestAnimationFrame(() => delete image.dataset.entering));
      leave();
    };
    image.decode().then(enter, enter);
  }

  // When a page finishes scrolling, the monitor "clicks" through to the site's next page.
  screen.addEventListener("animationend", (event) => {
    if (event.animationName !== "pan-once" || event.target.dataset.leaving !== undefined) return;
    const pages = pagesNow();
    if (pages.length < 2) return;
    state.page = (state.page + 1) % pages.length;
    screen.dataset.loading = "";
    setTimeout(() => {
      delete screen.dataset.loading;
      showShot("nav");
    }, LOADING_MS);
  });

  // A product with no public page shows a short, labelled illustration instead of a capture.
  function paintScreenLines(project) {
    for (const holder of document.querySelectorAll("[data-bind='screen-lines']")) {
      const lines = project.screen.map((text, index) => {
        const line = document.createElement("p");
        line.className = "dv-state";
        line.style.setProperty("--n", index);
        const lamp = document.createElement("span");
        lamp.className = "lamp";
        line.append(lamp, text);
        return line;
      });
      holder.replaceChildren(...lines);
    }
  }

  // ---- bound controls and readouts ----------------------------------------------------

  function paint() {
    const project = data.projects[state.project];
    const size = data.devices[state.device];

    rig.dataset.device = state.device;
    device.dataset.device = state.device;

    const sizes = sizesOf(state.project);
    for (const button of document.querySelectorAll("[data-set-device]")) {
      button.setAttribute("aria-pressed", String(button.dataset.setDevice === state.device));
      button.disabled = !sizes.includes(button.dataset.setDevice);
    }
    for (const button of document.querySelectorAll("[data-set-project]")) {
      button.setAttribute("aria-pressed", String(button.dataset.setProject === state.project));
    }
    for (const node of document.querySelectorAll("[data-bind='project-name']")) node.textContent = project.name;
    for (const node of document.querySelectorAll("[data-bind='project-open']")) node.textContent = project.open;
    for (const node of document.querySelectorAll("[data-bind='project-kind']")) node.textContent = project.kind;
    for (const node of document.querySelectorAll("[data-bind='project-host']")) node.textContent = project.host;
    for (const node of document.querySelectorAll("[data-bind='project-link']")) node.setAttribute("href", project.href);
    for (const node of document.querySelectorAll("[data-bind='device-size']")) node.textContent = `${size.w} × ${size.h}`;
    for (const node of document.querySelectorAll("[data-bind='device-label']")) {
      const button = document.querySelector(`[data-set-device='${state.device}']`);
      if (button) node.textContent = button.dataset.label;
    }
    const sceneShot = project.shots.laptop?.top;
    for (const node of document.querySelectorAll("[data-bind='scene-image']")) {
      node.hidden = !sceneShot;
      if (sceneShot && node.getAttribute("src") !== sceneShot) node.setAttribute("src", sceneShot);
    }
    for (const node of document.querySelectorAll("[data-bind='scene-states']")) node.hidden = Boolean(sceneShot);
  }

  function set(next) {
    const changed = (next.project && next.project !== state.project) || (next.device && next.device !== state.device);
    if (!changed) return;
    Object.assign(state, next, { page: 0 });
    state.device = nearestSize(state.project, state.device);
    paint();
    showShot("swap");
    for (const listener of listeners) listener(state);
  }

  // ---- motion: the monitor steps through the five sizes until the visitor picks one ----

  const motionButton = document.querySelector("[data-cycle]");
  let timer = null;
  let visible = true;
  let auto = true; // still stepping through sizes by itself
  let playing = !reduceMotion.matches;

  function schedule() {
    clearInterval(timer);
    timer =
      playing && auto && visible && !document.hidden
        ? setInterval(() => {
            const sizes = sizesOf(state.project);
            set({ device: sizes[(sizes.indexOf(state.device) + 1) % sizes.length] });
          }, CYCLE_MS)
        : null;
    rig.toggleAttribute("data-paused", !playing);
  }
  function setPlaying(on) {
    playing = on;
    if (motionButton) {
      motionButton.setAttribute("aria-pressed", String(on));
      motionButton.querySelector("[data-cycle-play]").hidden = on;
      motionButton.querySelector("[data-cycle-pause]").hidden = !on;
    }
    schedule();
  }

  if (motionButton) {
    motionButton.hidden = false;
    motionButton.addEventListener("click", () => setPlaying(!playing));
  }
  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    schedule();
  }).observe(rig);
  document.addEventListener("visibilitychange", schedule);
  setPlaying(playing);

  // ---- events -------------------------------------------------------------------------

  document.addEventListener("click", (event) => {
    const deviceButton = event.target.closest("[data-set-device]");
    if (deviceButton) {
      auto = false;
      schedule();
      set({ device: deviceButton.dataset.setDevice });
      return;
    }
    const projectButton = event.target.closest("[data-set-project]");
    if (projectButton) set({ project: projectButton.dataset.setProject });
  });

  // Pointer tilt: the monitor leans a few degrees toward the cursor.
  const tilt = rig.querySelector("[data-tilt]");
  const well = rig.closest("[data-stage]") ?? rig;
  if (tilt && matchMedia("(hover: hover) and (pointer: fine)").matches && !reduceMotion.matches) {
    let targetX = 0;
    let targetY = 0;
    let x = 0;
    let y = 0;
    let frame = null;

    const step = () => {
      x += (targetX - x) * 0.08;
      y += (targetY - y) * 0.08;
      tilt.style.setProperty("--px", `${x.toFixed(2)}deg`);
      tilt.style.setProperty("--py", `${y.toFixed(2)}deg`);
      frame = Math.abs(targetX - x) + Math.abs(targetY - y) > 0.02 ? requestAnimationFrame(step) : null;
    };
    const aim = (nextX, nextY) => {
      targetX = nextX;
      targetY = nextY;
      frame ??= requestAnimationFrame(step);
    };
    well.addEventListener("pointermove", (event) => {
      const box = well.getBoundingClientRect();
      const horizontal = (event.clientX - box.left) / box.width - 0.5;
      const vertical = (event.clientY - box.top) / box.height - 0.5;
      aim(vertical * -7, horizontal * 12);
    });
    well.addEventListener("pointerleave", () => aim(0, 0));
  }

  paint();
  screen.toggleAttribute("data-pages", pagesNow().length > 1);

  return {
    get state() {
      return state;
    },
    set,
    onChange(listener) {
      listeners.add(listener);
    },
  };
}
