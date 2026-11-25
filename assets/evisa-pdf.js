/* "e-Visa" as an A4 PDF, one page per person. Forms and wording follow the Immigration Department's notification slips:
   entry visa / permit, conditions of stay, and the domestic helper slip for extension of stay and entry visa.
   The wording depends on the category. Needs qrcode.js and BHGMakePDF from passport-pdf.js. */
(function () {
  "use strict";
  var W = 1240, H = 1754, SCALE = 2, L = 163, R = 1116, TOP = 290, BOT = 1532;
  var SERIF = '"Times New Roman",Times,"Liberation Serif","Noto Serif TC","Noto Serif CJK TC","Noto Serif KR","PMingLiU","MingLiU","Batang",serif';
  var DEPT_ZH = "大韓民國柏峴화랑特別行政區政府入境事務處";
  var GOV_EN = "The Government of the Baekhyeon Hwarang Special Administrative Region of the Republic of Korea";
  var NOTES = [
    ["本通知書由大韓民國柏峴화랑特別行政區政府入境事務處發出，當中所載的資料可在入境事務處網站或「BHG政府一站通」核實。",
     "This notification slip is issued by the Immigration Department, the Government of the Baekhyeon Hwarang Special Administrative Region of the Republic of Korea. The information contained herein can be verified on the website of the Immigration Department or GovBHG."],
    ["本通知書不是身分證明文件。", "This notification slip is not a proof of identity."],
    ["通知書持有人應把本通知書的軟複本儲存在流動裝置上，或把本通知書列印在一張 A4 白紙上，以便在有需要時出示以供查閱。", "This notification slip should be saved in soft copy on a mobile device or printed on a piece of A4 white paper for production for inspection as necessary."],
    ["本通知書載有個人資料，必須妥為保管。", "This notification slip contains personal data and must be kept in safe custody."]
  ];
  var LIMIT = ["已施加於你的逗留期限及逗留條件（如有），對於你在該逗留期限的有效期內再次入境時仍然適用，除非該逗留期限及逗留條件已期滿失效、或被撤銷、變更、縮短期限或因任何理由而變為無效。",
    "The limit and condition(s) of stay, if any, imposed on you will, unless expired, cancelled, varied, curtailed or for whatever reason becomes invalid, apply to any subsequent landing in Baekhyeon Hwarang within the currency of the limit of stay."];
  var EEP = ["本進入許可必須與具有相關赴柏峴화랑簽注的有效往來柏峴화랑通行證一併於辦理入境手續時出示，方為有效。",
    "This entry permit is valid only if it is presented together with a valid Exit-entry Permit for Travelling to and from Baekhyeon Hwarang with relevant exit endorsement issued to the holder of this entry permit upon immigration arrival clearance."];
  var C_EMP = ["未得入境事務處處長批准，不得轉換工作。", "Change of employment without approval of the Director of Immigration is not permitted."];
  var C_STU = ["未得入境事務處處長批准，不得轉讀其他院校或其他課程。", "Change to another educational institution or another course of study without approval of the Director of Immigration is not permitted."];
  var C_IMP = ["不得轉換僱主或職位或受僱工作地點", "Change of employer or post or place of work is not permitted"];
  var C_FDH = ["不得轉換僱主或擔任駕駛車輛職務", "Change of employer or performing of motor vehicle driving duties is not permitted"];
  var C_VIS = ["訪客不得從事任何僱傭工作（不論有薪或無薪）；開辦或參與任何業務；及／或就讀於學校、大學或其他教育機構。",
    "A visitor shall not take any employment (whether paid or unpaid); establish or join in any business; and/or become a student at a school, university or other educational institution."];
  var C_INV = ["未得入境事務處處長批准，不得轉換業務或從事僱傭工作。", "Change of business or taking up employment without approval of the Director of Immigration is not permitted."];
  var C_TRN = ["未得入境事務處處長批准，不得轉換培訓機構或從事僱傭工作。", "Change of training company or taking up employment without approval of the Director of Immigration is not permitted."];
  var C_WHS = ["持證人以度假為主要目的，並可從事附帶性質的短期僱傭工作。", "The holder's main purpose is to holiday; short-term employment incidental to the holiday may be taken up."];
  var C_MFD = ["不得轉換僱主或受僱漁船", "Change of employer or fishing vessel is not permitted"];
  /* ISO 3166 alpha-2 -> alpha-3 for the code at the top right (nationality - type of travel document) */
  var A3 = {}; ("AFAFG AXALA ALALB DZDZA ASASM ADAND AOAGO AIAIA AQATA AGATG ARARG AMARM AWABW AUAUS ATAUT AZAZE BSBHS BHBHR BDBGD BBBRB BYBLR BEBEL BZBLZ BJBEN BMBMU BTBTN BOBOL BQBES BABIH BWBWA BVBVT BRBRA IOIOT BNBRN BGBGR BFBFA BIBDI CVCPV KHKHM CMCMR CACAN KYCYM CFCAF TDTCD CLCHL CNCHN CXCXR CCCCK COCOL KMCOM CGCOG CDCOD CKCOK CRCRI CICIV HRHRV CUCUB CWCUW CYCYP CZCZE DKDNK DJDJI DMDMA DODOM ECECU EGEGY SVSLV GQGNQ ERERI EEEST SZSWZ ETETH FKFLK FOFRO FJFJI FIFIN FRFRA GFGUF PFPYF TFATF GAGAB GMGMB GEGEO DEDEU GHGHA GIGIB GRGRC GLGRL GDGRD GPGLP GUGUM GTGTM GGGGY GNGIN GWGNB GYGUY HTHTI HMHMD VAVAT HNHND HKHKG HUHUN ISISL ININD IDIDN IRIRN IQIRQ IEIRL IMIMN ILISR ITITA JMJAM JPJPN JEJEY JOJOR KZKAZ KEKEN KIKIR KPPRK KRKOR KWKWT KGKGZ LALAO LVLVA LBLBN LSLSO LRLBR LYLBY LILIE LTLTU LULUX MOMAC MGMDG MWMWI MYMYS MVMDV MLMLI MTMLT MHMHL MQMTQ MRMRT MUMUS YTMYT MXMEX FMFSM MDMDA MCMCO MNMNG MEMNE MSMSR MAMAR MZMOZ MMMMR NANAM NRNRU NPNPL NLNLD NCNCL NZNZL NINIC NENER NGNGA NUNIU NFNFK MKMKD MPMNP NONOR OMOMN PKPAK PWPLW PSPSE PAPAN PGPNG PYPRY PEPER PHPHL PNPCN PLPOL PTPRT PRPRI QAQAT REREU ROROU RURUS RWRWA BLBLM SHSHN KNKNA LCLCA MFMAF PMSPM VCVCT WSWSM SMSMR STSTP SASAU SNSEN RSSRB SCSYC SLSLE SGSGP SXSXM SKSVK SISVN SBSLB SOSOM ZAZAF GSSGS SSSSD ESESP LKLKA SDSDN SRSUR SJSJM SESWE CHCHE SYSYR TWTWN TJTJK TZTZA THTHA TLTLS TGTGO TKTKL TOTON TTTTO TNTUN TRTUR TMTKM TCTCA TVTUV UGUGA UAUKR AEARE GBGBR USUSA UMUMI UYURY UZUZB VUVUT VEVEN VNVNM VGVGB VIVIR WFWLF EHESH YEYEM ZMZMB ZWZWE").split(" ").forEach(function (s) { A3[s.slice(0, 2)] = s.slice(2); });

  function font(x, size, bold) { x.font = (bold ? "700 " : "") + size + "px " + SERIF; }
  function txt(x, s, px, py, size, opt) {
    opt = opt || {}; font(x, size, opt.bold);
    if (opt.max) { var w = x.measureText(s).width; if (w > opt.max) { size = size * opt.max / w; font(x, size, opt.bold); } }
    x.fillStyle = "#111"; x.textAlign = opt.align || "left"; x.textBaseline = "alphabetic"; x.fillText(s, px, py);
    if (opt.under) { var u = x.measureText(s).width, x0 = opt.align === "center" ? px - u / 2 : px; x.fillRect(x0, py + 3, u, 1.2); }
  }
  /* words for Latin text, single characters for CJK; Latin runs and numbers inside CJK text stay together */
  function tokens(s) { return s.match(/[A-Za-z0-9][A-Za-z0-9.,'’“”()\-\/]*\s?|\s|[^\sA-Za-z0-9]/g) || []; }
  function isCjk(s) { return /[㐀-鿿]/.test(s); }
  var NOSTART = /^[，。、；：）」』？！.,;:)]/;
  function breakLines(x, s, maxw) {
    var t = isCjk(s) ? tokens(s) : (s.match(/\S+\s*/g) || []), out = [], line = "";
    t.forEach(function (w) {
      if (line && x.measureText((line + w).replace(/\s+$/, "")).width > maxw && !NOSTART.test(w)) { out.push(line.replace(/\s+$/, "")); line = w.replace(/^\s+/, ""); } else line += w;
    });
    if (line.trim()) out.push(line.replace(/\s+$/, ""));
    return out;
  }
  function justify(x, s, px, py, maxw) {
    var t = isCjk(s) ? tokens(s) : (s.match(/\S+\s*/g) || []), w = x.measureText(s).width, gap = t.length > 1 ? (maxw - w) / (t.length - 1) : 0;
    if (gap < 0 || gap > 14) { x.fillText(s, px, py); return; }
    var p = px; t.forEach(function (k) { x.fillText(k, p, py); p += x.measureText(k).width + gap; });
  }
  /* draws (or, with draw = false, measures) wrapped text and returns the next baseline */
  function para(x, s, px, y, size, maxw, lh, draw, just) {
    font(x, size); x.fillStyle = "#111"; x.textAlign = "left"; x.textBaseline = "alphabetic";
    var ls = breakLines(x, s, maxw);
    ls.forEach(function (l, i) { if (draw) { if (just && i < ls.length - 1) justify(x, l, px, y, maxw); else x.fillText(l, px, y); } y += lh; });
    return y;
  }
  function line(x, x1, y1, x2, y2, w, dot) { x.beginPath(); x.lineWidth = w; x.strokeStyle = "#111"; x.setLineDash(dot ? [2, 2.5] : []); x.moveTo(x1, y1); x.lineTo(x2, y2); x.stroke(); x.setLineDash([]); }
  function qr(x, data, px, py, size) {
    var q; try { q = window.qrcode(8, "M"); q.addData(data, "Byte"); q.make(); } catch (e) { q = window.qrcode(0, "M"); q.addData(data, "Byte"); q.make(); }
    var n = q.getModuleCount(), c = Math.max(1, Math.round(size * SCALE / n)) / SCALE, o = (size - c * n) / 2;
    x.fillStyle = "#fff"; x.fillRect(px + o - c * 2, py + o - c * 2, c * (n + 4), c * (n + 4));
    x.fillStyle = "#000";
    for (var r = 0; r < n; r++) for (var k = 0; k < n; k++) if (q.isDark(r, k)) x.fillRect(px + o + k * c, py + o + r * c, c, c);
  }

  /* ------------------------------------------------------------------ watermark: emblem of the Immigration Department */
  function emblem(x) {
    var cx = W / 2, cy = 735, G = "#dcdddd", k, i;
    x.save(); x.fillStyle = G;
    x.beginPath(); x.arc(cx, cy + 20, 262, 0, 7); x.globalAlpha = .28; x.fill(); x.globalAlpha = 1;
    // mountain pass and the Hwarang gate in the disc
    x.save(); x.beginPath(); x.arc(cx, cy + 20, 262, 0, 7); x.clip(); x.strokeStyle = G; x.lineWidth = 2.5;
    [[-300, 120, -120, -70, 10, 120], [-60, 120, 110, -40, 300, 120]].forEach(function (m) { x.beginPath(); x.moveTo(cx + m[0], cy + m[1]); x.lineTo(cx + m[2], cy + m[3]); x.lineTo(cx + m[4], cy + m[5]); x.stroke(); });
    for (k = 0; k < 3; k++) { x.beginPath(); x.moveTo(cx - 280, cy + 135 + k * 22); x.bezierCurveTo(cx - 120, cy + 110 + k * 22, cx + 120, cy + 165 + k * 22, cx + 280, cy + 135 + k * 22); x.stroke(); }
    x.strokeRect(cx - 62, cy + 62, 14, 62); x.strokeRect(cx + 48, cy + 62, 14, 62); x.beginPath(); x.moveTo(cx - 92, cy + 62); x.quadraticCurveTo(cx, cy + 26, cx + 92, cy + 62); x.closePath(); x.stroke();
    x.restore();
    // wreath
    function leaf(px, py, a, len, wd) { x.save(); x.translate(px, py); x.rotate(a); x.beginPath(); x.moveTo(0, 0); x.quadraticCurveTo(len * .45, -wd, len, 0); x.quadraticCurveTo(len * .45, wd, 0, 0); x.fill(); x.restore(); }
    x.fillStyle = G;
    for (i = -1; i <= 1; i += 2) for (k = 0; k < 9; k++) {
      var th = Math.PI / 2 - i * (.32 + k * .235), px = cx + Math.cos(th) * 300, py = cy + 20 + Math.sin(th) * 300, dir = th - i * Math.PI / 2;
      leaf(px, py, dir - i * .42, 118, 24); leaf(px, py, dir + i * .30, 112, 22);
    }
    // flower of the regional flag
    var fx = cx, fy = cy - 265;
    for (k = 0; k < 5; k++) {
      x.save(); x.translate(fx, fy); x.rotate(k * Math.PI * 2 / 5); x.fillStyle = G;
      x.beginPath(); x.moveTo(0, -18); x.bezierCurveTo(-70, -60, -62, -150, 18, -158); x.bezierCurveTo(4, -120, 62, -110, 40, -52); x.bezierCurveTo(30, -30, 14, -22, 0, -18); x.fill();
      x.fillStyle = "#fff"; x.translate(-8, -98); x.beginPath(); for (i = 0; i < 10; i++) { var rr = i % 2 ? 6 : 15, aa = -Math.PI / 2 + i * Math.PI / 5; x[i ? "lineTo" : "moveTo"](Math.cos(aa) * rr, Math.sin(aa) * rr); } x.fill(); x.restore();
    }
    x.fillStyle = "#fff"; x.beginPath(); x.arc(fx, fy, 27, 0, 7); x.fill();
    x.fillStyle = G; x.beginPath(); x.arc(fx, fy, 21, 0, 7); x.fill(); x.fillStyle = "#fff"; x.beginPath(); x.arc(fx, fy, 21, 0, Math.PI); x.arc(fx - 10.5, fy, 10.5, Math.PI, 0, false); x.arc(fx + 10.5, fy, 10.5, Math.PI, 0, true); x.fill();
    // ribbons
    var y0 = cy + 330; x.fillStyle = G;
    for (i = -1; i <= 1; i += 2) { x.beginPath(); x.moveTo(cx + i * 125, y0 + 2); x.quadraticCurveTo(cx + i * 235, y0 - 18, cx + i * 320, y0 - 128); x.lineTo(cx + i * 352, y0 - 50); x.lineTo(cx + i * 345, y0 - 32); x.quadraticCurveTo(cx + i * 250, y0 + 55, cx + i * 125, y0 + 84); x.closePath(); x.fill(); }
    x.beginPath(); x.moveTo(cx - 150, y0 - 8); x.quadraticCurveTo(cx, y0 + 18, cx + 150, y0 - 8); x.lineTo(cx + 140, y0 + 84); x.quadraticCurveTo(cx, y0 + 112, cx - 140, y0 + 84); x.closePath(); x.fill(); x.lineWidth = 5; x.strokeStyle = "#fff"; x.stroke();
    x.fillStyle = "#fff"; x.textAlign = "center"; x.textBaseline = "middle";
    font(x, 37, true); x.fillText("柏峴화랑入境處", cx, y0 + 51, 262);
    function rib(s, i, a, dx, dy, mw) { x.save(); x.translate(cx + i * dx, y0 + dy); x.rotate(a); font(x, 25, true); x.fillText(s, 0, 0, mw); x.restore(); }
    rib("BAEKHYEON HWARANG", -1, .58, 243, 5, 205); rib("IMMIGRATION", 1, -.58, 243, 5, 190);
    x.restore();
  }

  /* ------------------------------------------------------------------ wording by category */
  function kindOf(rec, person) {
    if (person.dep) return "dep";
    if (rec.k) return rec.k;
    return { STUDY: "study", "FOREIGN DOMESTIC HELPER": "fdh", EMPLOYMENT: "gep", "IMPORTED LABOUR": "esls", DEPENDANT: "dep", VISIT: "visit", VISITOR: "fdhvisitor", TRAINING: "train", "WORKING HOLIDAY": "whs", INVESTMENT: "inv",
      "MAINLAND FISHERMAN DECKHAND": "mfd", "TECHNICAL PROFESSIONALS STREAM": "tps" }[rec.slip && rec.slip[1]] || "talent";
  }
  var GROUP = { gep: "emp", asmtp: "emp", tps: "emp", techtas: "emp", vpas: "emp", fdh: "fdh", fdhrenew: "fdh", fdhchange: "fdh", fdhcomplete: "fdh", fdhvisitor: "vis", visit: "vis", pri: "vis", prt: "vis", twn: "vis", tp: "vis",
    icw: "imp", slis: "imp", esls: "imp", inv: "inv", train: "trn", whs: "whs", mfd: "mfd", study: "stu", dep: "dep" };
  var STATUS = { emp: ["僱傭工作", "EMPLOYMENT"], fdh: ["僱傭工作", "EMPLOYMENT"], imp: ["僱傭工作", "EMPLOYMENT"], mfd: ["僱傭工作", "EMPLOYMENT"], stu: ["學生", "STUDENT"], dep: ["受養人", "DEPENDANT"], vis: ["訪客", "VISITOR"],
    inv: ["投資", "INVESTMENT"], trn: ["培訓", "TRAINING"], whs: ["工作假期", "WORKING HOLIDAY"] };
  var TITLES = { entry: ["入境簽證 / 進入許可通知書", "Notification Slip for Entry Visa / Permit"], ext: ["逗留條件通知書", "Notification Slip for Conditions of Stay"],
    fdh2: ["外籍家庭傭工 – 延期逗留及入境簽證通知書", "Foreign Domestic Helper – Notification Slip for Extension of Stay and Entry Visa"],
    pri: ["印度國民預辦入境登記通知書", "Notification Slip for Pre-arrival Registration for Indian Nationals"], prt: ["台灣居民預辦入境登記通知書", "Notification Slip for Pre-arrival Registration for Taiwan Residents"] };
  function formOf(rec, person) {
    var k = kindOf(rec, person);
    if (rec.mode === "ext") return k === "fdhrenew" || k === "fdhchange" ? "fdh2" : "ext";
    return k === "pri" || k === "prt" ? k : "entry";
  }
  function upper(s) { return String(s || "").toUpperCase(); }
  function employment(rec, g) {   // employer, contract and the condition attached to the employment
    var o = [];
    if (g === "fdh") {
      o.push(["m", "受僱於下列僱主 For employment with"], ["m", upper(rec.emp)], ["gap"]);
      o.push(["m", rec.cno ? "根據家庭傭工僱傭合約號碼 " + rec.cno + " 為家庭傭工" : "為家庭傭工"], ["m", rec.cno ? "under D.H. CONTRACT No. " + rec.cno + " as a domestic helper" : "as a domestic helper"]);
      o.push(["m", C_FDH[0]], ["m", C_FDH[1]]);
    } else if (g === "imp") {
      o.push(["m", "替下列僱主工作 For employment with"], ["m", upper(rec.emp)]);
      if (rec.cno) o.push(["m", "根據僱傭合約號碼 in accordance with Employment Contract No. " + rec.cno]);
      o.push(["gap"], ["m", C_IMP[0]], ["m", C_IMP[1]]);
    } else if (g === "mfd") {
      o.push(["m", "替下列僱主工作 For employment with"], ["m", upper(rec.emp)]);
      if (rec.vessel) o.push(["m", "漁船 On fishing vessel " + upper(rec.vessel)]);
      o.push(["gap"], ["m", C_MFD[0]], ["m", C_MFD[1]]);
    }
    return o;
  }
  function entryLines(rec, person) {
    var k = kindOf(rec, person), g = GROUP[k] || "talent", st = STATUS[g], n = rec.days || rec.months, uz = rec.days ? " 日" : " 個月", ue = rec.days ? " days" : " months", mainland = isMainland(rec, person), o = [];
    function cond(c) { o.push(["s", c[0]], ["s", c[1]]); }
    if (g === "stu") {
      o.push(["m", "持證人可在 " + rec.valid + " 或以前首次進入柏峴화랑"], ["m", "並在獲准逗留期限內多次前往柏峴화랑"], ["m", "學生 - 逗留至 " + rec.until], ["m", "於以下院校就讀獲批准課程"]);
      o.push(["m", "Good for first entry to Baekhyeon Hwarang on or before " + rec.valid], ["m", "and Multiple journeys within the permitted limit of stay"], ["m", "STUDENT - to remain until " + rec.until], ["m", "Studying the approved course at"], ["m", upper(rec.emp)], ["gap"]);
      cond(C_STU); if (mainland) cond(EEP); o.push(["m", "************************4W************************"]);
      return o;
    }
    var title = g === "dep" || g === "fdh" || k === "gep" || g === "vis" && k !== "tp" ? null : [rec.zh, rec.en];
    if (title) o.push(["m", title[0]]);
    o.push(["m", "持證人可在 " + rec.valid + " 或以前"], ["m", rec.multi ? "多次進入柏峴화랑" : "前往柏峴화랑一次"]);
    if (!mainland) o.push(["m", "惟須持有有效的旅行證件"]);
    o.push(["m", (st ? st[0] : "逗留") + " " + n + uz]);
    if (title) o.push(["m", title[1]]);
    o.push(["m", "Good for " + (rec.multi ? "Multiple journeys" : "a Single journey") + " to Baekhyeon Hwarang"], ["m", "valid for presentation on or before " + rec.valid]);
    if (!mainland) o.push(["m", "provided travel document is valid."]);
    o.push(["m", (st ? st[1] : "STAY") + " " + n + ue]);
    if (g === "emp") { o.push(["m", "為以下僱主工作"], ["m", "For employment with"], ["m", upper(rec.emp)], ["gap"]); cond(C_EMP); }
    else if (g === "fdh" || g === "imp" || g === "mfd") {
      if (g !== "mfd") o.push(["m", "或解除合約日計兩週內，以較早日期為準"], ["m", "or two weeks after termination of contract, whichever is earlier."]);
      o.push(["gap"]); o = o.concat(employment(rec, g));
    }
    else if (g === "inv") { o.push(["m", "開辦或參與以下業務"], ["m", "To establish or join in the business of"], ["m", upper(rec.emp)], ["gap"]); cond(C_INV); }
    else if (g === "trn") { o.push(["m", "於以下機構受訓"], ["m", "For training with"], ["m", upper(rec.emp)], ["gap"]); cond(C_TRN); }
    else { o.push(["gap"]); if (g === "vis") cond(C_VIS); if (g === "whs") cond(C_WHS); }
    if (mainland) { if (g === "fdh" || g === "imp" || g === "mfd") o.push(["gap"]); cond(EEP); }
    return o;
  }
  function extLines(rec, person) {
    var g = GROUP[kindOf(rec, person)] || "talent", st = STATUS[g], o = [];
    if (g === "stu") {
      return [["m", "學生 - 獲准逗留期限延至 " + rec.until + " 或終止修讀課程日計四週內，以較早日期為準"], ["m", "STUDENT - Permission to remain extended until " + rec.until + " or four weeks after termination of studies, whichever is earlier"],
        ["m", "於以下院校就讀獲批准課程"], ["m", "Studying the approved course at"], ["m", upper(rec.emp)], ["gap"], ["s", C_STU[0]], ["s", C_STU[1]], ["gap"], ["s", LIMIT[0]], ["s", LIMIT[1]]];
    }
    var two = g === "fdh" || g === "imp";
    o.push(["m", (st ? st[0] + "-" : "") + "獲准逗留期限延至" + rec.until + (two ? " 或解除合約日計兩週內，以較早日期為準" : "")]);
    o.push(["m", (st ? st[1] + " - " : "") + "Permission to remain extended until " + rec.until + (two ? " or two weeks after termination of contract, whichever is earlier." : "")]);
    if (two) { o.push(["gap"]); o = o.concat(employment(rec, g)); }
    o.push(["gap"]); if (g === "vis") o.push(["s", C_VIS[0]], ["s", C_VIS[1]], ["gap"]);
    o.push(["s", LIMIT[0]], ["s", LIMIT[1]]);
    return o;
  }
  function isMainland(rec, person) { var k = kindOf(rec, person); return person.td === "other" && person.nat === "KR" || k === "asmtp" || k === "mfd"; }
  function code(rec, person) { return isMainland(rec, person) ? "TWP-T" : person.nat ? (person.nat === "BHG" ? "BHG" : A3[person.nat] || person.nat) + "-" + (person.td === "other" ? "T" : "P") : ""; }

  /* lines at a given zoom; returns the last baseline */
  function lines(x, ls, px, y, maxw, z, draw) {
    ls.forEach(function (l) {
      if (l[0] === "gap") y += 12 * z;
      else if (l[0] === "f") { if (draw) txt(x, l[1], px, y, 20 * z, { max: maxw }); y += 24.6 * z; }   // one line, made to fit
      else if (l[0] === "m") y = para(x, l[1], px, y, 20 * z, maxw, 24.6 * z, draw);
      else y = para(x, l[1], px, y, 18.2 * z, maxw, 20.8 * z, draw);
    });
    return y;
  }
  function fitZoom(x, ls, y, maxw, limit) { var z = 1; while (z > .55 && lines(x, ls, 0, y, maxw, z, false) - 20.8 * z > limit) z -= .02; return z; }
  function money(n) { return "BH$" + (+n || 0).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }

  function page(rec, person, token) {
    var c = document.createElement("canvas"); c.width = W * SCALE; c.height = H * SCALE;
    var x = c.getContext("2d"); x.scale(SCALE, SCALE);
    x.fillStyle = "#fff"; x.fillRect(0, 0, W, H);
    emblem(x);
    var form = formOf(rec, person), t = TITLES[form];
    txt(x, "申請檔案編號 Application Reference No.: " + rec.ref, L + 3, 168, 20.5);
    txt(x, code(rec, person), R - 2, 168, 20.5, { align: "right" });
    txt(x, DEPT_ZH, W / 2, 222, 23, { align: "center" });
    txt(x, "Immigration Department", W / 2, 252, 22, { align: "center" });
    txt(x, GOV_EN, W / 2, 281, 22, { align: "center", max: R - L - 14 });
    txt(x, t[0], W / 2, TOP + 25, 22, { align: "center", max: R - L - 30 });
    txt(x, t[1], W / 2, TOP + 55, 21, { align: "center", max: R - L - 30 });
    // name, date of birth, QR code
    var r1 = TOP + 71, r2 = r1 + 107, r3 = r2 + 111, c1 = L + 254, c2 = R - 202;
    line(x, L, r1, R, r1, 2.6); line(x, L, r2, c2, r2, 1); line(x, c1, r1, c1, r3, 1); line(x, c2, r1, c2, r3, 2.6); line(x, L, r3, R, r3, 3);
    txt(x, "姓名", L + 4, r1 + 47, 20); txt(x, "Name", L + 4, r1 + 73, 19);
    var nw = c2 - c1 - 24;
    if (person.local) { txt(x, person.local, c1 + 15, r1 + 47, 20, { max: nw }); txt(x, person.name, c1 + 15, r1 + 73, 19.5, { max: nw }); }
    else txt(x, person.name, c1 + 15, r1 + 55, 19.5, { max: nw });
    txt(x, "出生日期（日-月-年）", L + 4, r2 + 51, 20, { max: c1 - L - 8 }); txt(x, "Date of birth (day-month-year)", L + 4, r2 + 77, 19, { max: c1 - L - 8 });
    var dob = /^(\d{4})-(\d{2})-(\d{2})$/.exec(person.dob || "");
    txt(x, dob ? dob[3] + "-" + dob[2] + "-" + dob[1] : "", c1 + 15, r2 + 61, 19.5);
    if (token) qr(x, token, c2 + (R - c2 - 142) / 2, r1 + (r3 - r1 - 142) / 2 - 8, 142);
    // important notes: measured first and placed at the bottom, so that nothing can run into them
    var nx = L + 40, nw2 = R - 12 - nx;
    function notes(y, draw) {
      NOTES.forEach(function (n, k) {
        if (draw) { font(x, 18); x.fillStyle = "#111"; x.textAlign = "left"; x.fillText("(" + (k + 1) + ")", L + 5, y); }
        y = para(x, n[0], nx, y, 18.2, nw2, 22.6, draw, true); y = para(x, n[1], nx, y + .5, 17.6, nw2, 20.2, draw, true); if (k < NOTES.length - 1) y += 21;
      });
      return y - 20.2;
    }
    var nh = notes(0, false), nt = BOT - 10 - nh - 46;
    line(x, L, nt, R, nt, 3);
    txt(x, "重要事項", L + 6, nt + 20, 18, { bold: true }); txt(x, "Important notes", L + 87, nt + 20, 17, { bold: true });
    notes(nt + 46, true);
    // particulars
    var y0 = r3 + 28, limit = nt - 12, z;
    if (form === "fdh2") {
      var mid = (L + R) / 2 - 10, hy = r3 + 25, by = r3 + 60, hw = mid - L - 14, hw2 = R - mid - 14;
      var le = [["f", "僱傭工作 - 獲准逗留期限由 " + rec.from + " 起至 " + rec.until], ["f", "或解除合約日計兩週內，以較早日期為準"], ["m", "EMPLOYMENT - Permission to remain from " + rec.from + " to " + rec.until + " or two weeks after termination of contract, whichever is earlier."]];
      var ri = [["m", "持證人可在 " + rec.until + " 或以前"], ["m", "前往柏峴화랑一次"], ["m", "惟須持有有效的旅行證件"], ["m", "繼續其僱傭工作至 " + rec.reuntil], ["m", "Good for a Single journey to Baekhyeon Hwarang"], ["m", "valid for presentation on or before " + rec.until], ["m", "provided travel document is valid."], ["m", "RE-ENTRY EMPLOYMENT till " + rec.reuntil]];
      var bo = employment(rec, "fdh"), my = nt - 238;
      txt(x, "延期逗留 Extension of Stay", (L + mid) / 2, hy, 19, { align: "center", bold: true, under: true }); txt(x, "入境簽證 Entry Visa", (mid + R) / 2, hy, 19, { align: "center", bold: true, under: true });
      line(x, L, hy + 14, R, hy + 14, 1.2, true); line(x, mid, r3, mid, my, 1.2, true); line(x, L, my, R, my, 1.2, true);
      z = Math.min(fitZoom(x, le, by, hw, my - 10), fitZoom(x, ri, by, hw2, my - 10));
      lines(x, le, L + 8, by, hw, z, true); lines(x, ri, mid + 7, by, hw2, z, true);
      z = fitZoom(x, bo, my + 26, R - L - 20, limit); lines(x, bo, L + 8, my + 26, R - L - 20, z, true);
    } else {
      var ls = rec.mode === "ext" ? extLines(rec, person) : entryLines(rec, person), mw = R - L - 24;
      z = fitZoom(x, ls, y0, mw, limit); lines(x, ls, L + 14, y0, mw, z, true);
    }
    x.strokeStyle = "#111"; x.lineWidth = 2.6; x.strokeRect(L, TOP, R - L, BOT - TOP);
    // fee
    var fy = BOT + 40, paid = +rec.fee > 0;
    txt(x, "(11/2026)", L + 5, fy, 12);
    if (form === "fdh2") {
      [["延期逗留", paid ? "經已繳費" : "免收費用", "Extension of Stay", paid ? "Fee Paid" : "No Fee", paid ? money(rec.fee) : ""], ["入境簽證", "免收費用", "Entry Visa", "No Fee", ""]].forEach(function (f, i) {
        [317, 440, 568, 740, 859].forEach(function (px, j) { txt(x, f[j], px, fy + i * 25, 19); });
      });
    } else { txt(x, paid ? "經已繳費" : "免收費用", 458, fy, 19); txt(x, paid ? "Fee Paid " + money(rec.fee) : "No Fee", 700, fy, 19); }
    txt(x, rec.issued, R - 2, fy, 19, { align: "right" });
    return c;
  }

  function tokenOf(rec, person, records) {
    var r = records || (window.IAS && window.IAS.records);
    if (!r || !r.evisaToken) return Promise.reject(new Error("evisa_token"));
    return r.evisaToken(rec.ref, person.dob).then(function (v) { if (!v || !v.token) throw new Error("evisa_token"); return v.token; });
  }
  window.BHGEVisaForm = formOf;
  window.BHGEVisaToken = tokenOf;
  /* recs: a record or a list (applicant and accompanying dependants). Rejects when the QR code cannot be signed. */
  window.BHGEVisaPDF = function (recs, onlyDob, records) {
    if (!recs) return Promise.resolve(null);
    recs = Array.isArray(recs) ? recs : [recs];
    var list = [];
    recs.forEach(function (rec) { rec.people.forEach(function (p) { if (!onlyDob || p.dob === onlyDob) list.push([rec, p]); }); });
    return Promise.all(list.map(function (x) { return tokenOf(x[0], x[1], records).then(function (t) { return { canvas: page(x[0], x[1], t), w: 210, h: 297 }; }); })).then(function (pages) {
      var blob = window.BHGMakePDF(pages), a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = "e-Visa-" + recs[0].ref.replace(/[()]/g, "") + ".pdf";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 60000);
      return blob.size;
    });
  };
})();
