import { $, $$ } from "../utils/dom.js";

// Simple badge updater (you can wire this with a real count endpoint later)
export function updateCartBadge(delta = +1) {
  const el = $("[data-cart-badge]");
  if (!el) return;
  const current = parseInt(el.textContent || "0", 10) || 0;
  el.textContent = String(Math.max(0, current + delta));
  el.classList.remove("d-none");
}
