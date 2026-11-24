/* "e-Visa" (Notification Slip for Entry Visa / Permit, Notification Slip for Conditions of Stay) as an A4 PDF,
   one page per person, laid out like the Immigration Department's notification slips. Needs qrcode.js and
   BHGMakePDF from passport-pdf.js. */
(function () {
  "use strict";
  var BASE = (function () { var s = document.currentScript && document.currentScript.src; return s ? s.replace(/[^\/]*$/, "") : "../../assets/"; })();
  var W = 1240, H = 1754;
  var SERIF = '"Times New Roman",Times,"Noto Serif TC","Noto Serif KR","PMingLiU","MingLiU","Batang",serif';
  var DEPT_ZH = "大韓民國柏峴화랑特別行政區政府入境事務處";
  var GOV_EN = "The Government of the Baekhyeon Hwarang Special Administrative Region of the Republic of Korea";
  var NOTES = [
    ["本通知書由大韓民國柏峴화랑特別行政區政府入境事務處發出，當中所載的資料可在入境事務處網站或「BHG政府一站通」的「電子簽證」查詢服務核實。",
     "This notification slip is issued by the Immigration Department, the Government of the Baekhyeon Hwarang Special Administrative Region of the Republic of Korea. The information contained herein can be verified through the “e-Visa” Enquiry service of the Immigration Department or GovBHG."],
    ["本通知書不是身分證明文件。", "This notification slip is not a proof of identity."],
    ["通知書持有人應把本通知書的軟複本儲存在流動裝置上，或把本通知書列印在一張A4白紙上，以便在有需要時出示以供查閱。", "This notification slip should be saved in soft copy on a mobile device or printed on a piece of A4 white paper for production for inspection as necessary."],
    ["本通知書載有個人資料，必須妥為保管。", "This notification slip contains personal data and must be kept in safe custody."]
  ];

  function load(src) { return new Promise(function (ok) { var im = new Image(); im.onload = function () { ok(im); }; im.onerror = function () { ok(null); }; im.src = src; }); }
  function txt(x, s, px, py, size, opt) {
    opt = opt || {};
    x.font = (opt.bold ? "700 " : "") + size + "px " + SERIF; x.fillStyle = "#111"; x.textAlign = opt.align || "left"; x.textBaseline = "alphabetic";
    x.fillText(s, px, py);
  }
  function wrap(x, s, px, py, size, maxw, lh, cjk) {
    x.font = size + "px " + SERIF; x.fillStyle = "#111"; x.textAlign = "left";
    var parts = cjk ? Array.from(s) : s.split(" "), line = "", y = py;
    parts.forEach(function (w) {
      var t = line ? line + (cjk ? "" : " ") + w : w;
      if (x.measureText(t).width > maxw && line) { x.fillText(line, px, y); y += lh; line = w; } else line = t;
    });
    if (line) { x.fillText(line, px, y); y += lh; }
    return y;
  }
  function qr(x, data, px, py, size) {
    if (!window.qrcode) return;
    var q = window.qrcode(0, "M"); q.addData(unescape(encodeURIComponent(data)), "Byte"); q.make();
    var n = q.getModuleCount(), c = size / n;
    x.fillStyle = "#000";
    for (var r = 0; r < n; r++) for (var k = 0; k < n; k++) if (q.isDark(r, k)) x.fillRect(Math.floor(px + k * c), Math.floor(py + r * c), Math.ceil(c), Math.ceil(c));
  }

  function bodyLines(rec) {
    var n = rec.days ? rec.days : rec.months, uz = rec.days ? " 日" : " 個月", ue = rec.days ? " days" : " months";
    var L = [];
    if (rec.mode === "ext") {
      L.push(["zh", rec.slip[0] + "-獲准逗留期限延至" + rec.until]);
      L.push(["en", rec.slip[1] + " - Permission to remain extended until " + rec.until]);
      L.push(["gap"]);
      L.push(["zhs", "已施加於你的逗留期限及逗留條件（如有），對於你在該逗留期限的有效期內再次入境時仍然適用，除非該逗留期限及逗留條件已期滿失效、或被撤銷、變更、縮短期限或因任何理由而變為無效。"]);
      L.push(["ens", "The limit and condition(s) of stay, if any, imposed on you will, unless expired, cancelled, varied, curtailed or for whatever reason becomes invalid, apply to any subsequent landing in Baekhyeon Hwarang within the currency of the limit of stay."]);
      return L;
    }
    L.push(["zh", rec.zh]);
    L.push(["zh", "持證人可在 " + rec.valid + " 或以前"]);
    L.push(["zh", (rec.multi ? "多次" : "單次") + "進入柏峴화랑"]);
    L.push(["zh", (rec.employ ? "僱傭工作" : rec.slip[0]) + " " + n + uz]);
    L.push(["en", rec.en]);
    L.push(["en", "Good for " + (rec.multi ? "Multiple journeys" : "Single journey") + " to Baekhyeon Hwarang"]);
    L.push(["en", "valid for presentation on or before " + rec.valid]);
    L.push(["en", (rec.employ ? "EMPLOYMENT" : rec.slip[1]) + " " + n + ue]);
    if (rec.emp) {
      L.push(["zh", rec.employ ? "為以下僱主工作" : "擔保人／機構"]);
      L.push(["en", rec.employ ? "For employment with" : "Sponsor / institution"]);
      L.push(["en", String(rec.emp).toUpperCase()]);
    }
    L.push(["gap"]);
    if (rec.employ) {
      L.push(["zhs", "未得入境事務處處長批准，不得轉換工作。"]);
      L.push(["ens", "Change of employment without approval of the Director of Immigration is not permitted."]);
    } else if (rec.slip[1] === "VISIT" || rec.slip[1] === "VISITOR") {
      L.push(["zhs", "不得接受僱傭工作（不論是否受薪）、開辦或參與任何業務，或以學生身份入學。"]);
      L.push(["ens", "Taking up employment (paid or unpaid), establishing or joining in any business, or entering school as a student is not permitted."]);
    }
    L.push(["zhs", "本進入許可必須與有效旅行證件一併於辦理入境手續時出示，方為有效。"]);
    L.push(["ens", "This entry permit is valid only if it is presented together with a valid travel document upon immigration arrival clearance."]);
    return L;
  }

  function page(rec, person, flag) {
    var c = document.createElement("canvas"); c.width = W; c.height = H;
    var x = c.getContext("2d");
    x.fillStyle = "#fff"; x.fillRect(0, 0, W, H);
    var L = 160, R = W - 160, code = rec.ref.slice(0, 4);
    txt(x, "申請檔案編號 Application Reference No.: " + rec.ref, L, 168, 25);
    txt(x, code, R, 168, 25, { align: "right" });
    txt(x, DEPT_ZH, W / 2, 228, 30, { align: "center" });
    txt(x, "Immigration Department", W / 2, 266, 28, { align: "center" });
    txt(x, GOV_EN, W / 2, 300, 24, { align: "center" });
    // watermark: regional flag, faded
    if (flag) {
      x.save(); x.globalAlpha = 0.09; x.beginPath(); x.arc(W / 2, 760, 380, 0, 7); x.clip();
      var r = Math.max(760 / flag.width, 760 / flag.height);
      x.drawImage(flag, W / 2 - flag.width * r / 2, 760 - flag.height * r / 2, flag.width * r, flag.height * r); x.restore();
    }
    x.strokeStyle = "#111"; x.lineWidth = 2.2;
    var top = 312, bot;
    var ext = rec.mode === "ext";
    txt(x, ext ? "逗留條件通知書" : "入境簽證 / 進入許可通知書", W / 2, top + 36, 27, { align: "center" });
    txt(x, ext ? "Notification Slip for Conditions of Stay" : "Notification Slip for Entry Visa / Permit", W / 2, top + 72, 26, { align: "center" });
    var r1 = top + 92, r2 = r1 + 128, r3 = r2 + 140, c1 = L + 255, c2 = R - 220;
    [[L, r1, R, r1], [L, r3, R, r3], [L, r2, c2, r2], [c1, r1, c1, r3], [c2, r1, c2, r3]].forEach(function (l) { x.beginPath(); x.moveTo(l[0], l[1]); x.lineTo(l[2], l[3]); x.stroke(); });
    txt(x, "姓名", L + 8, r1 + 48, 24); txt(x, "Name", L + 8, r1 + 80, 23);
    if (person.local) { txt(x, person.local, c1 + 16, r1 + 48, 25); txt(x, person.name, c1 + 16, r1 + 82, 25); }
    else txt(x, person.name, c1 + 16, r1 + 62, 25);
    txt(x, "出生日期（日-月-年）", L + 8, r2 + 58, 24); txt(x, "Date of birth (day-month-year)", L + 8, r2 + 92, 19);
    var dob = /^(\d{4})-(\d{2})-(\d{2})$/.exec(person.dob || "");
    txt(x, dob ? dob[3] + "-" + dob[2] + "-" + dob[1] : "", c1 + 16, r2 + 78, 25);
    qr(x, "BHG-EVISA|" + rec.ref + "|" + person.name + "|" + (person.dob || "") + "|" + (ext ? rec.until : rec.valid), c2 + 26, r1 + 22, 220 - 52);
    // conditions
    var y = r3 + 42, maxw = R - L - 40;
    bodyLines(rec).forEach(function (ln) {
      if (ln[0] === "gap") { y += 18; return; }
      if (ln[0] === "zh" || ln[0] === "en") { txt(x, ln[1], L + 18, y, 26); y += 36; return; }
      y = wrap(x, ln[1], L + 18, y, 22, maxw, 28, ln[0] === "zhs");
    });
    // important notes
    var nt = 1100;
    x.beginPath(); x.moveTo(L, nt); x.lineTo(R, nt); x.stroke();
    txt(x, "重要事項  Important notes", L + 10, nt + 32, 22, { bold: true });
    var ny = nt + 70;
    NOTES.forEach(function (n, k) {
      txt(x, "(" + (k + 1) + ")", L + 8, ny, 22);
      ny = wrap(x, n[0], L + 52, ny, 22, R - L - 70, 28, true);
      ny = wrap(x, n[1], L + 52, ny, 20, R - L - 70, 26, false) + 14;
    });
    bot = Math.max(ny + 4, 1500);
    x.strokeStyle = "#111"; x.lineWidth = 2.2; x.strokeRect(L, top, R - L, bot - top);
    // footer
    var fee = (+rec.fee || 0).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    txt(x, "(11/2026)", L, bot + 50, 17);
    txt(x, "經已繳費", W / 2 - 120, bot + 50, 24, { align: "center" });
    txt(x, "Fee Paid BH$" + fee, W / 2 + 160, bot + 50, 24, { align: "center" });
    txt(x, rec.issued, R, bot + 50, 24, { align: "right" });
    return c;
  }

  window.BHGEVisaPDF = function (rec, onlyDob) {
    if (!rec) return Promise.resolve(null);
    return load(BASE + "flag.jpg").then(function (flag) {
      var ppl = rec.people.filter(function (p) { return !onlyDob || p.dob === onlyDob; });
      var pages = ppl.map(function (p) { return { canvas: page(rec, p, flag), w: 210, h: 297 }; });
      var blob = window.BHGMakePDF(pages), a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = "e-Visa-" + rec.ref.replace(/[()]/g, "") + ".pdf";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 60000);
      return blob.size;
    });
  };
})();
