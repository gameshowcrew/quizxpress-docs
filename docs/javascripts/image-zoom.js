// Click a screenshot to see it full size; click again or press Esc to close.
(function () {
  var overlay = document.createElement("div");
  overlay.className = "qx-zoom";
  overlay.innerHTML = "<img alt=''>";
  var big = overlay.firstChild;
  function close() { overlay.classList.remove("qx-zoom--open"); }
  overlay.addEventListener("click", close);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
  document.body.appendChild(overlay);

  document$.subscribe(function () {
    document.querySelectorAll(".md-content img:not(.inline-icon)").forEach(function (img) {
      if (img.closest("a") || img.dataset.zoom) return;
      img.dataset.zoom = "1";
      img.addEventListener("click", function () {
        big.src = img.currentSrc || img.src;
        big.alt = img.alt;
        overlay.classList.add("qx-zoom--open");
      });
    });
  });
})();
