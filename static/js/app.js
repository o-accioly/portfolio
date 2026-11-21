// Entry point. Every module enhances markup that already works without it.
import { initBrand } from "./brand.js";
import { initInside } from "./inside.js";
import { initLight } from "./light.js";
import { initStage } from "./stage.js";
import { initMixer } from "./mixer.js";
import { initPatch } from "./patch.js";
import { initReveal } from "./reveal.js";
import { initTone } from "./tone.js";

initLight();
const stage = initStage();
initMixer(stage);
initPatch();
initReveal();
initTone();
initBrand();
initInside();
