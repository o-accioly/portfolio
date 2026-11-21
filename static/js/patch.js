// Patch bay: one jack per stage of the work. Picking a jack sends the signal up to it and
// shows that stage. Without this script, every stage is listed one under the other.

export function initPatch() {
  const patch = document.querySelector("[data-patch]");
  if (!patch) return;

  const tabs = [...patch.querySelectorAll("[data-patch-tab]")];
  const panels = [...patch.querySelectorAll("[data-patch-panel]")];

  function select(index, focus = false) {
    patch.style.setProperty("--at", index);
    tabs.forEach((tab, position) => {
      tab.setAttribute("aria-selected", String(position === index));
      tab.tabIndex = position === index ? 0 : -1;
      tab.toggleAttribute("data-lit", position <= index);
    });
    panels.forEach((panel, position) => panel.toggleAttribute("data-active", position === index));
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => select(index));
    tab.addEventListener("keydown", (event) => {
      const move = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[event.key];
      if (move) {
        event.preventDefault();
        select((index + move + tabs.length) % tabs.length, true);
      } else if (event.key === "Home" || event.key === "End") {
        event.preventDefault();
        select(event.key === "Home" ? 0 : tabs.length - 1, true);
      }
    });
  });

  patch.dataset.ready = "";
  select(0);
}
