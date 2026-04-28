/* jshint esversion: 11, jquery: true */
/* global global, describe, beforeEach, afterEach, jest, test, require, expect, bootstrap */

describe('addToCart service', () => {
	const originalFetch = global.fetch;

	beforeEach(() => {
		jest.resetModules();
		document.cookie = 'csrftoken=; Max-Age=0; path=/';
		document.cookie = 'csrftoken=test-token';
	});

	afterEach(() => {
		global.fetch = originalFetch;
	});

	test('posts quantity and csrf token and returns ok on success', async () => {
		global.fetch = jest.fn().mockResolvedValue({
			ok: true,
			redirected: false,
			url: 'http://testserver/trailer/add/42/',
		});

		const { addToCart } = require('../js/services/cartService.js');
		const result = await addToCart(42, 3);

		expect(result).toEqual({ ok: true });
		expect(global.fetch).toHaveBeenCalledTimes(1);
		const [url, options] = global.fetch.mock.calls[0];
		expect(url).toBe('/trailer/add/42/');
		expect(options.method).toBe('POST');
		expect(options.headers['X-CSRFToken']).toBe('test-token');
		expect(String(options.body)).toContain('quantity=3');
		expect(options.redirect).toBe('follow');
	});

	test('returns redirected when backend sends login redirect', async () => {
		const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

		global.fetch = jest.fn().mockResolvedValue({
			ok: true,
			redirected: true,
			url: 'http://testserver/accounts/login/?next=/trailer/add/42/',
		});

		const { addToCart } = require('../js/services/cartService.js');
		const result = await addToCart(42, 1);

		expect(result).toEqual({ redirected: true });
		consoleSpy.mockRestore();
	});

	test('throws a descriptive error when response is not ok', async () => {
		global.fetch = jest.fn().mockResolvedValue({
			ok: false,
			status: 500,
			redirected: false,
			url: 'http://testserver/trailer/add/42/',
			text: jest.fn().mockResolvedValue('Internal server error: something failed badly'),
		});

		const { addToCart } = require('../js/services/cartService.js');

		await expect(addToCart(42, 1)).rejects.toThrow('Add to cart failed (500).');
	});
});
