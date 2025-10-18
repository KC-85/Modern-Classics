// Showroom page enhancements (progressive, no deps)
(() => {
  // 1) Reveal-on-scroll for cards
  const cards = document.querySelectorAll(".row.g-3 .card");
  if (cards.length) {
    cards.forEach(c => c.setAttribute("data-reveal", ""));

    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add("in-view");
          obs.unobserve(e.target);
        }
      });
    }, { rootMargin: "80px 0px", threshold: 0.1 });

    cards.forEach(c => io.observe(c));
  }

  // 2) Persist “Sort” selection in the URL on change (reset page)
  const sortSel = document.getElementById("sort");
  if (sortSel) {
    sortSel.addEventListener("change", () => {
      const url = new URL(window.location.href);
      url.searchParams.set("sort", sortSel.value);
      url.searchParams.set("page", "1");
      window.location.assign(url.toString());
    });
  }

  // 3) Gentle hover effect on image only (keeps layout steady)
  const scaleUp = (img) => {
    img.style.transition = "transform 140ms ease";
    img.style.transform = "scale(1.02)";
  };
  const scaleDown = (img) => {
    img.style.transform = "";
  };

  cards.forEach(card => {
    card.addEventListener("pointerenter", () => {
      const img = card.querySelector(".card-img-top");
      if (img) scaleUp(img);
    });
    card.addEventListener("pointerleave", () => {
      const img = card.querySelector(".card-img-top");
      if (img) scaleDown(img);
    });
  });

  // 4) Submit filters on Enter inside the search field (no extra clicks)
  const searchInput = document.getElementById("q");
  if (searchInput) {
    searchInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.target.form?.requestSubmit?.() || e.target.form?.submit();
      }
    });
  }

  // 5) Make cards feel tappable on mobile: click anywhere reveals link
  document.addEventListener("click", (e) => {
    const card = e.target.closest(".card");
    if (!card) return;
    const link = card.querySelector(".stretched-link");
    // Ignore clicks on buttons/links/inputs already
    if (e.target.closest("a,button,.btn,.form-control,.form-select")) return;
    if (link) {
      e.preventDefault();
      link.click();
    }
  });

  // 6) Superuser toolbar: enable Edit/Delete for selected car
  const adminForm   = document.getElementById("car-admin-form");
  const adminSelect = document.getElementById("adminCar");
  const editBtn     = document.getElementById("adminEdit");
  const deleteBtn   = document.getElementById("adminDelete");
  const editTplEl   = document.getElementById("editTpl");
  const delTplEl    = document.getElementById("delTpl");

  if (adminForm && adminSelect && editBtn && deleteBtn && editTplEl && delTplEl) {
    const updateButtons = () => {
      const slug = adminSelect.value || "";
      const ready = slug.length > 0;
      editBtn.disabled   = !ready;
      deleteBtn.disabled = !ready;

      if (ready) {
        editBtn.dataset.href      = editTplEl.value.replace("__SLUG__", slug);
        adminForm.dataset.delHref =  delTplEl.value.replace("__SLUG__", slug);
      } else {
        delete editBtn.dataset.href;
        delete adminForm.dataset.delHref;
      }
    };

    adminSelect.addEventListener("change", updateButtons);

    // Edit navigates
    editBtn.addEventListener("click", () => {
      const href = editBtn.dataset.href;
      if (href) window.location.assign(href);
    });

    // Delete posts to delete URL; CSRF already in the form
    adminForm.addEventListener("submit", (e) => {
      const action = adminForm.dataset.delHref;
      if (!action) { e.preventDefault(); return; }
      if (!confirm("Delete this car? This cannot be undone.")) {
        e.preventDefault();
        return;
      }
      adminForm.action = action;
      // method="post" is set in the template
    });

    updateButtons();
  }
})();
