/* jshint esversion: 11, jquery: true */
/* global describe, beforeEach, jest, test, require, expect */

describe('global frontend behavior', () => {
  beforeEach(() => {
    document.body.innerHTML = '';
    jest.resetModules();
  });

  test('swaps a broken image to its fallback source when an error occurs', () => {
    document.body.innerHTML = `
      <img
        id="car-image"
        src="https://example.com/broken.jpg"
        data-fallback-src="/static/images/placeholder-car.svg"
        alt="Test car"
      />
    `;

    require('../js/main.js');

    const image = document.getElementById('car-image');
    image.dispatchEvent(new Event('error'));

    expect(image.getAttribute('src')).toContain('/static/images/placeholder-car.svg');
  });

  test('reveals editorial content when IntersectionObserver is unavailable', () => {
    const originalObserver = window.IntersectionObserver;
    delete window.IntersectionObserver;
    document.body.innerHTML = '<article data-reveal></article>';

    require('../js/main.js');

    expect(document.querySelector('[data-reveal]').classList.contains('in-view')).toBe(true);
    window.IntersectionObserver = originalObserver;
  });
});
