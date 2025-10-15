import { getCSRFToken } from "../utils/csrf.js";

export async function addToCart(carId, quantity = 1) {
  const resp = await fetch(`/trailer/add/${carId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
      "X-CSRFToken": getCSRFToken(),
    },
    body: new URLSearchParams({ quantity }),
    redirect: "follow",
  });

  // If Django redirected to login, we’ll land on 200 with login HTML.
  // Detect by URL change.
  if (resp.redirected && /\/accounts\/login\//.test(resp.url)) {
    window.location.href = resp.url; // go to login
    return { redirected: true };
  }

  if (!resp.ok) {
    const text = await resp.text().catch(() => "");
    throw new Error(`Add to cart failed (${resp.status}). ${text.slice(0,120)}`);
  }

  return { ok: true };
}
