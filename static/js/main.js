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
