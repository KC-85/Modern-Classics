export const $  = (sel, root = document) => root.querySelector(sel);
export const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

export function toast(msg, {type="info", timeout=2500} = {}) {
  let box = $("#mc-toast");
  if (!box) {
    box = document.createElement("div");
    box.id = "mc-toast";
    box.style.position = "fixed";
    box.style.zIndex = "9999";
    box.style.left = "50%";
    box.style.bottom = "18px";
    box.style.transform = "translateX(-50%)";
    box.style.maxWidth = "90vw";
    document.body.appendChild(box);
  }
  const el = document.createElement("div");
  el.textContent = msg;
  el.className = `alert alert-${type} shadow-sm mb-2`;
  el.style.minWidth = "260px";
  box.appendChild(el);
  setTimeout(() => el.remove(), timeout);
}
