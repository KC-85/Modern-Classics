/* jshint esversion: 11, jquery: true */
/* global global, describe, beforeEach, afterEach, jest, test, require, expect, bootstrap */

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