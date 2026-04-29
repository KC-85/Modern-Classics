/* jshint esversion: 11, jquery: true */
/* global describe, beforeEach, test, require, expect, */

describe('getCSRFToken', () => {
	beforeEach(() => {
		document.cookie = 'csrftoken=; Max-Age=0; path=/';
		document.cookie = 'sessiontoken=; Max-Age=0; path=/';
	});

	test('returns the csrftoken cookie value', () => {
		document.cookie = 'csrftoken=abc123';

		const { getCSRFToken } = require('../js/utils/csrf.js');

		expect(getCSRFToken()).toBe('abc123');
	});

	test('returns an empty string when the token is missing', () => {
		const { getCSRFToken } = require('../js/utils/csrf.js');

		expect(getCSRFToken()).toBe('');
	});

	test('supports a custom cookie name', () => {
		document.cookie = 'sessiontoken=custom-value';

		const { getCSRFToken } = require('../js/utils/csrf.js');

		expect(getCSRFToken('sessiontoken')).toBe('custom-value');
	});
});
