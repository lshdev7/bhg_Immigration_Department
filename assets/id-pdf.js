/* Baekhyeon Hwarang Smart Identity Card (front + back, ID-1 card size) as a PDF, drawn in the browser.
   Layout follows the Hong Kong smart identity card issued from 26 November 2018; symbols follow the
   HKID symbol system (stars, A/R/U/C, B, N, Y, place-of-birth letter, L). Uses BHGMakePDF from passport-pdf.js. */
(function () {
  "use strict";
  var BASE = (function () { var s = document.currentScript && document.currentScript.src; return s ? s.replace(/[^\/]*$/, "") : "../../assets/"; })();
  var W = 1012, H = 638, TEAL = "#13808f", INK = "#1b1b1b";
  var MONO = '"OCR B","OCR-B","Courier New",Courier,monospace';
  var CJK = '"Noto Sans TC","Microsoft JhengHei","PingFang TC","Noto Sans KR","Malgun Gothic",sans-serif';
  var OFFICE = { hq: "B1", b3: "B3", b4: "B4" };

  function z(n) { return (n < 10 ? "0" : "") + n; }
  function load(src) { return new Promise(function (ok, bad) { var im = new Image(); im.onload = function () { ok(im); }; im.onerror = bad; im.src = src; }); }
  function canvas() { var c = document.createElement("canvas"); c.width = W; c.height = H; return c; }
  function cover(x, img, dx, dy, dw, dh) { var r = Math.max(dw / img.width, dh / img.height), sw = dw / r, sh = dh / r; x.drawImage(img, (img.width - sw) / 2, (img.height - sh) / 2, sw, sh, dx, dy, dw, dh); }

  /* ---------------------------------------------------------------- number and symbols */
  function checkChar(letters, digits) {
    var c = function (ch) { return ch.charCodeAt(0) - 55; }, sum = letters.length === 1 ? 36 * 9 + c(letters) * 8 : c(letters[0]) * 9 + c(letters[1]) * 8;
    for (var i = 0; i < 6; i++) sum += (+digits[i]) * (7 - i);
    var k = (11 - sum % 11) % 11; return k === 10 ? "A" : String(k);
  }
  function idPrefix(pob, dob) {   // births in BHG follow the birth register; everyone else is first registered now
    if (pob !== "BHG" || !dob || dob < "1980-01-01") return "L";
    return dob < "1989-01-01" ? "Z" : dob < "2005-04-01" ? "Y" : dob < "2019-06-01" ? "S" : "N";
  }
  function newNumber(pob, dob) {
    var L = idPrefix(pob, dob), d = "";
    for (var i = 0; i < 6; i++) d += Math.floor(Math.random() * 10);
    return L + d + "(" + checkChar(L, d) + ")";
  }
  function ageOn(dob, now) { var a = now.getFullYear() - dob.getFullYear(); if (now.getMonth() < dob.getMonth() || (now.getMonth() === dob.getMonth() && now.getDate() < dob.getDate())) a--; return a; }
  function symbols(v, age) {
    var s = "";
    if (v.kornat === "KOR" && v.status === "A") s += age >= 18 ? "***" : "*";
    s += v.status || "";
    if (v.chgbirth === "Y") s += "B";
    if (v.chgname === "Y") s += "N";
    if (v.dobproof === "Y") s += "Y";
    s += v.pob === "BHG" ? "Z" : v.pob === "KR" ? "X" : "O";
    return s;
  }
  function commercialCode(local) {
    var out = [], chars = Array.from((local || "").replace(/\s+/g, ""));
    chars.slice(0, 6).forEach(function (ch) { out.push(("0000" + (ch.codePointAt(0) % 10000)).slice(-4)); });
    return out.join(" ");
  }
  function titleCase(s) { return (s || "").toLowerCase().replace(/(^|[\s\-'])([a-z])/g, function (m, a, b) { return a + b.toUpperCase(); }); }

  function build(v) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v.dob || "") || [0, 2000, 1, 1], dob = new Date(+m[1], +m[2] - 1, +m[3]), now = v.issued ? new Date(v.issued) : new Date();
    var age = ageOn(dob, now), first = v.idtype === "first";
    var fr = first ? z(now.getMonth() + 1) + "-" + String(now.getFullYear()).slice(2) : (v.firstreg || "").replace(/\s/g, "");
    var no = v.idno ? String(v.idno) : first ? newNumber(v.pob, v.dob) : String(v.oldid || "").toUpperCase().replace(/\s/g, "").replace(/^([A-Z]{1,2}\d{6})\(?([0-9A])\)?$/, "$1($2)");
    return {
      permanent: v.status === "A", status: v.status, age: age, no: no, window: no.replace(/\(.*$/, ""),
      local: v.local || "", en: (v.surname || "").toUpperCase() + ", " + titleCase(v.given),
      ccc: commercialCode(v.local), dob: z(+m[3]) + "-" + m[2] + "-" + m[1], sex: v.sex === "F" ? "女 F" : "男 M",
      sym: symbols(v, age), firstReg: "(" + fr + ")", reg: z(now.getDate()) + "-" + z(now.getMonth() + 1) + "-" + String(now.getFullYear()).slice(2),
      office: (OFFICE[v.office] || "B1") + (v.idtype === "lost" ? " L" : "")
    };
  }

  /* ---------------------------------------------------------------- artwork */
  function star(x, cx, cy, r) {
    x.beginPath();
    for (var i = 0; i < 10; i++) { var a = -Math.PI / 2 + i * Math.PI / 5, q = i % 2 ? r * .42 : r; x.lineTo(cx + q * Math.cos(a), cy + q * Math.sin(a)); }
    x.closePath(); x.fill();
  }
  function flower(x, cx, cy, r, rot) {
    for (var k = 0; k < 5; k++) {
      x.save(); x.translate(cx, cy); x.rotate(rot + k * Math.PI * 2 / 5);
      x.beginPath(); x.moveTo(0, 0);
      x.bezierCurveTo(r * .5, -r * .2, r * .98, r * .2, r * .66, r * .6);
      x.bezierCurveTo(r * .45, r * .82, r * .1, r * .55, 0, 0);
      x.fill();
      x.fillStyle = "rgba(108,149,201,.85)"; star(x, r * .5, r * .38, r * .05);
      x.restore(); x.fillStyle = "rgba(255,255,255,.72)";
    }
  }
  function background(x, mirror) {
    var g = x.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, "#e1f0cc"); g.addColorStop(.45, "#d5ecf3"); g.addColorStop(1, "#f2dbe7");
    x.fillStyle = g; x.fillRect(0, 0, W, H);
    var rg = x.createRadialGradient(W * .78, H * .1, 10, W * .78, H * .1, 420); rg.addColorStop(0, "rgba(246,214,228,.9)"); rg.addColorStop(1, "rgba(246,214,228,0)");
    x.fillStyle = rg; x.fillRect(0, 0, W, H);
    x.save(); x.lineWidth = .6;
    for (var i = 0; i < 70; i++) {
      x.strokeStyle = i % 3 ? "rgba(255,255,255,.45)" : "rgba(19,128,143,.08)";
      x.beginPath();
      for (var X = 0; X <= W; X += 8) { var Y = H * i / 70 + Math.sin(X / 48 + i * .4) * 9 + Math.sin(X / 13 + i) * 2; if (X) x.lineTo(X, Y); else x.moveTo(X, Y); }
      x.stroke();
    }
    x.restore();
    x.fillStyle = "rgba(255,255,255,.72)"; flower(x, mirror ? W * .74 : W * .58, H * .5, 250, -.3);
  }
  function round(x) { x.save(); x.globalCompositeOperation = "destination-in"; x.beginPath(); var r = 34; x.moveTo(r, 0); x.arcTo(W, 0, W, H, r); x.arcTo(W, H, 0, H, r); x.arcTo(0, H, 0, 0, r); x.arcTo(0, 0, W, 0, r); x.fill(); x.globalCompositeOperation = "destination-over"; x.fillStyle = "#fff"; x.fillRect(0, 0, W, H); x.restore(); }
  function txt(x, s, px, py, font, color, align) { x.font = font; x.fillStyle = color || INK; x.textAlign = align || "left"; x.fillText(s, px, py); }
  function gray(img, w, h) {
    var c = document.createElement("canvas"); c.width = w; c.height = h; var x = c.getContext("2d"); cover(x, img, 0, 0, w, h);
    var d = x.getImageData(0, 0, w, h); for (var i = 0; i < d.data.length; i += 4) { var v = d.data[i] * .3 + d.data[i + 1] * .59 + d.data[i + 2] * .11; d.data[i] = d.data[i + 1] = d.data[i + 2] = v; }
    x.putImageData(d, 0, 0); return c;
  }
  function seeThrough(x, cx, cy, s, mirror) {
    x.save(); x.translate(cx, cy); if (mirror) x.scale(-1, 1);
    var g = x.createLinearGradient(-90, 0, 90, 0); g.addColorStop(0, "rgba(255,255,255,.95)"); g.addColorStop(1, "rgba(220,225,230,.95)");
    x.fillStyle = g; x.beginPath(); x.ellipse(0, 0, 92, 22, 0, 0, 7); x.fill(); x.strokeStyle = "rgba(120,120,120,.5)"; x.lineWidth = 1.5; x.stroke();
    x.font = 'italic 700 22px ' + MONO; x.fillStyle = "#333"; x.textAlign = "center"; x.textBaseline = "middle"; x.fillText(s, 0, 1);
    x.restore(); x.textBaseline = "alphabetic";
  }

  function front(d, photo) {
    var c = canvas(), x = c.getContext("2d");
    background(x, false);
    txt(x, d.permanent ? "柏峴화랑永久性居民身份證" : "柏峴화랑居民身份證", W * .53, 66, "700 38px " + CJK, TEAL, "center");
    txt(x, d.permanent ? "BAEKHYEON HWARANG PERMANENT IDENTITY CARD" : "BAEKHYEON HWARANG IDENTITY CARD", W * .53, 104, "600 27px Arial,Helvetica,sans-serif", TEAL, "center");
    seeThrough(x, 800, 150, d.window, false);
    if (d.local) txt(x, d.local.split("").join(" "), 92, 182, "500 38px " + CJK, INK);
    var en = d.en; x.font = "600 31px " + MONO; var ew = x.measureText(en).width;
    x.save(); x.translate(92, 228); if (ew > 540) x.scale(540 / ew, 1); txt(x, en, 0, 0, "600 31px " + MONO, INK); x.restore();
    if (d.ccc) txt(x, d.ccc, 400, 282, "600 31px " + MONO, INK);
    cover(x, photo, 70, 252, 300, 340);
    x.save(); x.globalAlpha = .55; x.drawImage(gray(photo, 104, 128), 772, 376); x.restore();
    txt(x, "出生日期", 400, 330, "500 21px " + CJK, TEAL); txt(x, "Date of Birth", 492, 330, "500 21px Arial,Helvetica,sans-serif", TEAL);
    txt(x, d.dob, 400, 372, "600 33px " + MONO, INK); txt(x, d.sex, 640, 372, "600 33px " + MONO, INK);
    txt(x, d.sym, 400, 418, "600 33px " + MONO, INK);
    txt(x, "簽發日期", 400, 458, "500 21px " + CJK, TEAL); txt(x, "Date of Issue", 492, 458, "500 21px Arial,Helvetica,sans-serif", TEAL);
    txt(x, d.firstReg, 400, 500, "600 33px " + MONO, INK);
    txt(x, d.reg, 400, 590, "600 36px " + MONO, INK); txt(x, d.no, 660, 590, "600 36px " + MONO, INK);
    round(x); return c;
  }

  function back(d, flag) {
    var c = canvas(), x = c.getContext("2d");
    background(x, true);
    x.save(); x.beginPath(); x.arc(W * .5, 92, 58, 0, 7); x.clip(); cover(x, flag, W * .5 - 88, 34, 176, 116); x.restore();
    seeThrough(x, 300, 156, d.window, true);
    // contact chip
    var cg = x.createLinearGradient(80, 210, 220, 330); cg.addColorStop(0, "#f3d98e"); cg.addColorStop(.5, "#c99a3c"); cg.addColorStop(1, "#f0d48a");
    x.fillStyle = cg; x.beginPath(); x.roundRect ? x.roundRect(80, 214, 150, 118, 18) : x.rect(80, 214, 150, 118); x.fill();
    x.strokeStyle = "rgba(110,80,20,.65)"; x.lineWidth = 2;
    [[80, 254, 135, 254], [80, 293, 135, 293], [175, 254, 230, 254], [175, 293, 230, 293], [155, 214, 155, 250], [155, 297, 155, 332]].forEach(function (l) { x.beginPath(); x.moveTo(l[0], l[1]); x.lineTo(l[2], l[3]); x.stroke(); });
    x.strokeRect(120, 250, 70, 48);
    x.fillStyle = "#8a4a1c"; x.beginPath(); x.moveTo(28, 270); x.lineTo(58, 236); x.lineTo(58, 304); x.closePath(); x.fill();
    var cx = W * .56;
    if (d.permanent) {
      txt(x, "本證持有人擁有柏峴화랑居留權", cx, 300, "500 31px " + CJK, TEAL, "center");
      txt(x, "The holder of this card has", cx, 344, "700 27px Arial,Helvetica,sans-serif", TEAL, "center");
      txt(x, "the right of abode in Baekhyeon Hwarang", cx, 380, "700 27px Arial,Helvetica,sans-serif", TEAL, "center");
    } else if (d.status === "R") {
      txt(x, "本證持有人擁有柏峴화랑入境權", cx, 300, "500 31px " + CJK, TEAL, "center");
      txt(x, "The holder of this card has", cx, 344, "700 27px Arial,Helvetica,sans-serif", TEAL, "center");
      txt(x, "the right to land in Baekhyeon Hwarang", cx, 380, "700 27px Arial,Helvetica,sans-serif", TEAL, "center");
    }
    txt(x, d.age >= 18 ? "適用於十八歲或以上的人士" : "適用於十八歲以下的人士", cx, 440, "500 26px " + CJK, INK, "center");
    txt(x, d.age >= 18 ? "FOR A PERSON OF THE AGE OF 18 OR OVER" : "FOR A PERSON UNDER THE AGE OF 18", cx, 472, "500 22px Arial,Helvetica,sans-serif", INK, "center");
    txt(x, d.office, 60, 600, "600 22px " + MONO, "#555");
    round(x); return c;
  }

  /* front and back as canvases (used by the iAM Smart app to show the issued card) */
  window.BHGIdCardImages = function (vals, photoFile) {
    var d = build(vals || {}), u = URL.createObjectURL(photoFile);
    return Promise.all([load(u), load(BASE + "flag.jpg")]).then(function (im) { URL.revokeObjectURL(u); return { no: d.no, sym: d.sym, front: front(d, im[0]), back: back(d, im[1]) }; });
  };
  window.BHGIdCardPDF = function (vals, photoFile) {
    var d = build(vals || {}), u = URL.createObjectURL(photoFile);
    return Promise.all([load(u), load(BASE + "flag.jpg")]).then(function (im) {
      URL.revokeObjectURL(u);
      var pages = [{ canvas: front(d, im[0]), w: 85.6, h: 54 }, { canvas: back(d, im[1]), w: 85.6, h: 54 }];
      var blob = window.BHGMakePDF(pages), a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = "BHG-Smart-ID-" + d.no.replace(/[()]/g, "") + ".pdf";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 60000);
      return { no: d.no, sym: d.sym, size: blob.size };
    });
  };
})();
