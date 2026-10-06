// Open links to other websites in a new browser tab.
// `document$` fires on every page load, including instant navigation.
document$.subscribe(function () {
  document.querySelectorAll(".md-content a[href]").forEach(function (link) {
    if (link.hostname && link.hostname !== window.location.hostname) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener");
    }
  });
});
