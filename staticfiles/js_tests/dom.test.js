/* jshint esversion: 11, jquery: true */
/* global describe, beforeEach, jest, test, require, expect */

describe('dom utilities', () => {
	beforeEach(() => {
		document.body.innerHTML = '';
		jest.resetModules();
	});

	test('$ returns the first matching element', () => {
		document.body.innerHTML = `
			<div class="item" id="first"></div>
			<div class="item" id="second"></div>
		`;

		const { $ } = require('../js/utils/dom.js');
		const first = $('.item');

		expect(first).not.toBeNull();
		expect(first.id).toBe('first');
	});

	test('$$ returns all matching elements as an array', () => {
		document.body.innerHTML = `
			<li class="row">One</li>
			<li class="row">Two</li>
			<li class="row">Three</li>
		`;

		const { $$ } = require('../js/utils/dom.js');
		const rows = $$('.row');

		expect(Array.isArray(rows)).toBe(true);
		expect(rows).toHaveLength(3);
		expect(rows[2].textContent).toBe('Three');
	});

	test('toast creates one container and removes toast after timeout', () => {
		jest.useFakeTimers();

		const { toast } = require('../js/utils/dom.js');
		toast('Saved successfully', { type: 'success', timeout: 100 });

		const box = document.getElementById('mc-toast');
		expect(box).not.toBeNull();
		expect(box.children).toHaveLength(1);
		expect(box.firstElementChild.textContent).toBe('Saved successfully');
		expect(box.firstElementChild.className).toContain('alert-success');

		jest.advanceTimersByTime(100);
		expect(box.children).toHaveLength(0);

		jest.useRealTimers();
	});
});
