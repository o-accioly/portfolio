// Footer wordmark: "oAccioly faz" followed by a tape that is rewritten with what gets done.
// It runs through the list once when the footer comes into view, then rests on the last line.

const STEP_MS = 1500;

export function initBrand() {
  const tape = document.querySelector("[data-makes]");
  if (!tape || matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  const lines = tape.dataset.makes.split("|");
  if (lines.length < 2 || !("IntersectionObserver" in window)) return;

  const observer = new IntersectionObserver(
    ([entry]) => {
      if (!entry.isIntersecting) return;
      observer.disconnect();
      let index = 0;
      const write = () => {
        tape.textContent = lines[index];
        tape.classList.remove("is-writing");
        void tape.offsetWidth; // restart the stroke
        tape.classList.add("is-writing");
        index += 1;
        if (index < lines.length) setTimeout(write, STEP_MS);
      };
      write();
    },
    { threshold: 0.6 },
  );
  observer.observe(tape);
}
