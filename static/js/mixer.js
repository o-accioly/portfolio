// Routing matrix: solo one product to see only its mix.
// A solo also puts that product on the monitor, so the choice shows in both places.

export function initMixer(stage) {
  const matrix = document.querySelector("[data-matrix]");
  if (!matrix) return;

  const buttons = [...document.querySelectorAll("[data-solo]")];
  const rows = [...matrix.querySelectorAll(".mx-row")];
  const columns = [...matrix.querySelectorAll("[data-col]")];

  function solo(slug) {
    if (slug) matrix.dataset.solo = slug;
    else delete matrix.dataset.solo;

    for (const button of buttons) button.setAttribute("aria-pressed", String(button.dataset.solo === slug));
    for (const row of rows) {
      const used = row.dataset.uses.split(" ").includes(slug);
      row.toggleAttribute("data-ghost", Boolean(slug) && !used);
    }
    for (const cell of columns) cell.toggleAttribute("data-solo-cell", Boolean(slug) && cell.dataset.col === slug);
  }

  for (const button of buttons) {
    button.addEventListener("click", () => {
      const slug = button.dataset.solo;
      solo(slug);
      if (slug && stage) stage.set({ project: slug });
    });
  }

  // A project picked on the tape while a solo is active moves the solo with it.
  stage?.onChange((state) => {
    if (matrix.dataset.solo && matrix.dataset.solo !== state.project) solo(state.project);
  });
}
