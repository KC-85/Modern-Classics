/* global describe, beforeEach, afterEach, jest, test, require, expect */

describe("hero carousel", () => {
  beforeEach(() => {
    jest.useFakeTimers();
    jest.resetModules();
    window.matchMedia = jest.fn(() => ({ matches: false }));
    document.body.innerHTML = `
      <section id="heroCarousel">
        <article data-carousel-slide class="opacity-100 scale-100" aria-hidden="false"></article>
        <article data-carousel-slide class="opacity-0 scale-[1.03] pointer-events-none" aria-hidden="true"></article>
        <button data-carousel-prev></button><button data-carousel-next></button>
        <span data-carousel-current>01</span>
      </section>`;
  });

  afterEach(() => jest.useRealTimers());

  test("moves to the next slide with controls", () => {
    require("../js/pages/hero.js");
    document.querySelector("[data-carousel-next]").click();
    const slides = document.querySelectorAll("[data-carousel-slide]");
    expect(slides[0].getAttribute("aria-hidden")).toBe("true");
    expect(slides[1].getAttribute("aria-hidden")).toBe("false");
    expect(document.querySelector("[data-carousel-current]").textContent).toBe("02");
  });

  test("advances automatically", () => {
    require("../js/pages/hero.js");
    jest.advanceTimersByTime(6500);
    expect(document.querySelectorAll("[data-carousel-slide]")[1].getAttribute("aria-hidden")).toBe("false");
  });

  test("exits safely when the carousel is absent", () => {
    document.body.innerHTML = "";
    expect(() => require("../js/pages/hero.js")).not.toThrow();
  });
});
