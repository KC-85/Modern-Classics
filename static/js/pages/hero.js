/* jshint esversion: 11 */

(() => {
  const el = document.getElementById("heroCarousel");
  if (!el || typeof bootstrap === "undefined") {
    return;
  }

  const carousel = bootstrap.Carousel.getOrCreateInstance(el, {
    interval: 5000,
    ride: "carousel",
    pause: "hover",
    keyboard: true,
    touch: true,
    wrap: true,
  });

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      carousel.pause();
    } else {
      carousel.cycle();
    }
  });
})();