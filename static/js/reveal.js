// Marks a scene as "in" the first time it enters the viewport. The CSS owns the motion;
// without this script (or with reduced motion) every scene is already in its final state.

export function initReveal() {
  const scenes = document.querySelectorAll("[data-reveal]");
  if (!scenes.length) return;

  if (!("IntersectionObserver" in window)) {
    for (const scene of scenes) scene.classList.add("is-in");
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add("is-in");
        observer.unobserve(entry.target);
      }
    },
    { rootMargin: "0px 0px -12% 0px", threshold: 0.08 },
  );
  for (const scene of scenes) observer.observe(scene);
}
