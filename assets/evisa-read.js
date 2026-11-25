/* Reads the QR code of an "e-Visa" from a file (PDF, JPEG, GIF, PNG) or a canvas, on this device only.
   BHGEVisaRead.ready() / .canvas(canvas, quick) -> text or null / .file(file) -> Promise([texts]) */
(function () {
  "use strict";
  var BASE = (function () { var s = document.currentScript && document.currentScript.src; return s ? s.replace(/[^\/]*$/, "") : "../../assets/"; })(), jsqrP = null;
  function jsqr() {
    if (!jsqrP) jsqrP = new Promise(function (ok, bad) { if (window.jsQR) return ok(); var s = document.createElement("script"); s.src = BASE + "jsqr.js"; s.onload = ok; s.onerror = function () { jsqrP = null; bad(); }; document.head.appendChild(s); });
    return jsqrP;
  }
  /* QR code text in a canvas: the whole picture first, then the place of the code on the slip at several sizes */
  function qrIn(c, quick) {
    function tryAt(sx, sy, sw, sh, w) {
      var k = document.createElement("canvas"), x; k.width = Math.round(w); k.height = Math.round(w * sh / sw); x = k.getContext("2d"); x.fillStyle = "#fff"; x.fillRect(0, 0, k.width, k.height); x.drawImage(c, sx, sy, sw, sh, 0, 0, k.width, k.height);
      var d = x.getImageData(0, 0, k.width, k.height), r = window.jsQR(d.data, k.width, k.height, { inversionAttempts: "dontInvert" });
      return r && r.data || null;
    }
    var W = c.width, H = c.height, t = tryAt(0, 0, W, H, Math.min(W, 1200));
    if (t || quick) return t;
    [[.66, .13, .34, .24], [.5, 0, .5, .5]].some(function (b) { return [480, 720, 960, 1300].some(function (w) { t = tryAt(W * b[0], H * b[1], W * b[2], H * b[3], w); return t; }); });
    return t || (W > 1200 ? tryAt(0, 0, W, H, Math.min(W, 2600)) : null);
  }
  function evImages(f) {   // pictures of the pages: the file itself, or the JPEG pages inside a PDF
    function one(blob) { return new Promise(function (ok, bad) { var u = URL.createObjectURL(blob), im = new Image(); im.onload = function () { var c = document.createElement("canvas"); c.width = im.naturalWidth; c.height = im.naturalHeight; c.getContext("2d").drawImage(im, 0, 0); URL.revokeObjectURL(u); ok(c); }; im.onerror = bad; im.src = u; }); }
    if (!/pdf$/i.test(f.type) && !/\.pdf$/i.test(f.name)) return one(f).then(function (c) { return [c]; });
    return f.arrayBuffer().then(function (buf) {
      var b = new Uint8Array(buf), s = new TextDecoder("latin1").decode(b), jobs = [], re = /\/DCTDecode[\s\S]{0,300}?stream\r?\n/g, m;
      while ((m = re.exec(s))) { var st = m.index + m[0].length, e = s.indexOf("endstream", st); if (e > 0) { jobs.push(one(new Blob([b.slice(st, e)], { type: "image/jpeg" })).catch(function () { return null; })); re.lastIndex = e; } }
      return Promise.all(jobs).then(function (l) { return l.filter(Boolean); });
    });
  }

  window.BHGEVisaRead = {
    ready: jsqr, canvas: qrIn,
    file: function (f) { return Promise.all([jsqr(), evImages(f)]).then(function (x) { return x[1].map(function (c) { return qrIn(c); }).filter(Boolean); }); }
  };
})();
