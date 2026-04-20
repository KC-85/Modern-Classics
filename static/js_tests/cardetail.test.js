jest.mock('../js/services/cartService.js', () => ({
	addToCart: jest.fn(),
}));

jest.mock('../js/components/cartBadge.js', () => ({
	updateCartBadge: jest.fn(),
}));

jest.mock('../js/utils/dom.js', () => {
	const actual = jest.requireActual('../js/utils/dom.js');
	return {
		...actual,
		toast: jest.fn(),
	};
});

describe('initCarDetailPage', () => {
	beforeEach(() => {
		document.body.innerHTML = '';
		jest.clearAllMocks();
		jest.resetModules();
	});

	test('submits add-to-cart and updates UI on success', async () => {
		const { addToCart } = require('../js/services/cartService.js');
		const { updateCartBadge } = require('../js/components/cartBadge.js');
		const { toast } = require('../js/utils/dom.js');

		addToCart.mockResolvedValue({ ok: true });

		document.body.innerHTML = `
			<form id="add-to-cart-form" data-car-id="42">
				<input name="quantity" value="2" />
				<button type="submit">Add to cart</button>
			</form>
		`;

		const { initCarDetailPage } = require('../js/pages/carDetail.js');
		initCarDetailPage();

		const form = document.getElementById('add-to-cart-form');
		const submitEvent = new Event('submit', { bubbles: true, cancelable: true });
		form.dispatchEvent(submitEvent);

		await Promise.resolve();

		const btn = form.querySelector("button[type='submit']");
		expect(addToCart).toHaveBeenCalledWith('42', '2');
		expect(toast).toHaveBeenCalledWith('Added to cart ✅', { type: 'success' });
		expect(updateCartBadge).toHaveBeenCalledWith(1);
		expect(btn.textContent).toBe('Added');
	});

	test('returns early on redirect without toast/badge updates', async () => {
		const { addToCart } = require('../js/services/cartService.js');
		const { updateCartBadge } = require('../js/components/cartBadge.js');
		const { toast } = require('../js/utils/dom.js');

		addToCart.mockResolvedValue({ redirected: true });

		document.body.innerHTML = `
			<form id="add-to-cart-form" data-car-id="42">
				<button type="submit">Add to cart</button>
			</form>
		`;

		const { initCarDetailPage } = require('../js/pages/carDetail.js');
		initCarDetailPage();

		const form = document.getElementById('add-to-cart-form');
		form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
		await Promise.resolve();

		expect(toast).not.toHaveBeenCalled();
		expect(updateCartBadge).not.toHaveBeenCalled();
	});

	test('shows error toast and restores button when add fails', async () => {
		const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
		const { addToCart } = require('../js/services/cartService.js');
		const { updateCartBadge } = require('../js/components/cartBadge.js');
		const { toast } = require('../js/utils/dom.js');

		addToCart.mockRejectedValue(new Error('network failed'));

		document.body.innerHTML = `
			<form id="add-to-cart-form" data-car-id="99">
				<button type="submit">Add to cart</button>
			</form>
		`;

		const { initCarDetailPage } = require('../js/pages/carDetail.js');
		initCarDetailPage();

		const form = document.getElementById('add-to-cart-form');
		const btn = form.querySelector("button[type='submit']");

		form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
		await Promise.resolve();

		expect(toast).toHaveBeenCalledWith('Couldn’t add to cart. Please try again.', { type: 'danger' });
		expect(updateCartBadge).not.toHaveBeenCalled();
		expect(btn.textContent).toBe('Add to cart');
		expect(btn.disabled).toBe(false);
		consoleSpy.mockRestore();
	});
});
