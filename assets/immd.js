(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* text size */
  var ts = $("#textsize");
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function size(n) { document.body.classList.remove("size-0", "size-2"); if (n !== 1) document.body.classList.add("size-" + n); store("immd-size", String(n)); }
  var sv = store("immd-size"); size(sv === "0" ? 0 : sv === "2" ? 2 : 1);
  if (ts) ts.addEventListener("click", function () { var c = document.body.classList.contains("size-2") ? 2 : document.body.classList.contains("size-0") ? 0 : 1; size(c === 1 ? 2 : c === 2 ? 0 : 1); });

  /* FAQ accordion */
  $$(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () { var o = q.getAttribute("aria-expanded") === "true"; q.setAttribute("aria-expanded", String(!o)); q.nextElementSibling.hidden = o; });
  });
  $$("[data-faq]").forEach(function (b) {
    b.addEventListener("click", function () { var o = b.getAttribute("data-faq") === "open"; $$(".faq-q").forEach(function (q) { q.setAttribute("aria-expanded", String(o)); q.nextElementSibling.hidden = !o; }); });
  });

  /* application page: place of application + tabs + expand all */
  var place = $("#place"), tabBtns = $$(".tabs3 button");
  function showPanel() {
    if (!place) return;
    var cur = $(".tabs3 button.on"), t = cur ? cur.getAttribute("data-tab") : "before";
    $$(".tp").forEach(function (p) { p.hidden = !(p.getAttribute("data-place") === place.value && p.getAttribute("data-tab") === t); });
  }
  if (place) place.addEventListener("change", showPanel);
  tabBtns.forEach(function (b) { b.addEventListener("click", function () { tabBtns.forEach(function (x) { x.classList.toggle("on", x === b); }); showPanel(); }); });
  $$("[data-ea]").forEach(function (b) {
    b.addEventListener("click", function () {
      var p = b.closest(".tp"), ds = $$("details", p), open = ds.some(function (d) { return !d.open; });
      ds.forEach(function (d) { d.open = open; });
    });
  });

  /* e-service start page */
  var start = $("#start");
  if (start) {
    start.addEventListener("click", function () {
      if (!$("#agree").checked) { $("#agree-err").textContent = $("#agree-err").getAttribute("data-msg") || "!"; return; }
      $("#term").hidden = true; $("#svc").hidden = false;
      if (window.svcStart) window.svcStart();
      window.scrollTo(0, 0);
    });
    var rb = $("#retrieve"), box = $("#retrieve-box");
    rb.addEventListener("click", function () { box.hidden = !box.hidden; });
    $("#r_go").addEventListener("click", function () { $("#r_msg").textContent = $("#r_msg").getAttribute("data-msg") || ""; });
  }
  $$("[data-stub]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); }); });
})();
