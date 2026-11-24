/* Builds a Baekhyeon Hwarang SAR passport booklet (cover, request page, personalised data page, visa pages,
   notes page, back cover) as a PDF entirely in the browser. Page images are drawn on canvas and embedded
   as JPEG (DCTDecode) in a small hand-written PDF. */
(function () {
  "use strict";
  var BASE = (function () { var s = document.currentScript && document.currentScript.src; return s ? s.replace(/[^\/]*$/, "") : "../../assets/"; })();
  var MON = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];
  var MM = 72 / 25.4;   // points per mm

  function load(src) {
    return new Promise(function (ok, bad) { var im = new Image(); im.onload = function () { ok(im); }; im.onerror = bad; im.src = src; });
  }
  function canvas(w, h) { var c = document.createElement("canvas"); c.width = w; c.height = h; return c; }
  function z(n) { return (n < 10 ? "0" : "") + n; }

  /* ---------------------------------------------------------------- MRZ (ICAO 9303) */
  function cv(ch) { if (ch >= "0" && ch <= "9") return +ch; if (ch === "<") return 0; return ch.charCodeAt(0) - 55; }
  function chk(s) { var w = [7, 3, 1], t = 0; for (var i = 0; i < s.length; i++) t += cv(s.charAt(i)) * w[i % 3]; return String(t % 10); }
  function mrzName(s) { return s.toUpperCase().replace(/[^A-Z ]/g, "").trim().replace(/\s+/g, "<"); }
  function pad(s, n) { s = s.slice(0, n); while (s.length < n) s += "<"; return s; }
  function mrz(d) {
    var l1 = pad("P<BHG" + mrzName(d.surname) + "<<" + mrzName(d.given), 44);
    var no = pad(d.no, 9), dob = d.dob.y2 + d.dob.m2 + d.dob.d2, exp = d.exp.y2 + d.exp.m2 + d.exp.d2, pn = pad("", 14);
    var body = no + chk(no) + "KOR" + dob + chk(dob) + d.sex + exp + chk(exp) + pn + chk(pn);
    var comp = chk(body.slice(0, 10) + body.slice(13, 20) + body.slice(21, 43));
    return [l1, body + comp];
  }

  /* ---------------------------------------------------------------- data */
  function parts(date) { return { d: date.getDate(), m: date.getMonth(), y: date.getFullYear(), d2: z(date.getDate()), m2: z(date.getMonth() + 1), y2: String(date.getFullYear()).slice(2) }; }
  function fmt(p) { return p.d2 + " " + MON[p.m] + " " + p.y2; }
  function splitLocal(s) {
    s = (s || "").trim();
    if (!s) return ["", ""];
    var sp = s.split(/\s+/);
    if (sp.length > 1) return [sp[0], sp.slice(1).join(" ")];
    return [s.charAt(0), s.slice(1)];
  }
  function build(v) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v.dob || "") || [0, 2000, 1, 1];
    var dob = new Date(+m[1], +m[2] - 1, +m[3]), now = new Date();
    var years = (v.ageGroup === "18+" || v.ageGroup === "16-17") ? 10 : 5;
    var exp = new Date(now.getFullYear() + years, now.getMonth(), now.getDate());
    var no = "B"; for (var i = 0; i < 8; i++) no += Math.floor(Math.random() * 10);
    var loc = splitLocal(v.local);
    var d = {
      surname: (v.surname || "").toUpperCase(), given: (v.given || "").toUpperCase(), locS: loc[0], locG: loc[1],
      sex: v.sex === "F" ? "F" : "M", dob: parts(dob), iss: parts(now), exp: parts(exp), pob: (v.pob || "").toUpperCase(), no: no,
      pages: v.pages === "48" ? 48 : 32
    };
    d.mrz = mrz(d);
    return d;
  }

  /* ---------------------------------------------------------------- drawing helpers */
  function cover(ctx, img, x, y, w, h) {
    var r = Math.max(w / img.width, h / img.height), sw = w / r, sh = h / r;
    ctx.drawImage(img, (img.width - sw) / 2, (img.height - sh) / 2, sw, sh, x, y, w, h);
  }
  function text(ctx, s, x, y, size, weight, sx, color) {
    ctx.save(); ctx.translate(x, y); ctx.scale(sx || 1, 1);
    ctx.font = (weight || "700") + " " + size + 'px "Arial Narrow","Roboto Condensed","Helvetica Neue",Arial,"Noto Sans KR","Malgun Gothic","Microsoft JhengHei",sans-serif';
    ctx.fillStyle = color || "#1a1a1a"; ctx.textBaseline = "alphabetic"; ctx.fillText(s, 0, 0); ctx.restore();
  }
  function gray(img, w, h) {
    var c = canvas(w, h), x = c.getContext("2d"); cover(x, img, 0, 0, w, h);
    var d = x.getImageData(0, 0, w, h);
    for (var i = 0; i < d.data.length; i += 4) { var g = d.data[i] * .3 + d.data[i + 1] * .59 + d.data[i + 2] * .11; d.data[i] = d.data[i + 1] = d.data[i + 2] = g; }
    x.putImageData(d, 0, 0); return c;
  }
  function flower(ctx, cx, cy, r, rot) {
    for (var k = 0; k < 5; k++) {
      ctx.save(); ctx.translate(cx, cy); ctx.rotate(rot + k * Math.PI * 2 / 5);
      ctx.beginPath(); ctx.moveTo(0, 0);
      ctx.bezierCurveTo(r * .55, -r * .15, r * .95, r * .25, r * .62, r * .62);
      ctx.bezierCurveTo(r * .4, r * .85, r * .05, r * .55, 0, 0);
      ctx.fill(); ctx.restore();
    }
  }
  function guilloche(ctx, w, h, color, n, amp) {
    ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = 0.7;
    for (var i = 0; i < n; i++) {
      ctx.beginPath();
      for (var x = 0; x <= w; x += 6) {
        var y = h * (i + .5) / n + Math.sin(x / 55 + i * .7) * amp + Math.sin(x / 17 + i) * amp * .25;
        if (x) ctx.lineTo(x, y); else ctx.moveTo(x, y);
      }
      ctx.stroke();
    }
    ctx.restore();
  }
  function perforate(ctx, s, x, y, dot) {
    // passport number laser-perforated through the pages (5x7 dot glyphs)
    var G = { "0": "01110100011001110101110011000101110", "1": "00100011000010000100001000010001110", "2": "01110100010000100010001000100011111",
      "3": "11110000010000101110000010000111110", "4": "00010001100101010010111110001000010", "5": "11111100001111000001000011000101110",
      "6": "00110010001000011110100011000101110", "7": "11111000010001000100010000100001000", "8": "01110100011000101110100011000101110",
      "9": "01110100011000101111000010001001100", "B": "11110100011000111110100011000111110" };
    ctx.save(); ctx.fillStyle = "rgba(90,80,70,.55)";
    for (var i = 0; i < s.length; i++) {
      var g = G[s.charAt(i)] || ""; for (var k = 0; k < 35; k++) if (g.charAt(k) === "1") { ctx.beginPath(); ctx.arc(x + i * dot * 6.4 + (k % 5) * dot, y + Math.floor(k / 5) * dot, dot * .36, 0, 7); ctx.fill(); }
    }
    ctx.restore();
  }

  /* ---------------------------------------------------------------- pages */
  var PW = 660, PH = 938;   // portrait booklet page (88 x 125 mm) in pixels

  function pageBase(tone) {
    var c = canvas(PW, PH), x = c.getContext("2d");
    var g = x.createLinearGradient(0, 0, PW, PH); g.addColorStop(0, tone[0]); g.addColorStop(1, tone[1]);
    x.fillStyle = g; x.fillRect(0, 0, PW, PH);
    guilloche(x, PW, PH, tone[2], 34, 14);
    return [c, x];
  }

  function requestPage(flag) {
    var r = pageBase(["#f7f1e6", "#efe6d6", "rgba(150,120,80,.13)"]), c = r[0], x = r[1];
    x.save(); x.beginPath(); x.arc(PW / 2, 190, 70, 0, 7); x.clip(); cover(x, flag, PW / 2 - 105, 120, 210, 140); x.restore();
    x.textAlign = "center"; x.fillStyle = "#1d2b4a";
    x.font = '700 24px "Noto Sans TC","Microsoft JhengHei","Noto Sans KR",sans-serif';
    var zh = ["大韓民國柏峴화랑特別行政區行政長官", "請各國軍政機關對持照人", "予以通行便利及必要時予以", "協助和保護。"];
    zh.forEach(function (l, i) { x.fillText(l, PW / 2, 330 + i * 38); });
    x.font = '400 19px Georgia,"Times New Roman",serif';
    var en = ["The Chief Executive of the Baekhyeon Hwarang", "Special Administrative Region of the Republic of Korea", "requests all whom it may concern to allow the bearer", "to pass freely and without hindrance and to afford", "the bearer such assistance and protection", "as may be necessary."];
    en.forEach(function (l, i) { x.fillText(l, PW / 2, 530 + i * 30); });
    return c;
  }

  function dataPage(tpl, photo, d) {
    var c = canvas(tpl.width, tpl.height), x = c.getContext("2d");
    x.drawImage(tpl, 0, 0);
    // portraits
    cover(x, photo, 78, 198, 302, 386);
    x.save(); x.globalAlpha = .42; x.beginPath(); x.ellipse(1066, 268, 44, 56, 0, 0, 7); x.clip(); x.drawImage(gray(photo, 96, 120), 1018, 210); x.restore();
    x.save(); x.globalAlpha = .7; x.drawImage(gray(photo, 70, 86), 1135, 516); x.restore();
    x.save(); x.translate(1232, 584); x.rotate(-Math.PI / 2); text(x, "BHG", 0, 0, 22, "700", 1, "#333"); x.restore();
    // variable fields
    text(x, d.no, 948, 166, 32, "700", .92);
    text(x, (d.locS ? d.locS + " / " : "") + d.surname, 420, 238, 36, "700", .9);
    text(x, (d.locG ? d.locG + " / " : "") + d.given, 420, 316, 36, "700", .9);
    text(x, fmt(d.dob), 893, 394, 34, "700", .92);
    text(x, d.sex, 420, 462, 34, "700", .92);
    text(x, d.pob, 893, 462, 34, "700", .92);
    text(x, fmt(d.iss), 420, 532, 34, "700", .92);
    text(x, fmt(d.exp), 893, 532, 34, "700", .92);
    // machine readable zone
    x.fillStyle = "#151515"; x.font = '400 37px "OCR B","OCR-B","OCRB","Courier New",monospace';
    var step = (1205 - 62) / 44;
    d.mrz.forEach(function (line, li) { for (var k = 0; k < 44; k++) x.fillText(line.charAt(k), 62 + k * step, 718 + li * 60); });
    return c;
  }

  var SEASONS = [["#fdeff3", "#f6d9e3", "rgba(200,90,130,.13)", "rgba(214,98,140,.18)"], ["#e8f6ef", "#d2ebe1", "rgba(60,150,110,.13)", "rgba(50,150,120,.18)"],
                 ["#fdf3e2", "#f5e0c3", "rgba(190,120,40,.14)", "rgba(210,130,40,.18)"], ["#e8f0fa", "#d4e2f3", "rgba(60,100,170,.13)", "rgba(60,100,180,.18)"]];

  function visaPage(n, total, d) {
    var s = SEASONS[Math.min(3, Math.floor((n - 3) / Math.max(1, (total - 3) / 4)))];
    var r = pageBase(s), c = r[0], x = r[1];
    // ribbon
    x.save(); x.fillStyle = s[3]; x.beginPath(); x.moveTo(0, PH * .62);
    for (var X = 0; X <= PW; X += 10) x.lineTo(X, PH * .62 + Math.sin(X / 90 + n) * 40);
    for (X = PW; X >= 0; X -= 10) x.lineTo(X, PH * .7 + Math.sin(X / 80 + n + 1) * 36);
    x.closePath(); x.fill(); x.restore();
    // flower watermark (regional flower, as the bauhinia on HKSAR visa pages)
    x.save(); x.fillStyle = s[3]; flower(x, PW / 2, PH * .42, 210, n * .2); x.restore();
    x.save(); x.fillStyle = "rgba(255,255,255,.35)"; x.beginPath(); x.arc(PW / 2, PH * .42, 46, 0, 7); x.fill(); x.restore();
    // header, page numbers, micro-text, perforation
    x.fillStyle = "#3b3b3b"; x.textAlign = "center";
    x.font = '700 22px "Noto Sans TC","Microsoft JhengHei",sans-serif'; x.fillText("簽 證", PW / 2, 58);
    x.font = '700 15px Arial,Helvetica,sans-serif'; x.fillText("V I S A S", PW / 2, 80);
    x.font = '700 20px Arial,Helvetica,sans-serif'; x.textAlign = n % 2 ? "right" : "left"; x.fillText(String(n), n % 2 ? PW - 36 : 36, 52);
    x.textAlign = "center"; x.font = '400 15px Arial,Helvetica,sans-serif'; x.fillText(String(n), PW / 2, PH - 26);
    x.font = '400 5px Arial,Helvetica,sans-serif'; x.fillStyle = "rgba(60,60,60,.6)";
    var micro = ""; while (micro.length < 230) micro += "BAEKHYEONHWARANGSPECIALADMINISTRATIVEREGION";
    x.fillText(micro, PW / 2, PH - 52);
    var pw = d.no.length * 4.2 * 6.4; perforate(x, d.no, n % 2 ? PW - 40 - pw : 40, 108, 4.2);
    return c;
  }

  function notesPage(n) {
    var r = pageBase(["#f4f4f1", "#e7e6e0", "rgba(120,120,100,.12)"]), c = r[0], x = r[1];
    x.fillStyle = "#222"; x.textAlign = "center";
    x.font = '700 22px "Noto Sans TC","Microsoft JhengHei",sans-serif'; x.fillText("注 意 事 項", PW / 2, 70);
    x.font = '700 16px Arial,Helvetica,sans-serif'; x.fillText("NOTES", PW / 2, 94);
    var notes = [
      ["1. 本護照屬柏峴화랑特別行政區政府所有。", "This passport is the property of the Government of the", "Baekhyeon Hwarang Special Administrative Region."],
      ["2. 本護照如有遺失，應立即向入境事務處或", "If this passport is lost, report immediately to the Immigration", "Department or the nearest Korean Diplomatic and Consular Mission."],
      ["   最近的大韓民國駐外使領館報告。", "", ""],
      ["3. 持照人不得塗改本護照或將其轉讓他人使用。", "The holder must not alter this passport or permit", "any other person to use it."],
      ["4. 請妥為保管本護照。", "Please keep this passport in a safe place.", ""]
    ];
    x.textAlign = "left"; var y = 150;
    notes.forEach(function (nt) {
      x.font = '400 17px "Noto Sans TC","Microsoft JhengHei",sans-serif'; x.fillText(nt[0], 44, y); y += 26;
      x.font = '400 14px Arial,Helvetica,sans-serif';
      if (nt[1]) { x.fillText(nt[1], 66, y); y += 20; }
      if (nt[2]) { x.fillText(nt[2], 66, y); y += 20; }
      y += 16;
    });
    x.textAlign = "center"; x.font = '400 15px Arial,Helvetica,sans-serif'; x.fillText(String(n), PW / 2, PH - 26);
    return c;
  }

  function backCover() {
    var c = canvas(PW, PH), x = c.getContext("2d");
    x.fillStyle = "#13223f"; x.fillRect(0, 0, PW, PH);
    var d = x.getImageData(0, 0, PW, PH);
    for (var i = 0; i < d.data.length; i += 4) { var n = (Math.random() - .5) * 10; d.data[i] += n; d.data[i + 1] += n; d.data[i + 2] += n; }
    x.putImageData(d, 0, 0);
    return c;
  }
  function frontCover(img) { var c = canvas(PW, PH); cover(c.getContext("2d"), img, 0, 0, PW, PH); return c; }

  /* ---------------------------------------------------------------- PDF writer */
  function b64bytes(b64) { var s = atob(b64), u = new Uint8Array(s.length); for (var i = 0; i < s.length; i++) u[i] = s.charCodeAt(i); return u; }
  function makePDF(pages) {
    var enc = new TextEncoder(), chunks = [], offs = [], pos = 0;
    function put(x) { var b = typeof x === "string" ? enc.encode(x) : x; chunks.push(b); pos += b.length; }
    function obj(id, body) { offs[id] = pos; put(id + " 0 obj\n"); body(); put("\nendobj\n"); }
    put("%PDF-1.4\n%\xE2\xE3\xCF\xD3\n");
    var n = pages.length, kids = [];
    for (var i = 0; i < n; i++) kids.push((3 + i * 3) + " 0 R");
    obj(1, function () { put("<< /Type /Catalog /Pages 2 0 R >>"); });
    obj(2, function () { put("<< /Type /Pages /Count " + n + " /Kids [" + kids.join(" ") + "] >>"); });
    pages.forEach(function (p, i) {
      var pid = 3 + i * 3, iid = pid + 1, cid = pid + 2;
      var jpg = b64bytes(p.canvas.toDataURL("image/jpeg", .82).split(",")[1]);
      var w = (p.w * MM).toFixed(2), h = (p.h * MM).toFixed(2), cs = "q " + w + " 0 0 " + h + " 0 0 cm /Im Do Q";
      obj(pid, function () { put("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 " + w + " " + h + "] /Resources << /XObject << /Im " + iid + " 0 R >> >> /Contents " + cid + " 0 R >>"); });
      obj(iid, function () {
        put("<< /Type /XObject /Subtype /Image /Width " + p.canvas.width + " /Height " + p.canvas.height + " /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length " + jpg.length + " >>\nstream\n");
        put(jpg); put("\nendstream");
      });
      obj(cid, function () { put("<< /Length " + cs.length + " >>\nstream\n" + cs + "\nendstream"); });
    });
    var total = 3 + n * 3, xref = pos;
    var t = "xref\n0 " + total + "\n0000000000 65535 f \n";
    for (var k = 1; k < total; k++) t += ("0000000000" + offs[k]).slice(-10) + " 00000 n \n";
    put(t + "trailer\n<< /Size " + total + " /Root 1 0 R >>\nstartxref\n" + xref + "\n%%EOF\n");
    return new Blob(chunks, { type: "application/pdf" });
  }

  /* ---------------------------------------------------------------- public entry */
  window.BHGPassportPDF = function (vals, photoFile) {
    var d = build(vals || {});
    var photoUrl = URL.createObjectURL(photoFile);
    return Promise.all([load(BASE + "passport-cover.jpg"), load(BASE + "passport-datapage.jpg"), load(BASE + "flag.jpg"), load(photoUrl)]).then(function (im) {
      URL.revokeObjectURL(photoUrl);
      var P = [];
      P.push({ canvas: frontCover(im[0]), w: 88, h: 125 });
      P.push({ canvas: requestPage(im[2]), w: 88, h: 125 });
      P.push({ canvas: dataPage(im[1], im[3], d), w: 125, h: 88 });
      for (var n = 3; n < d.pages; n++) P.push({ canvas: visaPage(n, d.pages, d), w: 88, h: 125 });
      P.push({ canvas: notesPage(d.pages), w: 88, h: 125 });
      P.push({ canvas: backCover(), w: 88, h: 125 });
      var blob = makePDF(P), a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = "BHG-SAR-Passport-" + d.no + ".pdf";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 60000);
      return { no: d.no, pages: P.length, size: blob.size, mrz: d.mrz };
    });
  };
})();
