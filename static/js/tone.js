// The console's line-up oscillator: A, 440 Hz, the note a tuning fork (diapasão) gives.
// It only sounds when the visitor presses the key, and stops by itself.

const SECONDS = 1.6;

export function initTone() {
  const button = document.querySelector("[data-tone]");
  const AudioContextClass = window.AudioContext ?? window.webkitAudioContext;
  if (!button || !AudioContextClass) return;

  button.hidden = false;
  const hint = document.querySelector("[data-tone-hint]");
  if (hint) hint.hidden = false;

  let context = null;
  let playing = false;

  button.addEventListener("click", async () => {
    if (playing) return;
    context ??= new AudioContextClass();
    await context.resume();

    const now = context.currentTime;
    const oscillator = context.createOscillator();
    const gain = context.createGain();
    oscillator.type = "sine";
    oscillator.frequency.value = 440;
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.12, now + 0.04);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + SECONDS);
    oscillator.connect(gain).connect(context.destination);
    oscillator.start(now);
    oscillator.stop(now + SECONDS);

    playing = true;
    button.setAttribute("aria-pressed", "true");
    oscillator.addEventListener("ended", () => {
      playing = false;
      button.setAttribute("aria-pressed", "false");
    });
  });
}
