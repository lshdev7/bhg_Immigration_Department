/* GovBHG e-services (client-side). Appointment bookings are kept in localStorage for the change / cancel / enquire tab. */
(function () {
  "use strict";
  var root = document.getElementById("svc");
  if (!root) return;
  var C = JSON.parse(document.getElementById("svc-cfg").textContent);
  var L = C.L;

  /* ------------------------------------------------------------------ helpers */
  function el(tag, props, kids) {
    var e = document.createElement(tag), k;
    props = props || {};
    for (k in props) {
      if (k === "text") e.textContent = props[k];
      else if (k === "html") e.innerHTML = props[k];   // trusted strings from our own build only
      else if (k === "cls") e.className = props[k];
      else if (k === "on") { for (var ev in props.on) e.addEventListener(ev, props.on[ev]); }
      else if (props[k] !== undefined && props[k] !== null && props[k] !== false) e.setAttribute(k, props[k] === true ? "" : props[k]);
    }
    (kids || []).forEach(function (c) { if (c) e.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return e;
  }
  function clear(n) { while (n.firstChild) n.removeChild(n.firstChild); }
  function z(n) { return (n < 10 ? "0" : "") + n; }
  function hash(s) { var h = 5381, i; for (i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) >>> 0; return h; }
  function rnd(n) { var s = ""; for (var i = 0; i < n; i++) s += Math.floor(Math.random() * 10); return s; }
  function today() { return new Date(); }
  function ymd(d) { return d.getFullYear() + "-" + z(d.getMonth() + 1) + "-" + z(d.getDate()); }
  function fmtNow() { var d = today(); return ymd(d) + " " + z(d.getHours()) + ":" + z(d.getMinutes()); }
  function money(n) { return C.cur + String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }

  var HOLIDAYS = ["01-01", "03-01", "05-01", "05-05", "06-06", "07-01", "08-15", "10-01", "10-03", "10-09", "12-25"];
  function isHoliday(d) { return HOLIDAYS.indexOf(z(d.getMonth() + 1) + "-" + z(d.getDate())) >= 0; }
  function workingDays(n) {
    var out = [], d = today();
    d.setHours(0, 0, 0, 0);
    while (out.length < n) {
      d.setDate(d.getDate() + 1);
      if (d.getDay() !== 0 && !isHoliday(d)) out.push(new Date(d.getTime()));
    }
    return out;
  }

  /* ------------------------------------------------------------------ validation */
  function luhn(num) {
    var s = 0, alt = false, i, d;
    for (i = num.length - 1; i >= 0; i--) { d = +num.charAt(i); if (alt) { d *= 2; if (d > 9) d -= 9; } s += d; alt = !alt; }
    return s % 10 === 0;
  }
  /* HKID-style number: 1-2 letters, 6 digits, check character 0-9 or A (brackets optional).
     Any number in this format is accepted; the check character is not recalculated. */
  var ID_RE = /^([A-Z]{1,2})(\d{6})\(?([0-9A])\)?$/;
  function bhidOK(v) { return ID_RE.test(String(v).toUpperCase().replace(/\s/g, "")); }
  function normId(v) { var m = ID_RE.exec(String(v).toUpperCase().replace(/\s/g, "")); return m ? m[1] + m[2] + "(" + m[3] + ")" : v; }
  /* Place of birth: country / territory list (ISO 3166-1), names localised by the browser */
  var ISO = "AF AX AL DZ AS AD AO AI AQ AG AR AM AW AU AT AZ BS BH BD BB BY BE BZ BJ BM BT BO BQ BA BW BV BR IO BN BG BF BI CV KH CM CA KY CF TD CL CN CX CC CO KM CG CD CK CR CI HR CU CW CY CZ DK DJ DM DO EC EG SV GQ ER EE SZ ET FK FO FJ FI FR GF PF TF GA GM GE DE GH GI GR GL GD GP GU GT GG GN GW GY HT HM VA HN HK HU IS IN ID IR IQ IE IM IL IT JM JP JE JO KZ KE KI KP KR KW KG LA LV LB LS LR LY LI LT LU MO MG MW MY MV ML MT MH MQ MR MU YT MX FM MD MC MN ME MS MA MZ MM NA NR NP NL NC NZ NI NE NG NU NF MK MP NO OM PK PW PS PA PG PY PE PH PN PL PT PR QA RE RO RU RW BL SH KN LC MF PM VC WS SM ST SA SN RS SC SL SG SX SK SI SB SO ZA GS SS ES LK SD SR SJ SE CH SY TW TJ TZ TH TL TG TK TO TT TN TR TM TC TV UG UA AE GB US UM UY UZ VU VE VN VG VI WF EH YE ZM ZW".split(" ");
  function countryOptions() {
    var lang = document.documentElement.lang || "en", dn = null;
    try { dn = new Intl.DisplayNames([lang], { type: "region" }); } catch (e) { dn = null; }
    var list = ISO.map(function (c) { var n = c; try { n = dn ? dn.of(c) : c; } catch (e) { n = c; } return [c, n]; });
    list.sort(function (a, b) { return a[1].localeCompare(b[1], lang); });
    var kr = list.filter(function (o) { return o[0] === "KR"; });
    return [["BHG", L.bhPlace]].concat(kr, list.filter(function (o) { return o[0] !== "KR"; }));
  }
  var EVREF = /^[A-Z]{4}-\d{7}-\d{2}\(\d\)$/;
  function evStore(v) { try { return v === undefined ? JSON.parse(localStorage.getItem("bhg-evisa") || "{}") : localStorage.setItem("bhg-evisa", JSON.stringify(v)); } catch (e) { return v === undefined ? {} : null; } }
  /* Dates are typed and shown as YYYYMMDD (8 digits, no hyphens); S.vals keeps YYYY-MM-DD. */
  var DATE_V = { date: 1, fdate: 1, anydate: 1, age11: 1 };
  function isDate(f) { return f.t === "date" || !!DATE_V[f.v]; }
  function dateShow(v) { return /^\d{4}-\d{2}-\d{2}$/.test(v || "") ? v.replace(/-/g, "") : (v || ""); }
  function dateKeep(d) { return /^\d{8}$/.test(d) ? d.slice(0, 4) + "-" + d.slice(4, 6) + "-" + d.slice(6) : d; }
  function validDate(v) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v);
    if (!m) return false;
    var d = new Date(+m[1], +m[2] - 1, +m[3]);
    return d.getFullYear() === +m[1] && d.getMonth() === +m[2] - 1 && d.getDate() === +m[3] && d <= today() && +m[1] >= 1900;
  }
  function checkField(f, v, vals) {
    var s = (v === undefined || v === null) ? "" : String(v).trim();
    if (f.t === "checkbox" && f.req) return v ? "" : L.errAgree;
    if (f.req && !s) return L.errReq;
    if (!s) return "";
    switch (f.v) {
      case "email": if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s)) return L.errEmail; break;
      case "tel": if (!/^[0-9+\-\s]{8,15}$/.test(s)) return L.errTel; break;
      case "bhid": if (!bhidOK(s)) return L.errId; break;
      case "date": if (!validDate(s)) return L.errDate; break;
      case "fdate": { var fm = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s), fd = fm && new Date(+fm[1], +fm[2] - 1, +fm[3]);
        if (!fd || fd.getMonth() !== +fm[2] - 1 || fd <= today()) return L.errFdate; break; }
      case "anydate": { var am = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s), ad = am && new Date(+am[1], +am[2] - 1, +am[3]);
        if (!ad || ad.getMonth() !== +am[2] - 1 || +am[1] < 1900) return L.errAnyDate; break; }
      case "evref": if (!EVREF.test(s.toUpperCase().replace(/\s/g, ""))) return L.errEvref; break;
      case "enname": if (!/^[A-Za-z][A-Za-z '\-]*$/.test(s)) return L.errName; break;
      case "digits4": if (!/^\d{4}$/.test(s)) return L.errCode; break;
      case "pw": if (!/^(?=.*[A-Za-z])(?=.*\d).{8,}$/.test(s)) return L.errPw; break;
      case "match": if (s !== (vals[f.of] || "")) return L.errMatch; break;
      case "cardnum": { var d = s.replace(/[\s-]/g, ""); if (!/^\d{13,19}$/.test(d) || !luhn(d)) return L.errCard; break; }
      case "exp": {
        var m = /^(\d{2})\s*\/\s*(\d{2})$/.exec(s);
        if (!m || +m[1] < 1 || +m[1] > 12) return L.errExp;
        var now = today(), y = 2000 + +m[2];
        if (y < now.getFullYear() || (y === now.getFullYear() && +m[1] < now.getMonth() + 1)) return L.errExp;
        break;
      }
      case "cvv": if (!/^\d{3,4}$/.test(s)) return L.errCvv; break;
      case "num": if (!/^\d+(\.\d+)?$/.test(s)) return L.errNum; break;
      case "mmyy": { var mm = /^(\d{2})-(\d{2})$/.exec(s); if (!mm || +mm[1] < 1 || +mm[1] > 12) return L.errMMYY; break; }
      case "age11": {
        if (!validDate(s)) return L.errAge11;
        var b = new Date(s + "T00:00:00"), n = today(), a = n.getFullYear() - b.getFullYear();
        if (n.getMonth() < b.getMonth() || (n.getMonth() === b.getMonth() && n.getDate() < b.getDate())) a--;
        if (a < 11) return L.errAge11; break;
      }
      case "ref": if (!/^[A-Za-z0-9\-]{6,20}$/.test(s)) return L.errRef; break;
    }
    return "";
  }

  /* ------------------------------------------------------------------ field rendering */
  function showIf(cond, vals) {
    if (!cond) return true;
    var v = vals[cond.n];
    if (cond.eq !== undefined) return v === cond.eq;
    if (cond.ne !== undefined) return v !== cond.ne;
    if (cond.in) return cond.in.indexOf(v) >= 0;
    if (cond.nin) return cond.nin.indexOf(v) < 0;
    if (cond.pos) return !!v && v !== "0";
    return true;
  }
  function optLabel(f, v) {
    var r = v;
    (f.o || []).forEach(function (o) { if (o[0] === v) r = o[1]; });
    return r;
  }

  /* Photo cropper: move / zoom / rotate the picture inside a 40:50 frame and export 1280 x 1600 JPEG. */
  var OUT_W = 1280, OUT_H = 1600, VW = 300, VH = 375;
  function openCropper(file, host, onDone, onCancel) {
    var url = URL.createObjectURL(file), img = new Image();
    img.onerror = function () { URL.revokeObjectURL(url); onCancel(L.errPhotoType); };
    img.onload = function () {
      URL.revokeObjectURL(url);
      var src = img, zoom = 1, sc, ox, oy;
      var box = el("div", { cls: "crop" });
      var cv = el("canvas", { width: VW, height: VH, cls: "crop-cv", "aria-label": L.cropTitle });
      var zr = el("input", { type: "range", min: "1", max: "4", step: "0.01", value: "1", "aria-label": L.zoom });
      var err = el("div", { cls: "err", role: "alert" });
      var ctx = cv.getContext("2d");
      function base() { return Math.max(VW / src.width, VH / src.height); }
      function clamp() {
        ox = Math.min(0, Math.max(VW - src.width * sc, ox));
        oy = Math.min(0, Math.max(VH - src.height * sc, oy));
      }
      function reset() { sc = base() * zoom; ox = (VW - src.width * sc) / 2; oy = (VH - src.height * sc) / 2; clamp(); draw(); }
      function setZoom(z) {
        var cx = (VW / 2 - ox) / sc, cy = (VH / 2 - oy) / sc;
        zoom = Math.min(4, Math.max(1, z)); zr.value = String(zoom);
        sc = base() * zoom; ox = VW / 2 - cx * sc; oy = VH / 2 - cy * sc; clamp(); draw();
      }
      function draw() {
        ctx.fillStyle = "#fff"; ctx.fillRect(0, 0, VW, VH);
        ctx.drawImage(src, ox, oy, src.width * sc, src.height * sc);
        // face guide: crown-to-chin 32-36 mm of the 50 mm photo height
        ctx.save(); ctx.strokeStyle = "rgba(0,120,140,.9)"; ctx.setLineDash([6, 5]); ctx.lineWidth = 2;
        ctx.beginPath(); ctx.ellipse(VW / 2, VH * .46, VW * .27, VH * .34, 0, 0, 7); ctx.stroke();
        ctx.setLineDash([2, 4]); ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(VW / 2, 0); ctx.lineTo(VW / 2, VH); ctx.stroke(); ctx.restore();
      }
      var drag = null;
      cv.addEventListener("pointerdown", function (e) { drag = { x: e.clientX, y: e.clientY, ox: ox, oy: oy }; cv.setPointerCapture(e.pointerId); });
      cv.addEventListener("pointermove", function (e) { if (!drag) return; ox = drag.ox + e.clientX - drag.x; oy = drag.oy + e.clientY - drag.y; clamp(); draw(); });
      cv.addEventListener("pointerup", function () { drag = null; });
      cv.addEventListener("wheel", function (e) { e.preventDefault(); setZoom(zoom * (e.deltaY < 0 ? 1.08 : 1 / 1.08)); }, { passive: false });
      zr.addEventListener("input", function () { setZoom(parseFloat(zr.value)); });
      var rot = el("button", { type: "button", cls: "btn sec", text: L.rotate });
      rot.addEventListener("click", function () {
        var c = document.createElement("canvas"); c.width = src.height; c.height = src.width;
        var x = c.getContext("2d"); x.translate(c.width, 0); x.rotate(Math.PI / 2); x.drawImage(src, 0, 0);
        src = c; zoom = 1; zr.value = "1"; reset();
      });
      var ok = el("button", { type: "button", cls: "btn", text: L.cropApply });
      ok.addEventListener("click", function () {
        var out = document.createElement("canvas"); out.width = OUT_W; out.height = OUT_H;
        var x = out.getContext("2d"), k = OUT_W / VW;
        x.fillStyle = "#fff"; x.fillRect(0, 0, OUT_W, OUT_H);
        x.drawImage(src, ox * k, oy * k, src.width * sc * k, src.height * sc * k);
        out.toBlob(function (b) {
          if (!b) { err.textContent = L.errPhotoType; return; }
          if (b.size > 5 * 1024 * 1024) { err.textContent = L.errPhotoSize; return; }
          box.remove();
          onDone(new File([b], "photo.jpg", { type: "image/jpeg" }));
        }, "image/jpeg", 0.92);
      });
      var no = el("button", { type: "button", cls: "btn sec", text: L.cropCancel });
      no.addEventListener("click", function () { box.remove(); onCancel(""); });
      box.appendChild(el("p", { cls: "crop-t", text: L.cropTitle }));
      box.appendChild(el("p", { cls: "hint", text: L.cropHint }));
      box.appendChild(cv);
      box.appendChild(el("label", { cls: "crop-z" }, [el("span", { text: L.zoom }), zr]));
      box.appendChild(err);
      box.appendChild(el("div", { cls: "nav" }, [rot, no, ok]));
      host.appendChild(box);
      reset();
    };
    img.src = url;
  }

  function buildField(f, S, onChange) {
    var wrap = el("div", { cls: "fld" + (f.full ? " full" : ""), "data-n": f.n });
    var id = "f_" + f.n, ctl, v = S.vals[f.n];
    if (f.t === "checkbox") {
      ctl = el("input", { type: "checkbox", id: id });
      ctl.checked = !!v;
      ctl.addEventListener("change", function () { S.vals[f.n] = ctl.checked; onChange(f); });
      wrap.appendChild(el("label", { cls: "chk", "for": id }, [ctl, el("span", { html: f.l })]));
    } else if (f.t === "radio") {
      wrap.appendChild(el("div", { cls: "lbl", html: f.l + (f.req ? ' <b class="req">*</b>' : "") }));
      var grp = el("div", { cls: "radios" });
      f.o.forEach(function (o, k) {
        var r = el("input", { type: "radio", name: id, id: id + k, value: o[0] });
        r.checked = v === o[0];
        r.addEventListener("change", function () { S.vals[f.n] = o[0]; onChange(f); });
        grp.appendChild(el("label", { cls: "rad", "for": id + k }, [r, el("span", { text: o[1] })]));
      });
      wrap.appendChild(grp);
    } else if (f.t === "info") {
      wrap.appendChild(el("div", { cls: "infotxt", html: f.l }));
    } else {
      wrap.appendChild(el("label", { cls: "lbl", "for": id, html: f.l + (f.req ? ' <b class="req">*</b>' : "") }));
      if (f.t === "country") f.o = countryOptions();
      if (f.t === "select" || f.t === "country") {
        ctl = el("select", { id: id }, [el("option", { value: "", text: L.choose })].concat(f.o.map(function (o) { return el("option", { value: o[0], text: o[1] }); })));
        ctl.value = v || "";
        ctl.addEventListener("change", function () { S.vals[f.n] = ctl.value; onChange(f); });
      } else if (f.t === "textarea") {
        ctl = el("textarea", { id: id, rows: 3 }); ctl.value = v || "";
        ctl.addEventListener("input", function () { S.vals[f.n] = ctl.value; });
      } else if (f.t === "file" || f.t === "photo") {
        var inp = el("input", { type: "file", id: id, accept: f.t === "photo" ? "image/*" : "image/jpeg,image/gif,image/tiff,application/pdf" });
        var prev = el("div", { cls: "prev" });
        if (S.files[f.n]) prev.textContent = S.files[f.n].name;
        inp.addEventListener("change", function () {
          var file = inp.files && inp.files[0];
          clear(prev); S.files[f.n] = null; S.vals[f.n] = "";
          if (!file) return;
          var orig = file;
          function ok() {
            clear(prev);
            S.files[f.n] = file; S.vals[f.n] = file.name;
            if (f.t === "photo") {
              var u = URL.createObjectURL(file), im = el("img", { src: u, alt: "", cls: "pphoto" });
              im.onload = function () { URL.revokeObjectURL(u); };
              prev.appendChild(im);
              var again = el("button", { type: "button", cls: "btn sec", text: L.cropAgain });
              again.addEventListener("click", function () { crop(); });
              prev.appendChild(again);
            } else prev.appendChild(el("span", { text: file.name }));
            setErr(wrap, "");
          }
          function crop() {
            var old = wrap.querySelector(".crop"); if (old) old.remove();
            openCropper(orig, wrap, function (out) { file = out; ok(); }, function (msg) { if (msg) { inp.value = ""; setErr(wrap, msg); } });
          }
          if (f.t === "photo") {
            if (!/^image\//.test(file.type)) { inp.value = ""; setErr(wrap, L.errPhotoType); return; }
            crop();
          }
          else if (file.size > 2 * 1024 * 1024) { inp.value = ""; setErr(wrap, L.errFileSize); }
          else ok();
        });
        wrap.appendChild(inp); wrap.appendChild(prev);
        ctl = null;
      } else if (f.t === "slot") {
        return buildSlot(f, S, wrap, onChange);
      } else {
        ctl = el("input", { type: f.t === "password" ? "password" : (f.t === "date" ? "text" : (f.t || "text")), id: id, placeholder: f.ph || "", autocomplete: "off", inputmode: f.im || null, maxlength: f.max || null });
        if (isDate(f)) {
          ctl.setAttribute("inputmode", "numeric"); ctl.value = dateShow(v);
          ctl.addEventListener("input", function () {
            var d = ctl.value.replace(/\D/g, "").slice(0, 8);
            if (ctl.value !== d) { var at = ctl.value.slice(0, ctl.selectionStart).replace(/\D/g, "").length; ctl.value = d; ctl.setSelectionRange(at, at); }
            S.vals[f.n] = dateKeep(d);
          });
        } else {
          ctl.value = v || "";
          ctl.addEventListener("input", function () { S.vals[f.n] = ctl.value; });
        }
      }
      if (ctl) wrap.appendChild(ctl);
    }
    if (f.h) wrap.appendChild(el("div", { cls: "hint", html: f.h }));
    wrap.appendChild(el("div", { cls: "err", role: "alert" }));
    return wrap;
  }
  function setErr(wrap, msg) { var e = wrap.querySelector(".err"); if (e) { e.textContent = msg; wrap.classList.toggle("bad", !!msg); } }

  /* ------------------------------------------------------------------ slot picker (office / date / time) */
  function slotsFor(office, date) {
    var out = [], h = 9, m = 0, seed = hash(office + date);
    while (h < 16 || (h === 16 && m <= 15)) {
      var lunch = (h === 12 && m >= 45) || h === 13;
      if (!lunch && (hash(seed + ":" + h + ":" + m) % 5) !== 0) out.push(z(h) + ":" + z(m));
      m += 15; if (m >= 60) { m = 0; h++; }
    }
    return out;
  }
  function buildSlot(f, S, wrap, onChange) {
    var v = S.vals, part = f.part || "all";
    var timeBox = el("div", { cls: "times" });
    function draw() {
      clear(timeBox);
      if (!v.office || !v.date) { timeBox.appendChild(el("p", { cls: "hint", text: L.pickOfficeDate })); return; }
      var sl = slotsFor(v.office, v.date);
      if (!sl.length) { timeBox.appendChild(el("p", { cls: "hint", text: L.noSlots })); return; }
      sl.forEach(function (t) {
        var b = el("button", { type: "button", cls: "slot" + (v.time === t ? " on" : ""), text: t });
        b.addEventListener("click", function () { v.time = t; draw(); setErr(wrap, ""); });
        timeBox.appendChild(b);
      });
    }
    if (part !== "time") {
      var offSel = el("select", { id: "f_office" }, [el("option", { value: "", text: L.choose })].concat(C.offices.map(function (o) { return el("option", { value: o[0], text: o[1] }); })));
      var days = workingDays(24);
      var dateSel = el("select", { id: "f_date" }, [el("option", { value: "", text: L.choose })].concat(days.map(function (d) {
        return el("option", { value: ymd(d), text: ymd(d) + " (" + L.dow[d.getDay()] + ")" });
      })));
      offSel.value = v.office || ""; dateSel.value = v.date || "";
      offSel.addEventListener("change", function () { v.office = offSel.value; v.time = ""; if (part === "all") draw(); });
      dateSel.addEventListener("change", function () { v.date = dateSel.value; v.time = ""; if (part === "all") draw(); });
      wrap.appendChild(el("div", { cls: "lbl", html: L.office + ' <b class="req">*</b>' })); wrap.appendChild(offSel);
      wrap.appendChild(el("div", { cls: "lbl", html: L.date + ' <b class="req">*</b>' })); wrap.appendChild(dateSel);
    } else {
      var off = v.office;
      C.offices.forEach(function (o) { if (o[0] === off) off = o[1]; });
      wrap.appendChild(el("p", { cls: "pickd", text: off + " – " + v.date }));
    }
    if (part !== "od") {
      wrap.appendChild(el("div", { cls: "lbl", html: L.time + ' <b class="req">*</b>' })); wrap.appendChild(timeBox);
      draw();
    }
    wrap.appendChild(el("div", { cls: "err", role: "alert" }));
    return wrap;
  }

  /* ------------------------------------------------------------------ fee calculation */
  function feeOf(vals) {
    if (!C.fee) return { lines: [], total: 0 };
    var lines = [], total = 0;
    (C.fee.base || []).some(function (r) {
      var ok = Object.keys(r.when).every(function (k) { return vals[k] === r.when[k]; });
      if (ok) { lines.push([r.l, r.amt]); total += r.amt; }
      return ok;
    });
    (C.fee.extra || []).forEach(function (r) {
      var ok = Object.keys(r.when).every(function (k) { return vals[k] === r.when[k]; });
      if (ok) { lines.push([r.l, r.amt]); total += r.amt; }
    });
    var mult = C.fee.mult ? 1 + (+vals[C.fee.mult] || 0) : 1;
    if (mult > 1) { lines = lines.map(function (r) { return [r[0] + " × " + mult, r[1] * mult]; }); total *= mult; }
    if (C.fee.amountField && vals[C.fee.amountField]) { total = Math.round(parseFloat(vals[C.fee.amountField]) * 100) / 100; lines = [[C.fee.amountLabel, total]]; }
    return { lines: lines, total: total };
  }

  /* ------------------------------------------------------------------ wizard */
  /* "e-ME" form filling with iAM Smart: form field -> e-ME data */
  var EME_MAP = {
    surname: function (r) { return String(r.name_en || "").split(",")[0].trim(); },
    given: function (r) { return String(String(r.name_en || "").split(",")[1] || "").trim(); },
    local: "name_local", sex: "sex", dob: "dob", idno: "id_no", email: "email", mobile: "mobile", addr: "residential_address", marital: "marital",
    status: "res_status",
    pob: function (r) { return r.pob === "BHG" || r.pob === "KR" ? r.pob : ""; },
    nat: function (r) { return r.nationality === "KOR" ? "KR" : ""; },
    kornat: function (r) { return r.nationality ? (r.nationality === "KOR" ? "KOR" : "OTH") : ""; }
  };
  var EME_KEY = { surname: "name_en", given: "name_en", pob: "pob", nat: "nationality", kornat: "nationality" };
  function emeValue(f, r) { var m = EME_MAP[f.n]; return typeof m === "function" ? m(r) : r[m]; }
  function Wizard(cfg, container) {
    var S = { step: 0, vals: {}, files: {}, done: false };
    var host = el("div", { cls: "wiz" });
    (container || root).appendChild(host);

    function steps() { return cfg.steps.filter(function (s) { return showIf(s.showIf, S.vals); }); }
    function fieldsOf(s) {
      if (s.gen === "applicants") {
        var n = +S.vals.count || 1, out = (s.fields || []).filter(function (f) { return showIf(f.showIf, S.vals); });
        for (var k = 1; k <= n; k++) {
          out.push({ n: "a" + k + "_id", l: L.applicant + " " + k + " – " + L.idno, t: "text", req: true, v: "bhid", ph: "A123456(3)", sens: true });
          out.push({ n: "a" + k + "_dob", l: L.applicant + " " + k + " – " + L.dob, t: "text", req: true, v: "date", ph: "YYYYMMDD", sens: true });
        }
        return out.concat(s.extra || []);
      }
      if (s.gen === "deps") {
        var dn = +S.vals.deps || 0, dl = [];
        for (var j = 1; j <= dn; j++) {
          (cfg.depFields || []).forEach(function (t) {
            var f = JSON.parse(JSON.stringify(t));
            f.n = t.n.replace("{k}", j); f.l = L.dependant + " " + j + " – " + t.l; f.rl = f.l;
            dl.push(f);
          });
        }
        return dl;
      }
      return (s.fields || []).filter(function (f) { return showIf(f.showIf, S.vals); });
    }
    function validateStep(s, wrapRoot) {
      var ok = true;
      fieldsOf(s).forEach(function (f) {
        if (f.t === "info") return;
        var wrap = wrapRoot.querySelector('[data-n="' + f.n + '"]') || wrapRoot.querySelector(".fld");
        var msg = "";
        if (f.t === "slot") {
          if (f.part === "od" ? (!S.vals.office || !S.vals.date) : f.part === "time" ? !S.vals.time : (!S.vals.office || !S.vals.date || !S.vals.time)) msg = L.errSlot;
          wrap = wrapRoot.querySelector('[data-n="' + f.n + '"]');
        } else if (f.t === "file" || f.t === "photo") {
          if (f.req && !S.files[f.n]) msg = L.errReq;
        } else {
          msg = checkField(f, S.vals[f.n], S.vals);
          if (!msg && f.v === "bhid" && S.vals[f.n]) {
            S.vals[f.n] = normId(S.vals[f.n]);
            var idIn = document.getElementById("f_" + f.n); if (idIn) idIn.value = S.vals[f.n];
          }
        }
        if (msg && wrap) { setErr(wrap, msg); ok = false; }
        else if (wrap) setErr(wrap, "");
      });
      if (s.type === "review" && cfg.declare) {
        var dw = wrapRoot.querySelector('[data-n="declare"]');
        if (!S.vals.declare) { setErr(dw, L.errAgree); ok = false; } else setErr(dw, "");
      }
      if (s.type === "pay") ok = validatePay(wrapRoot) && ok;
      return ok;
    }

    function progress(list) {
      var ol = el("ol", { cls: "prog" });
      list.forEach(function (s, i) {
        ol.appendChild(el("li", { cls: i === S.step ? "on" : (i < S.step ? "done" : ""), text: L.stepFmt.replace("{n}", i + 1).replace("{t}", s.title) }));
      });
      return ol;
    }

    function render() {
      clear(host);
      var list = steps();
      if (S.step >= list.length) S.step = list.length - 1;
      var s = list[S.step];
      if (!S.done) host.appendChild(progress(list));
      var box = el("section", { cls: "stepbox" });
      box.appendChild(el("h2", { text: s.title }));
      if (s.intro) box.appendChild(el("div", { cls: "intro", html: s.intro }));
      if (s.type === "review") renderReview(box, list);
      else if (s.type === "pay") renderPay(box);
      else if (s.type === "done") renderDone(box);
      else {
        var grid = el("div", { cls: "grid" });
        var emeF = fieldsOf(s).filter(function (f) { return EME_MAP[f.n]; });
        var sess = window.IASClient && window.IASClient.session();
        if (sess) {   // logged in with iAM Smart: the profile was given at login, so empty fields are filled at once
          emeF.forEach(function (f) { if (S.vals[f.n] === undefined || S.vals[f.n] === "") { var v = emeValue(f, sess); if (v) S.vals[f.n] = v; } });
        }
        if (window.IASClient && emeF.length >= 2) {
          var fb = el("button", { type: "button", cls: "btn sec iasfill", html: window.IASClient.logo + " " + window.IASClient.text("fill") });
          fb.addEventListener("click", function () {
            var now = window.IASClient.session();
            if (now) { emeF.forEach(function (f) { var v = emeValue(f, now); if (v) S.vals[f.n] = v; }); render(); return; }
            var scope = [];
            emeF.forEach(function (f) { var k = EME_KEY[f.n] || EME_MAP[f.n]; if (scope.indexOf(k) < 0) scope.push(k); });
            window.IASClient.request("eme", scope).then(function (r) {
              emeF.forEach(function (f) { var v = emeValue(f, r); if (v) S.vals[f.n] = v; });
              render();
            }, function () { /* cancelled */ });
          });
          box.appendChild(fb);
        }
        fieldsOf(s).forEach(function (f) {
          grid.appendChild(buildField(f, S, function () { refreshVis(s, box); }));
        });
        box.appendChild(grid);
      }
      var nav = el("div", { cls: "nav" });
      if (s.type !== "done") {
        if (S.step > 0) nav.appendChild(el("button", { type: "button", cls: "btn sec", text: L.back, on: { click: function () { S.step--; render(); window.scrollTo(0, root.offsetTop); } } }));
        var last = S.step === list.length - 2 && list[list.length - 1].type === "done";
        nav.appendChild(el("button", { type: "button", cls: "btn", text: last ? (s.type === "pay" ? L.pay : L.submit) : L.next, on: { click: function () { go(s, box, last); } } }));
      } else {
        nav.appendChild(el("button", { type: "button", cls: "btn sec", text: L.print, on: { click: function () { window.print(); } } }));
        nav.appendChild(el("button", { type: "button", cls: "btn", text: L.again, on: { click: function () { S = { step: 0, vals: {}, files: {}, done: false }; render(); } } }));
      }
      box.appendChild(nav);
      host.appendChild(box);
      refreshVis(s, box);
    }
    function refreshVis(s, box) {
      // re-render only when a field's visibility depends on another field (cheap: rebuild the grid)
      var grid = box.querySelector(".grid");
      if (!grid || s.type) return;
      var want = fieldsOf(s).map(function (f) { return f.n; }).join(",");
      if (grid.getAttribute("data-w") === null) { grid.setAttribute("data-w", want); return; }
      if (grid.getAttribute("data-w") !== want) {
        var focus = document.activeElement && document.activeElement.id;
        clear(grid); grid.setAttribute("data-w", want);
        fieldsOf(s).forEach(function (f) { grid.appendChild(buildField(f, S, function () { refreshVis(s, box); })); });
        if (focus) { var n = document.getElementById(focus); if (n) n.focus(); }
      }
    }
    function go(s, box, isLast) {
      if (!validateStep(s, box)) { var b = box.querySelector(".bad"); if (b) b.scrollIntoView({ block: "center" }); return; }
      if (s.type === "pay") { return finish(box); }
      if (isLast) return finish(box);
      S.step++; render(); window.scrollTo(0, root.offsetTop);
    }

    function renderReview(box, list) {
      var dl = el("dl", { cls: "review" });
      list.forEach(function (st) {
        if (st.type) return;
        var rows = [];
        fieldsOf(st).forEach(function (f) {
          if (f.t === "info" || f.sens) return;
          var v = S.vals[f.n];
          if (v === undefined || v === "" || v === false) return;
          if (f.t === "select" || f.t === "radio") v = optLabel(f, v);
          if (f.t === "country") v = optLabel({ o: countryOptions() }, v);
          if (f.t === "checkbox") v = "✓";
          if (isDate(f)) v = dateShow(v);
          rows.push([f.rl || f.l.replace(/<[^>]+>/g, ""), String(v)]);
        });
        if (!rows.length) return;
        dl.appendChild(el("dt", { cls: "grp", text: st.title }));
        rows.forEach(function (r) { dl.appendChild(el("dt", { text: r[0] })); dl.appendChild(el("dd", { text: r[1] })); });
      });
      box.appendChild(dl);
      var f = cfg.declare;
      if (f) {
        var g = el("div", { cls: "grid" });
        g.appendChild(buildField(f, S, function () {}));
        box.appendChild(g);
      }
    }
    function renderPay(box) {
      var fee = feeOf(S.vals);
      S.fee = fee;
      var t = el("table", { cls: "feet" });
      fee.lines.forEach(function (r) { t.appendChild(el("tr", {}, [el("td", { text: r[0] }), el("td", { cls: "amt", text: money(r[1]) })])); });
      t.appendChild(el("tr", { cls: "tot" }, [el("td", { text: L.total }), el("td", { cls: "amt", text: money(fee.total) })]));
      box.appendChild(t);
      box.appendChild(el("p", { cls: "trn", text: L.trn + ": " + (S.trn || (S.trn = "TRN" + rnd(12))) }));
      var methods = cfg.pay.methods;
      var grp = el("div", { cls: "radios" });
      methods.forEach(function (m, k) {
        var r = el("input", { type: "radio", name: "paym", id: "pm" + k, value: m[0] });
        r.checked = S.vals.paym === m[0];
        r.addEventListener("change", function () { S.vals.paym = m[0]; drawPayFields(box); });
        grp.appendChild(el("label", { cls: "rad", "for": "pm" + k }, [r, el("span", { text: m[1] })]));
      });
      box.appendChild(el("div", { cls: "lbl", html: L.payMethod + ' <b class="req">*</b>' }));
      box.appendChild(grp);
      box.appendChild(el("div", { cls: "payfields grid" }));
      box.appendChild(el("div", { cls: "err payerr", role: "alert" }));
      drawPayFields(box);
    }
    function drawPayFields(box) {
      var pf = box.querySelector(".payfields"); clear(pf);
      var m = S.vals.paym, fs = (cfg.pay.fields || {})[m] || [];
      fs.forEach(function (f) { pf.appendChild(buildField(f, S, function () {})); });
      if (m && !fs.length) pf.appendChild(el("p", { cls: "hint", text: L.payRedirect }));
    }
    function validatePay(box) {
      var pe = box.querySelector(".payerr"), ok = true;
      if (!S.vals.paym) { pe.textContent = L.errPay; return false; }
      pe.textContent = "";
      ((cfg.pay.fields || {})[S.vals.paym] || []).forEach(function (f) {
        var wrap = box.querySelector('[data-n="' + f.n + '"]'), msg = checkField(f, S.vals[f.n], S.vals);
        if (msg) { setErr(wrap, msg); ok = false; } else setErr(wrap, "");
      });
      return ok;
    }
    function finish(box) {
      var btn = box.querySelector(".nav .btn:not(.sec)");
      if (btn) { btn.disabled = true; btn.textContent = L.processing; }
      setTimeout(function () {
        var d = today();
        S.ref = cfg.refCode ? cfg.refCode + "-" + rnd(7) + "-" + String(d.getFullYear()).slice(2) + "(" + rnd(1) + ")"
                            : cfg.prefix + d.getFullYear() + z(d.getMonth() + 1) + z(d.getDate()) + rnd(6);
        if (cfg.evisa) saveEVisa(cfg, S);
        S.when = fmtNow();
        // do not keep payment secrets in memory after submission
        ["card", "cardname", "exp", "cvv", "opsno", "opspw", "pw", "pw2", "pass"].forEach(function (k) { delete S.vals[k]; });
        S.done = true;
        if (cfg.onDone) cfg.onDone(S);
        S.step = steps().length - 1;
        render(); window.scrollTo(0, root.offsetTop);
      }, 900);
    }
    function renderDone(box) {
      box.appendChild(el("div", { cls: "ok", html: cfg.doneText }));
      var rows = [[L.refNo, S.ref], [L.when, S.when]];
      if (S.fee && S.fee.total) { rows.push([L.trn, S.trn]); rows.push([L.paid, money(S.fee.total)]); }
      (cfg.doneRows || []).forEach(function (r) {
        var v = S.vals[r.n];
        if (v) rows.push([r.l, r.o ? optLabel({ o: r.o }, v) : v]);
      });
      var dl = el("dl", { cls: "review" });
      rows.forEach(function (r) { dl.appendChild(el("dt", { text: r[0] })); dl.appendChild(el("dd", { text: r[1] })); });
      box.appendChild(dl);
      if (cfg.doneNote) box.appendChild(el("p", { cls: "hint", html: cfg.doneNote }));
      if (cfg.evisa && window.BHGEVisaPDF) {
        var eb = el("button", { type: "button", cls: "btn", text: L.dlEvisa });
        eb.addEventListener("click", function () { window.BHGEVisaPDF(evStore()[S.ref]); });
        box.appendChild(el("p", { cls: "dlp" }, [eb]));
      }
      if (cfg.idcardPdf && window.BHGIdCardPDF && S.files.photo) {
        var ib = el("button", { type: "button", cls: "btn", text: L.dlIdcard });
        ib.addEventListener("click", function () {
          ib.disabled = true; ib.textContent = L.generating;
          window.BHGIdCardPDF(S.vals, S.files.photo).then(function () { ib.disabled = false; ib.textContent = L.dlIdcard; },
            function () { ib.disabled = false; ib.textContent = L.dlIdcard; });
        });
        box.appendChild(el("p", { cls: "dlp" }, [ib]));
      }
      if (cfg.passportPdf && window.BHGPassportPDF && S.files.photo) {
        var pb = el("button", { type: "button", cls: "btn", text: L.dlPassport });
        pb.addEventListener("click", function () {
          pb.disabled = true; pb.textContent = L.generating;
          window.BHGPassportPDF(S.vals, S.files.photo).then(function () { pb.disabled = false; pb.textContent = L.dlPassport; },
            function () { pb.disabled = false; pb.textContent = L.dlPassport; });
        });
        box.appendChild(el("p", { cls: "dlp" }, [pb]));
      }
    }
    render();
  }

  /* ------------------------------------------------------------------ "e-Visa" records (kept in this browser) */
  function addMonths(d, m) { var r = new Date(d.getTime()); r.setMonth(r.getMonth() + m); return r; }
  function dmy(d) { return z(d.getDate()) + "-" + z(d.getMonth() + 1) + "-" + d.getFullYear(); }
  function dobDmy(v) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v || ""); return m ? m[3] + "-" + m[2] + "-" + m[1] : ""; }
  function saveEVisa(cfg, S) {
    var ev = cfg.evisa, v = S.vals, now = today(), people = [];
    function nm(sur, giv) { return (String(sur || "").toUpperCase() + ", " + String(giv || "").toUpperCase()).replace(/\s+/g, " "); }
    people.push({ name: nm(v.surname, v.given), local: v.local || "", dob: v.dob });
    for (var k = 1; k <= (+v.deps || 0); k++) people.push({ name: nm(v["d" + k + "_surname"], v["d" + k + "_given"]), local: "", dob: v["d" + k + "_dob"], dep: true });
    var base = ev.mode === "ext" && v.lse ? new Date(v.lse + "T00:00:00") : now;
    var until = ev.days ? new Date(now.getTime() + ev.days * 864e5) : addMonths(base, ev.months);
    var fee = S.fee && S.fee.total ? S.fee.total / people.length : 0;
    var rec = { ref: S.ref, mode: ev.mode, zh: ev.zh, en: ev.en, slip: ev.slip, months: ev.months, days: ev.days, multi: ev.multi, employ: ev.employ,
                emp: ev.emp ? (v[ev.emp] || "") : "", issued: dmy(now), valid: dmy(addMonths(now, 3)), until: dmy(until), fee: fee, trn: S.trn || "", people: people };
    var all = evStore(); all[S.ref] = rec; evStore(all);
    REC().then(function (r) { if (r) return r.saveEvisa(rec); }).catch(function () { /* kept locally */ });
  }
  function EVisa(cfg) {
    var S = { vals: {}, files: {} };
    var box = el("section", { cls: "stepbox" });
    box.appendChild(el("h2", { text: cfg.title }));
    box.appendChild(el("div", { cls: "intro", text: cfg.intro }));
    var grid = el("div", { cls: "grid" });
    cfg.fields.forEach(function (f) { grid.appendChild(buildField(f, S, function () {})); });
    box.appendChild(grid);
    var out = el("div", { cls: "result" });
    var b = el("button", { type: "button", cls: "btn", text: L.search });
    b.addEventListener("click", function () {
      clear(out);
      var ok = true;
      cfg.fields.forEach(function (f) { var w = box.querySelector('[data-n="' + f.n + '"]'), m = checkField(f, S.vals[f.n], S.vals); setErr(w, m); if (m) ok = false; });
      if (!ok) return;
      var ref = S.vals.ref.toUpperCase().replace(/\s/g, "");
      REC().then(function (r) { return r ? r.getEvisa(ref, S.vals.dob) : null; }).catch(function () { return null; }).then(function (rec) {
      rec = rec || evStore()[ref];
      if (!rec || !rec.people.some(function (p) { return p.dob === S.vals.dob; })) { out.appendChild(el("p", { cls: "errbox", text: L.evNotFound })); return; }
      var person = rec.people.filter(function (p) { return p.dob === S.vals.dob; })[0];
      if (cfg.mode === "enquiry") {
        var dl = el("dl", { cls: "review" });
        [[L.evRef, rec.ref], [L.evName, person.name], [L.evType, rec.mode === "ext" ? L.evExt : L.evEntry], [L.evScheme, document.documentElement.lang.indexOf("zh") === 0 ? rec.zh : rec.en],
         [L.evIssue, rec.issued], rec.mode === "ext" ? [L.evStay, rec.until] : [L.evValid, rec.valid], [L.evStatus, L.evOk]]
          .forEach(function (r) { dl.appendChild(el("dt", { text: r[0] })); dl.appendChild(el("dd", { text: r[1] })); });
        out.appendChild(dl);
        return;
      }
      if (cfg.mode === "payment") out.appendChild(el("p", { cls: "ok", text: rec.fee ? L.evPaid : L.evNoFee }));
      var d = el("button", { type: "button", cls: "btn", text: L.dlEvisa });
      d.addEventListener("click", function () { window.BHGEVisaPDF(rec, S.vals.dob); });
      out.appendChild(el("p", { cls: "dlp" }, [d]));
      });
    });
    box.appendChild(el("div", { cls: "nav" }, [b])); box.appendChild(out);
    root.appendChild(box);
  }

  /* records kept in the iAM Smart database (Supabase); null when the client is not available */
  function REC() {
    if (!window.IASClient) return Promise.resolve(null);
    return window.IASClient.ready.then(function () { return window.IAS && window.IAS.records ? window.IAS.records : null; }).catch(function () { return null; });
  }

  /* ------------------------------------------------------------------ appointment booking */
  function Booking(cfg) {
    var tabs = el("div", { cls: "tabsw" }), panel = el("div");
    var tMake = el("button", { type: "button", cls: "tb on", text: L.makeAppt }), tFind = el("button", { type: "button", cls: "tb", text: L.findAppt });
    tabs.appendChild(tMake); tabs.appendChild(tFind);
    root.appendChild(tabs); root.appendChild(panel);
    function store(v) { try { return v === undefined ? JSON.parse(localStorage.getItem("bhg-bookings") || "{}") : localStorage.setItem("bhg-bookings", JSON.stringify(v)); } catch (e) { return v === undefined ? {} : null; } }
    function show(which) {
      tMake.classList.toggle("on", which === "make"); tFind.classList.toggle("on", which === "find");
      clear(panel);
      if (which === "make") { var w = document.createElement("div"); panel.appendChild(w); makeWizard(w); } else findPanel();
    }
    tMake.addEventListener("click", function () { show("make"); });
    tFind.addEventListener("click", function () { show("find"); });

    function makeWizard(w) {
      Wizard({
        prefix: "AP", doneText: cfg.doneText, doneNote: cfg.doneNote, steps: cfg.steps, declare: null, pay: null,
        doneRows: [{ n: "office", l: L.office, o: C.offices }, { n: "date", l: L.date }, { n: "time", l: L.time }],
        onDone: function (S) {
          var off = S.vals.office, ref = S.ref, code = S.vals.code;
          C.offices.forEach(function (o) { if (o[0] === off) off = o[1]; });
          var data = { office: off, date: S.vals.date, time: S.vals.time };
          REC().then(function (r) {
            if (r) return r.saveBooking(ref, code, data);
            var all = store(); data.code = code; all[ref] = data; store(all);
          });
          delete S.vals.code; delete S.vals.code2;
        }
      }, w);
    }
    function findPanel() {
      var wrap = el("section", { cls: "stepbox" });
      wrap.appendChild(el("h2", { text: L.findAppt }));
      wrap.appendChild(el("div", { cls: "intro", text: L.findIntro }));
      var grid = el("div", { cls: "grid" }), S = { vals: {}, files: {} };
      var f1 = { n: "ref", l: L.refNo, t: "text", req: true, v: "ref" }, f2 = { n: "code", l: L.enqCode, t: "password", req: true, v: "digits4", max: 4, im: "numeric" };
      grid.appendChild(buildField(f1, S, function () {})); grid.appendChild(buildField(f2, S, function () {}));
      wrap.appendChild(grid);
      var out = el("div", { cls: "result" });
      var b = el("button", { type: "button", cls: "btn", text: L.search });
      b.addEventListener("click", function () {
        clear(out);
        var ok = true;
        [f1, f2].forEach(function (f) { var w = wrap.querySelector('[data-n="' + f.n + '"]'), m = checkField(f, S.vals[f.n], S.vals); setErr(w, m); if (m) ok = false; });
        if (!ok) return;
        var ref = S.vals.ref.toUpperCase().replace(/\s/g, ""), code = S.vals.code;
        REC().then(function (r) {
          if (r) return r.findBooking(ref, code);
          var bk0 = store()[ref]; return bk0 && bk0.code === code ? bk0 : null;
        }).then(function (bk) {
          if (!bk) { out.appendChild(el("p", { cls: "errbox", text: L.notFound })); return; }
          var dl = el("dl", { cls: "review" });
          [[L.office, bk.office], [L.date, bk.date], [L.time, bk.time]].forEach(function (x) { dl.appendChild(el("dt", { text: x[0] })); dl.appendChild(el("dd", { text: x[1] })); });
          out.appendChild(dl);
          var cb = el("button", { type: "button", cls: "btn sec", text: L.cancelAppt });
          cb.addEventListener("click", function () {
            REC().then(function (r) {
              if (r) return r.cancelBooking(ref, code);
              var all = store(); delete all[ref]; store(all); return true;
            }).then(function () { clear(out); out.appendChild(el("p", { cls: "ok", text: L.cancelled })); });
          });
          out.appendChild(cb);
        });
      });
      wrap.appendChild(el("div", { cls: "nav" }, [b])); wrap.appendChild(out);
      panel.appendChild(wrap);
    }
    show("make");
  }

  /* ------------------------------------------------------------------ status enquiry */
  function Status(cfg) {
    var S = { vals: {}, files: {} };
    var box = el("section", { cls: "stepbox" });
    box.appendChild(el("h2", { text: cfg.title }));
    box.appendChild(el("div", { cls: "intro", html: cfg.intro }));
    var grid = el("div", { cls: "grid" });
    cfg.fields.forEach(function (f) { grid.appendChild(buildField(f, S, function () {})); });
    box.appendChild(grid);
    var out = el("div", { cls: "result" });
    var b = el("button", { type: "button", cls: "btn", text: L.search });
    b.addEventListener("click", function () {
      clear(out);
      var ok = true;
      cfg.fields.forEach(function (f) { var w = box.querySelector('[data-n="' + f.n + '"]'), m = checkField(f, S.vals[f.n], S.vals); setErr(w, m); if (m) ok = false; });
      if (!ok) return;
      var ref = String(S.vals.ref).toUpperCase(), h = hash(ref + (S.vals.dobDay || "") + (S.vals.dobYear || "") + (S.vals.dob || ""));
      var st = cfg.results[h % cfg.results.length];
      var d = today(); d.setDate(d.getDate() - (h % 6));
      var dl = el("dl", { cls: "review" });
      [[L.refNo, ref], [cfg.statusLabel, st[0]], [L.updated, ymd(d)], [L.remark, st[1]]].forEach(function (r) { dl.appendChild(el("dt", { text: r[0] })); dl.appendChild(el("dd", { text: r[1] })); });
      out.appendChild(dl);
    });
    box.appendChild(el("div", { cls: "nav" }, [b])); box.appendChild(out);
    root.appendChild(box);
  }

  /* ------------------------------------------------------------------ eTAX login + portal */
  function Login(cfg) {
    var S = { vals: {}, files: {} };
    var box = el("section", { cls: "stepbox narrow" });
    function drawLogin() {
      clear(box);
      box.appendChild(el("h2", { text: cfg.title }));
      box.appendChild(el("div", { cls: "intro", html: cfg.intro }));
      var grid = el("div", { cls: "grid one" });
      cfg.fields.forEach(function (f) { grid.appendChild(buildField(f, S, function () {})); });
      box.appendChild(grid);
      var b = el("button", { type: "button", cls: "btn", text: L.login });
      b.addEventListener("click", function () {
        var ok = true;
        cfg.fields.forEach(function (f) { var w = box.querySelector('[data-n="' + f.n + '"]'), m = checkField(f, S.vals[f.n], S.vals); setErr(w, m); if (m) ok = false; });
        if (ok) drawPortal();
      });
      box.appendChild(el("div", { cls: "nav" }, [b]));
      var lk = el("p", { cls: "links" });
      cfg.links.forEach(function (l) { lk.appendChild(el("a", { href: l[1], text: l[0] })); });
      box.appendChild(lk);
    }
    function drawPortal() {
      clear(box); box.classList.remove("narrow");
      var acct = String(S.vals.acct), h = hash(acct);
      box.appendChild(el("h2", { text: cfg.portalTitle }));
      box.appendChild(el("p", { cls: "welcome", text: cfg.welcome + " " + acct.slice(0, 2) + "****" + acct.slice(-2) }));
      var t = el("table", { cls: "feet" });
      t.appendChild(el("tr", {}, cfg.taxCols.map(function (c) { return el("th", { text: c }); })));
      [2026, 2025, 2024].forEach(function (y, i) {
        var pay = 4000 + (h % 90) * 100 + i * 700, paid = i === 0 ? 0 : pay;
        t.appendChild(el("tr", {}, [el("td", { text: y - 1 + "/" + String(y).slice(2) }), el("td", { cls: "amt", text: money(pay) }), el("td", { cls: "amt", text: money(paid) }), el("td", { cls: "amt", text: money(pay - paid) })]));
      });
      box.appendChild(el("h3", { text: cfg.taxPos })); box.appendChild(t);
      box.appendChild(el("h3", { text: cfg.msgTitle }));
      var ul = el("ul", { cls: "msgs" });
      cfg.messages.forEach(function (m) { ul.appendChild(el("li", { text: m })); });
      box.appendChild(ul);
      box.appendChild(el("h3", { text: cfg.svcTitle }));
      var sv = el("ul", { cls: "svcl" });
      cfg.services.forEach(function (s) { sv.appendChild(el("li", {}, [el("a", { href: s[1], text: s[0] })])); });
      box.appendChild(sv);
      var out = el("button", { type: "button", cls: "btn sec", text: L.logout });
      out.addEventListener("click", function () { S.vals = {}; box.classList.add("narrow"); drawLogin(); });
      box.appendChild(el("div", { cls: "nav" }, [out]));
    }
    drawLogin();
    root.appendChild(box);
  }

  /* ------------------------------------------------------------------ tax calculator */
  function TaxCalc(cfg) {
    var P = cfg.params, S = { vals: { year: cfg.years[0] }, files: {} };
    var box = el("section", { cls: "stepbox" });
    box.appendChild(el("h2", { text: cfg.title }));
    box.appendChild(el("div", { cls: "intro", html: cfg.intro }));
    var grid = el("div", { cls: "grid" });
    cfg.fields.forEach(function (f) { grid.appendChild(buildField(f, S, function () {})); });
    box.appendChild(grid);
    var out = el("div", { cls: "result" });
    function n(k) { var v = parseFloat(S.vals[k]); return isFinite(v) && v > 0 ? v : 0; }
    function prog(x) {
      var tax = 0, left = x;
      P.bands.forEach(function (b) { var take = Math.min(left, b[0]); tax += take * b[1]; left -= take; });
      if (left > 0) tax += left * P.top;
      return tax;
    }
    function std(x) { return x <= P.stdCap ? x * P.stdLow : P.stdCap * P.stdLow + (x - P.stdCap) * P.stdHigh; }
    function compute(who) {
      var income = n("income"), mpf = Math.min(n("mpf"), P.mpfMax);
      var ded = mpf + Math.min(n("rent"), P.rentMax) + Math.min(n("loan"), P.loanMax) + Math.min(n("elder"), P.elderMax) + Math.min(n("edu"), P.eduMax) + Math.min(n("donation"), income * 0.35);
      var married = S.vals.marital === "married", sp = n("spIncome"), spDed = Math.min(n("spMpf"), P.mpfMax);
      var allow = who === "joint" ? P.married : P.basic;
      if (S.vals.marital === "single_parent") allow += P.singleParent;
      allow += (+S.vals.kids || 0) * P.child + (+S.vals.kidsNew || 0) * P.child;
      allow += (+S.vals.par60 || 0) * P.par60 + (+S.vals.par55 || 0) * P.par55 + (+S.vals.sib || 0) * P.sib + (+S.vals.dis || 0) * P.disabled;
      if (S.vals.selfDis === "yes") allow += P.disabled;
      var inc = income, dd = ded;
      if (who === "joint") { inc = income + sp; dd = ded + spDed; }
      var net = Math.max(inc - dd, 0), ncid = Math.max(net - allow, 0);
      var tp = prog(ncid), ts = std(net), tax = Math.min(tp, ts);
      var cap = P.redByYear && P.redByYear[S.vals.year] !== undefined ? P.redByYear[S.vals.year] : P.redCap, red = Math.min(tax * P.redPct, cap);
      return { inc: inc, ded: dd, allow: allow, net: net, ncid: ncid, tp: tp, ts: ts, tax: Math.max(tax - red, 0), red: red, pre: tax };
    }
    function row(a, b, bold) { return el("tr", { cls: bold ? "tot" : "" }, [el("td", { text: a }), el("td", { cls: "amt", text: b })]); }
    var b = el("button", { type: "button", cls: "btn", text: L.compute });
    b.addEventListener("click", function () {
      clear(out);
      var ok = true;
      cfg.fields.forEach(function (f) { if (f.t === "info") return; var w = box.querySelector('[data-n="' + f.n + '"]'), m = checkField(f, S.vals[f.n], S.vals); setErr(w, m); if (m) ok = false; });
      if (!ok) return;
      var r = compute("sep"), married = S.vals.marital === "married", j = married && n("spIncome") > 0 ? compute("joint") : null;
      var t = el("table", { cls: "feet" });
      t.appendChild(row(cfg.out.income, money(Math.round(r.inc))));
      t.appendChild(row(cfg.out.ded, money(Math.round(r.ded))));
      t.appendChild(row(cfg.out.net, money(Math.round(r.net))));
      t.appendChild(row(cfg.out.allow, money(Math.round(r.allow))));
      t.appendChild(row(cfg.out.ncid, money(Math.round(r.ncid))));
      t.appendChild(row(cfg.out.prog, money(Math.round(r.tp))));
      t.appendChild(row(cfg.out.std, money(Math.round(r.ts))));
      if (r.red > 0) t.appendChild(row(cfg.out.red, "−" + money(Math.round(r.red))));
      t.appendChild(row(cfg.out.tax, money(Math.round(r.tax)), true));
      out.appendChild(el("h3", { text: cfg.out.title })); out.appendChild(t);
      if (j) {
        out.appendChild(el("p", { cls: j.tax < r.tax ? "ok" : "hint", text: (j.tax < r.tax ? cfg.out.jointBetter : cfg.out.jointWorse) + " (" + money(Math.round(j.tax)) + ")" }));
      }
      out.appendChild(el("p", { cls: "hint", html: cfg.out.note }));
    });
    box.appendChild(el("div", { cls: "nav" }, [b])); box.appendChild(out);
    root.appendChild(box);
  }

  /* ------------------------------------------------------------------ start */
  var started = false;
  function startSvc() {
    if (started) return; started = true;
    if (C.type === "wizard") Wizard(C);
    else if (C.type === "booking") Booking(C);
    else if (C.type === "status") Status(C);
    else if (C.type === "evisa") EVisa(C);
    else if (C.type === "login") Login(C);
    else if (C.type === "taxcalc") TaxCalc(C);
  }
  window.svcStart = startSvc;
  if (!document.getElementById("term")) startSvc();
})();
