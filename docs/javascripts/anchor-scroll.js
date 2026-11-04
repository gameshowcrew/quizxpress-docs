// Pictures load lazily and have no reserved height, so a link to a section further down a page
// first jumps to the section and is then pushed away when the pictures above it load.
// Load the pictures above the target first, then scroll to the target again.
document$.subscribe(function () {
  if (!location.hash) return;
  var target;
  try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (e) { return; }
  if (!target) return;

  var pending = Array.prototype.filter.call(document.querySelectorAll(".md-content img"), function (img) {
    return (target.compareDocumentPosition(img) & Node.DOCUMENT_POSITION_PRECEDING) && !img.complete;
  });
  if (!pending.length) return;

  var waiting = pending.map(function (img) {
    return new Promise(function (resolve) {
      img.addEventListener("load", resolve);
      img.addEventListener("error", resolve);
      img.loading = "eager";
    });
  });
  Promise.all(waiting).then(function () { target.scrollIntoView(); });
});
