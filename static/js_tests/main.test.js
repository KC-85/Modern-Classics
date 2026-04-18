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
});
