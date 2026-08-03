/* jshint esversion: 11 */

(() => {
  const carousel = document.getElementById("heroCarousel");
  if (!carousel) return;

  const slides = Array.from(carousel.querySelectorAll("[data-carousel-slide]"));
  if (slides.length < 2) return;

  const previous = carousel.querySelector("[data-carousel-prev]");
  const next = carousel.querySelector("[data-carousel-next]");
  const counter = carousel.querySelector("[data-carousel-current]");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let activeIndex = 0;
  let timer;

  const show = (index) => {
    activeIndex = (index + slides.length) % slides.length;
    slides.forEach((slide, slideIndex) => {
      const isActive = slideIndex === activeIndex;
      slide.classList.toggle("opacity-0", !isActive);
      slide.classList.toggle("scale-[1.03]", !isActive);
      slide.classList.toggle("pointer-events-none", !isActive);
      slide.classList.toggle("opacity-100", isActive);
      slide.classList.toggle("scale-100", isActive);
      slide.setAttribute("aria-hidden", String(!isActive));
    });
    if (counter) counter.textContent = String(activeIndex + 1).padStart(2, "0");
  };

  const stop = () => window.clearInterval(timer);
  const start = () => {
    stop();
    if (!reducedMotion && !document.hidden) {
      timer = window.setInterval(() => show(activeIndex + 1), 6500);
    }
  };

  previous?.addEventListener("click", () => { show(activeIndex - 1); start(); });
  next?.addEventListener("click", () => { show(activeIndex + 1); start(); });
  carousel.addEventListener("mouseenter", stop);
  carousel.addEventListener("mouseleave", start);
  carousel.addEventListener("focusin", stop);
  carousel.addEventListener("focusout", start);
  carousel.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") show(activeIndex - 1);
    if (event.key === "ArrowRight") show(activeIndex + 1);
  });
  document.addEventListener("visibilitychange", start);
  start();
})();
