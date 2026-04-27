/* jshint esversion: 11 */

(() => {
	const navbar = document.querySelector(".navbar");
	const toggle = document.querySelector(".nav-toggle");
	const navShell = document.getElementById("site-nav");

	if (navbar && toggle && navShell) {
		const closeNav = () => {
			navbar.classList.remove("nav-open");
			toggle.setAttribute("aria-expanded", "false");
		};

		toggle.addEventListener("click", () => {
			const isOpen = navbar.classList.toggle("nav-open");
			toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
		});

		navShell.querySelectorAll("a").forEach((link) => {
			link.addEventListener("click", () => {
				if (window.matchMedia("(max-width: 960px)").matches) {
					closeNav();
				}
			});
		});

		window.addEventListener("resize", () => {
			if (!window.matchMedia("(max-width: 960px)").matches) {
				closeNav();
			}
		});
	}

	// Global broken-image fallback for media URLs that may be missing remotely.
	const applyImageFallback = (img) => {
		const fallback = img?.dataset?.fallbackSrc;
		if (!fallback || img.src === fallback) {
			return;
		}
		img.src = fallback;
	};

	document.querySelectorAll("img[data-fallback-src]").forEach((img) => {
		img.addEventListener("error", () => applyImageFallback(img));
		// If the image failed before listeners were attached, recover immediately.
		if (img.complete && img.naturalWidth === 0) {
			applyImageFallback(img);
		}
	});

	document.querySelectorAll(".alert").forEach((alertEl) => {
		if (alertEl.classList.contains("alert-danger")) {
			return;
		}
		window.setTimeout(() => {
			alertEl.style.transition = "opacity 260ms ease";
			alertEl.style.opacity = "0";
			window.setTimeout(() => alertEl.remove(), 280);
		}, 4500);
	});
})();
