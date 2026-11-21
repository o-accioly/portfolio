// Recordings of the product's own screens: each plays only while it is on screen.
// With reduced motion nothing plays by itself; the visitor gets the player's controls.

export function initInside() {
  const videos = [...document.querySelectorAll("[data-inside-video]")];
  if (!videos.length) return;

  if (matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) {
    for (const video of videos) video.controls = true;
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      for (const { target, isIntersecting } of entries) {
        if (isIntersecting) target.play().catch(() => (target.controls = true));
        else target.pause();
      }
    },
    { threshold: 0.45 },
  );
  for (const video of videos) observer.observe(video);
}
