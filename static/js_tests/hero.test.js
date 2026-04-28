/* jshint esversion: 11, jquery: true */
/* global global, describe, beforeEach, afterEach, jest, test, require, expect, bootstrap */

describe('hero page script', () => {
	beforeEach(() => {
		document.body.innerHTML = '';
		jest.resetModules();
		delete global.bootstrap;
	});

	test('initializes bootstrap carousel with expected options', () => {
		const pause = jest.fn();
		const cycle = jest.fn();
		const getOrCreateInstance = jest.fn(() => ({ pause, cycle }));

		global.bootstrap = {
			Carousel: {
				getOrCreateInstance,
			},
		};

		document.body.innerHTML = '<div id="heroCarousel"></div>';

		require('../js/pages/hero.js');

		const el = document.getElementById('heroCarousel');
		expect(getOrCreateInstance).toHaveBeenCalledWith(el, {
			interval: 5000,
			ride: 'carousel',
			pause: 'hover',
			keyboard: true,
			touch: true,
			wrap: true,
		});
	});

	test('pauses and resumes carousel on visibility changes', () => {
		const pause = jest.fn();
		const cycle = jest.fn();

		global.bootstrap = {
			Carousel: {
				getOrCreateInstance: jest.fn(() => ({ pause, cycle })),
			},
		};

		document.body.innerHTML = '<div id="heroCarousel"></div>';
		require('../js/pages/hero.js');

		Object.defineProperty(document, 'hidden', {
			configurable: true,
			get: () => true,
		});
		document.dispatchEvent(new Event('visibilitychange'));
		expect(pause).toHaveBeenCalledTimes(1);

		Object.defineProperty(document, 'hidden', {
			configurable: true,
			get: () => false,
		});
		document.dispatchEvent(new Event('visibilitychange'));
		expect(cycle).toHaveBeenCalledTimes(1);
	});

	test('exits safely when carousel element is missing', () => {
		global.bootstrap = {
			Carousel: {
				getOrCreateInstance: jest.fn(),
			},
		};

		expect(() => require('../js/pages/hero.js')).not.toThrow();
		expect(global.bootstrap.Carousel.getOrCreateInstance).not.toHaveBeenCalled();
	});
});
