import { $, toast } from "../utils/dom.js";
import { addToCart } from "../services/cartService.js";
import { updateCartBadge } from "../components/cartBadge.js";

export function initCarDetailPage() {
  const form = $("#add-to-cart-form"); // give your detail form this id
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const btn = form.querySelector("button[type='submit']");
    const carId = form.dataset.carId; // set data-car-id on the form
    const qty   = form.querySelector("input[name='quantity']")?.value || 1;
    if (!carId) return;

    btn.disabled = true;
    btn.dataset.originalText ??= btn.textContent;
    btn.textContent = "Adding…";

    try {
      const res = await addToCart(carId, qty);
      if (res.redirected) return; // went to login
      toast("Added to cart ✅", {type: "success"});
      updateCartBadge(+1);
      btn.textContent = "Added";
    } catch (err) {
      console.error(err);
      toast("Couldn’t add to cart. Please try again.", {type: "danger"});
      btn.textContent = btn.dataset.originalText || "Add to cart";
      btn.disabled = false;
    }
  });
}
