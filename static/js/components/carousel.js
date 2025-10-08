document.addEventListener("DOMContentLoaded", function () {
  var root = document.querySelector(".hero__glide");
  if (!root) return;

  var glide = new Glide(root, {
    type: "carousel",
    autoplay: 4500,
    hoverpause: true,
    animationDuration: 600,
    perView: 1,
    gap: 0,
    rewind: true
  });

  // Build bullets dynamically so they match your slides
  var track = root.querySelector(".glide__track");
  var slides = track ? track.querySelectorAll(".glide__slide") : [];
  var bulletsWrap = root.querySelector(".glide__bullets");
  if (bulletsWrap && slides.length > 1) {
    slides.forEach(function (_, i) {
      var b = document.createElement("button");
      b.className = "glide__bullet";
      b.setAttribute("data-glide-dir", "=" + i);
      bulletsWrap.appendChild(b);
    });
  }

  glide.mount();
});
