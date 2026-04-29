/* jshint esversion: 11, jquery: true */
/* global describe, beforeEach, jest, test, require, expect */

describe('cart badge helper', () => {
	beforeEach(() => {
		document.body.innerHTML = '';
		jest.resetModules();
	});

	test('increments the badge count and reveals the badge', () => {
		document.body.innerHTML = `
			<span data-cart-badge class="d-none">2</span>
		`;

		const { updateCartBadge } = require('../js/components/cartBadge.js');
		updateCartBadge();

		const badge = document.querySelector('[data-cart-badge]');
		expect(badge.textContent).toBe('3');
		expect(badge.classList.contains('d-none')).toBe(false);
	});

	test('does not let the badge count go below zero', () => {
		document.body.innerHTML = `
			<span data-cart-badge>0</span>
		`;

		const { updateCartBadge } = require('../js/components/cartBadge.js');
		updateCartBadge(-5);

		const badge = document.querySelector('[data-cart-badge]');
		expect(badge.textContent).toBe('0');
	});

	test('does nothing when no badge element exists', () => {
		const { updateCartBadge } = require('../js/components/cartBadge.js');

		expect(() => updateCartBadge()).not.toThrow();
	});
});
