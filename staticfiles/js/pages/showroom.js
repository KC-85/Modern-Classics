// static/js/pages/showroom.js
(() => {
  const qs = (sel, el=document) => el.querySelector(sel);
  const qsa = (sel, el=document) => Array.from(el.querySelectorAll(sel));
  const cards = qsa('.car-card');
  if (!cards.length) return;

  /* ---------- Reveal on scroll ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '80px 0px 80px 0px', threshold: 0.06 });
  cards.forEach(c => io.observe(c));

  /* ---------- Hover “lift” + micro tilt ---------- */
  const clamp = (n, min, max) => Math.min(max, Math.max(min, n));
  const enableTilt = (card) => {
    card.classList.add('is-interactive');
    let raf = null;
    const onMove = (e) => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width;   // 0..1
      const y = (e.clientY - r.top) / r.height;   // 0..1
      const rotY = clamp((x - 0.5) * 6, -6, 6);
      const rotX = clamp((0.5 - y) * 6, -6, 6);
      if (raf) cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        card.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-2px)`;
      });
    };
    const reset = () => { card.style.transform = ''; };
    card.addEventListener('mousemove', onMove);
    card.addEventListener('mouseleave', reset);
    card.addEventListener('blur', reset, true);
  };
  cards.forEach(enableTilt);

  /* ---------- Wishlist hearts (localStorage) ---------- */
  const KEY = 'mc_wishlist';
  const readSet = () => new Set(JSON.parse(localStorage.getItem(KEY) || '[]'));
  const writeSet = (set) => localStorage.setItem(KEY, JSON.stringify([...set]));
  const wish = readSet();

  cards.forEach(card => {
    const id = card.getAttribute('data-car-id');
    const btn = qs('.car-card__wish', card);
    if (!btn || !id) return;

    const sync = (active) => {
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-pressed', String(active));
      btn.textContent = active ? '♥' : '♡';
    };
    sync(wish.has(id));

    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const now = !wish.has(id);
      if (now) wish.add(id); else wish.delete(id);
      writeSet(wish);
      sync(now);
    });
  });

  /* ---------- Quick spec peek (optional) ---------- */
  const showPeek = (card) => {
    const spec = card.getAttribute('data-car-spec');
    if (!spec) return;
    let peek = qs('.car-card__peek', card);
    if (!peek) {
      peek = document.createElement('div');
      peek.className = 'car-card__peek';
      peek.style.cssText = `
        position:absolute; inset:auto 0 0 0; padding:.6rem .8rem;
        background:rgba(0,0,0,.55); color:#fff; font-size:.875rem;
        transform: translateY(100%); transition: transform .2s ease;
      `;
      qs('.ratio', card)?.appendChild(peek);
    }
    peek.textContent = spec;
    peek.style.transform = 'translateY(0)';
    setTimeout(() => { peek.style.transform = 'translateY(100%)'; }, 1600);
  };

  cards.forEach(card => {
    const imgWrap = qs('.ratio', card);
    if (!imgWrap) return;
    imgWrap.addEventListener('click', (e) => {
      if (e.target.closest('a')) return; // don’t block Details link
      showPeek(card);
    });
  });
})();
