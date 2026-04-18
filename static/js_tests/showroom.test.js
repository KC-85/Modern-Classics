describe('showroom page script', () => {
	let originalIntersectionObserver;

	beforeEach(() => {
		document.body.innerHTML = '';
		jest.resetModules();
		originalIntersectionObserver = global.IntersectionObserver;
	});

	afterEach(() => {
		global.IntersectionObserver = originalIntersectionObserver;
	});

	test('marks cards for reveal and observes them on load', () => {
		const observe = jest.fn();
		const unobserve = jest.fn();
		const disconnect = jest.fn();

		global.IntersectionObserver = jest.fn(() => ({
			observe,
			unobserve,
			disconnect,
		}));

		document.body.innerHTML = `
			<div class="row g-3">
				<div class="card">
					<img class="card-img-top" alt="Example car" />
				</div>
			</div>
		`;

		require('../js/pages/showroom.js');

		const card = document.querySelector('.card');
		expect(card.getAttribute('data-reveal')).toBe('');
		expect(global.IntersectionObserver).toHaveBeenCalledTimes(1);
		expect(observe).toHaveBeenCalledWith(card);
	});
});
