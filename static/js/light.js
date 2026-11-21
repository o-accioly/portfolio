// Studio light: follows the system until the visitor picks "on" or "dimmed".
const KEY = "studio-light";
const ORDER = ["auto", "light", "dark"];

function stored() {
  try {
    const value = localStorage.getItem(KEY);
    return value === "light" || value === "dark" ? value : "auto";
  } catch {
    return "auto";
  }
}

function apply(button, mode) {
  const root = document.documentElement;
  if (mode === "auto") delete root.dataset.theme;
  else root.dataset.theme = mode;

  const label = button.dataset[`label${mode[0].toUpperCase()}${mode.slice(1)}`];
  button.querySelector("[data-light-text]").textContent = label;
  button.setAttribute("aria-label", `${button.dataset.aria}: ${label}`);
}

export function initLight() {
  const button = document.querySelector("[data-light]");
  if (!button) return;

  let mode = stored();
  apply(button, mode);

  button.addEventListener("click", () => {
    mode = ORDER[(ORDER.indexOf(mode) + 1) % ORDER.length];
    try {
      if (mode === "auto") localStorage.removeItem(KEY);
      else localStorage.setItem(KEY, mode);
    } catch {
      // Storage can be blocked; the choice then lasts for this page only.
    }
    apply(button, mode);
  });
}
