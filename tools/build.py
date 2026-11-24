#!/usr/bin/env python3
"""Static site generator for the Immigration Department of the Baekhyeon Hwarang Special Administrative Region.

Layout and information architecture follow the Hong Kong Immigration Department website and its e-service
start page. All code, artwork and wording are original.   python3 tools/build.py
"""
import html
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import data_immd as M        # noqa: E402
import data_info as I        # noqa: E402
import data_travel as T      # noqa: E402
import data_esvc as E        # noqa: E402
from t2s_map import T2S, PHRASES  # noqa: E402

LANGS = [("en", "en", "en", "English"), ("ko", "ko", "ko", "한국어"), ("hant", "zh-hant", "zh-Hant", "繁"), ("hans", "zh-hans", "zh-Hans", "简")]
IDX = {"en": 0, "ko": 1, "hant": 2, "hans": 3}
FOLDER = [l[1] for l in LANGS]


def s2(text):
    for a, b in PHRASES:
        text = text.replace(a, b)
    return "".join(T2S.get(c, c) for c in text)


def g(tup, i):
    return s2(tup[2]) if i == 3 else tup[i]


def t(tup, i):
    return html.escape(g(tup, i))


def U(k, i):
    return t(M.UI[k], i)


def depth(path):
    return len([p for p in path.split("/") if p])


def rel(cur, target):
    up = "../" * depth(cur)
    return (up or "./") if not target else up + target + "/"


def gov(i, path=""):
    return M.GOV_BASE + FOLDER[i] + "/" + ((path + "/") if path else "")


# ----------------------------------------------------------------------------- pages registry
SV = "services/travel-documents"
PAGES = {}


def reg(path, **kw):
    PAGES[path] = kw


ARTICLES = {
    SV + "/photo": (I.PHOTO_TITLE, I.PHOTO), SV + "/fees": (I.FEES_TITLE, I.FEES), SV + "/faq": (I.FAQ_TITLE, I.FAQ),
    SV + "/kiosk": (I.KIOSK_TITLE, I.KIOSK), SV + "/docid": (I.ABOUT_DOCID_TITLE, I.ABOUT_DOCID),
    SV + "/reentry": (I.ABOUT_REENTRY_TITLE, I.ABOUT_REENTRY), SV + "/seaman": (I.ABOUT_SEAMAN_TITLE, I.ABOUT_SEAMAN),
    "services/identity-cards": (("Identity Cards", "신분증", "身份證"), I.SMARTID),
    "contact/branch-offices": (I.BRANCH_TITLE, I.BRANCH), "contact/hq-offices": (I.HQ_TITLE, I.HQ),
}
BLOCK_TARGET = {
    "idbook": "eservices/idcard-booking/loading", "apply": "eservices/passport-application/loading", "appointment": "eservices/travel-document-booking/loading",
    "photo": SV + "/photo", "fees": SV + "/fees", "faq": SV + "/faq",
}
ESERVICES = {
    "passport-application": lambda: E.PASSPORT, "travel-document-booking": lambda: E.booking("td"), "idcard-booking": lambda: E.booking("id"),
    "travel-document-status": lambda: E.TD_STATUS, "application-status": lambda: E.VISA_STATUS,
}


def build_registry():
    PAGES.clear()
    reg("", kind="home", title=M.UI["dept"])
    reg("services", kind="services", title=dict(M.NAV)["services"], crumbs=[])
    for slug, title, _ic in M.SERVICES:
        if slug not in ("travel-documents", "identity-cards"):
            reg("services/" + slug, kind="stub", title=title, crumbs=[("services", dict(M.NAV)["services"])])
    reg(SV, kind="cat", title=("Travel Documents", "여행증명서", "旅行證件"), crumbs=[("services", dict(M.NAV)["services"])])
    reg(SV + "/apply-passport", kind="apply", title=M.TD_PAGES[0][1], crumbs=[("services", dict(M.NAV)["services"]), (SV, ("Travel Documents", "여행증명서", "旅行證件"))])
    for path, (title, blocks) in ARTICLES.items():
        if path.startswith(SV):
            crumbs = [("services", dict(M.NAV)["services"]), (SV, ("Travel Documents", "여행증명서", "旅行證件"))]
        elif path.startswith("services/"):
            crumbs = [("services", dict(M.NAV)["services"])]
        else:
            crumbs = [("contact", dict(M.NAV)["contact"])]
        reg(path, kind="article", title=title, crumbs=crumbs)
    reg("online-services", kind="online", title=dict(M.NAV)["online-services"], crumbs=[])
    for slug, title in M.NAV:
        if slug not in ("services", "online-services"):
            reg(slug, kind="stub", title=title, crumbs=[])
    for key in ESERVICES:
        reg("eservices/" + key, kind="eservice", title=M.ES_TITLES[key], key=key)
        reg("eservices/" + key + "/loading", kind="loading", title=M.ES_TITLES[key], key=key)


# ----------------------------------------------------------------------------- icons
ICON = {
    "visa": '<rect x="8" y="10" width="32" height="28" rx="3"/><circle cx="19" cy="22" r="5"/><path d="M14 33c1-4 9-4 10 0M28 19h8M28 25h8"/>',
    "idcard": '<rect x="6" y="12" width="36" height="24" rx="3"/><circle cx="17" cy="23" r="4"/><path d="M11 32c1-4 11-4 12 0M28 20h10M28 26h10"/>',
    "abode": '<path d="M24 5c-8 0-13 6-13 12 0 9 13 24 13 24s13-15 13-24c0-6-5-12-13-12z"/><circle cx="24" cy="17" r="5"/>',
    "passport": '<rect x="10" y="5" width="28" height="38" rx="3"/><circle cx="24" cy="21" r="8"/><path d="M16 21h16M24 13c-4 4-4 12 0 16M24 13c4 4 4 12 0 16M15 36h18"/>',
    "flag": '<path d="M12 6v38M12 8h24l-5 9 5 9H12"/>',
    "baby": '<circle cx="24" cy="22" r="9"/><path d="M17 36c3-4 11-4 14 0M20 20h.01M28 20h.01M21 25c2 2 4 2 6 0"/>',
    "rings": '<circle cx="18" cy="28" r="10"/><circle cx="30" cy="28" r="10"/><path d="M21 12l3-4 3 4-3 5z"/>',
    "gate": '<path d="M8 40h32M12 40V14h24v26M18 14V8h12v6M20 26h8"/>',
    "help": '<circle cx="24" cy="18" r="9"/><path d="M10 40c2-9 26-9 28 0M18 16c1 3 11 3 12 0"/>',
    "cloud": '<path d="M14 34h20a8 8 0 000-16 11 11 0 00-21-2 8 9 0 001 18z"/>',
}


def icon(name, size=64):
    return ('<svg viewBox="0 0 48 48" width="%d" height="%d" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % (size, size, ICON[name]))


# ----------------------------------------------------------------------------- shell
def logo(i, cur, small=False):
    return ('<a class="logo" href="%s"><img src="%%A%%flag.jpg" alt="" width="%d" height="%d"><span><strong>%s</strong><em>%s</em></span></a>'
            % (rel(cur, ""), 40 if small else 54, 40 if small else 54, U("dept", i), U("govline", i)))


def lang_links(i, cur):
    out = []
    for code, folder, hl, label in LANGS:
        up = "../" * (depth(cur) + 1)
        out.append('<a href="%s%s/%s" lang="%s"%s>%s</a>' % (up, folder, (cur + "/") if cur else "", hl, ' class="cur"' if IDX[code] == i else "", label))
    return "".join(out)


def header(i, cur):
    nav = "".join('<li><a href="%s"%s>%s</a></li>' % (rel(cur, s), ' class="on"' if (cur == s or cur.startswith(s + "/")) else "", t(tt, i)) for s, tt in M.NAV)
    return (
        '<header class="hd"><div class="wrap hd-in">%s<div class="hd-r"><div class="tools"><a href="%s" class="ico" aria-label="%s">&#8962;</a>'
        '<span class="langs">%s</span><span class="ol">%s</span><button type="button" id="textsize">%s</button></div>'
        '<form class="sq" role="search"><input type="search" placeholder="%s" aria-label="%s"></form></div></div>'
        '<nav class="nv" aria-label="Main"><div class="wrap"><ul>%s</ul></div></nav></header>'
        % (logo(i, cur), rel(cur, ""), U("home", i), lang_links(i, cur), U("other_lang", i), U("text_size", i), U("search_ph", i), U("search_ph", i), nav)
    )


def side_tabs(i, cur):
    return ('<div class="sidetabs"><a href="%s"><b>%s</b></a><a href="%s"><b>%s</b></a></div>'
            % (rel(cur, SV + "/faq"), U("faq_tab", i), rel(cur, "contact"), U("enq_tab", i)))


def footer(i, cur):
    svc = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, "services/" + s), t(tt, i)) for s, tt, _ in M.SERVICES[:7])
    onl = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, p), t(tt, i)) for tt, p in M.ONLINE_ITEMS)
    about = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, s), t(tt, i)) for s, tt in M.NAV if s in ("about-us", "forms", "publications", "useful-information"))
    return (
        '<footer class="ft"><div class="wrap ft-in"><div class="fc c1"><h3>%s</h3><p><strong>%s</strong></p><a class="fl" href="%s">%s</a><a class="fl" href="%s">%s</a></div>'
        '<div class="fc"><h3>%s</h3><ul>%s</ul></div><div class="fc"><h3>%s</h3><ul>%s</ul></div><div class="fc"><h3>%s</h3><ul>%s</ul></div></div>'
        '<div class="wrap ft-b"><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a></div></footer>'
        % (U("hq", i), U("hq_addr", i), rel(cur, "contact/hq-offices"), U("addr_link", i), rel(cur, "contact"), U("enq_form", i),
           t(dict(M.NAV)["about-us"], i), about, t(dict(M.NAV)["services"], i), svc, t(dict(M.NAV)["online-services"], i), onl,
           gov(i), U("govhk", i), gov(i, "misc/copyright"), U("copyright", i), gov(i, "misc/privacy"), U("privacy", i), gov(i, "misc/disclaimer"), U("disclaimer", i))
    )


def head(i, hl, title, cur, cls=""):
    up = "../" * (depth(cur) + 1)
    return ('<!doctype html><html lang="%s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>%s | %s</title><link rel="icon" href="%sassets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="%sassets/site.css"></head>'
            '<body class="%s lang-%s"><a class="skip" href="#main">%s</a>' % (hl, html.escape(title), html.escape(g(M.UI["dept"], i)), up, up, cls, LANGS[i][0], U("skip", i)))


def finish(text, cur):
    return text.replace("%A%", "../" * (depth(cur) + 1) + "assets/")


def tail(extra=""):
    return '<script src="%A%immd.js"></script>' + extra + "</body></html>"


def banner(title_tup, i):
    return '<section class="bn"><div class="wrap"><h2>%s</h2></div></section>' % t(title_tup, i)


def crumbs(i, cur, info):
    parts = ['<a href="%s" class="hm" aria-label="%s">&#8962;</a>' % (rel(cur, ""), U("home", i))]
    for path, title in info.get("crumbs", []):
        parts.append('<a href="%s">%s</a>' % (rel(cur, path), t(title, i)))
    parts.append('<span class="cur">%s</span>' % t(info["title"], i))
    return '<div class="wrap bc">%s</div>' % '<i>&gt;</i>'.join(parts)


def page(i, hl, cur, info, body, cls="", extra=""):
    txt = head(i, hl, g(info["title"], i), cur, cls) + header(i, cur)
    if info["kind"] != "home":
        txt += banner(dict(M.NAV)["services"] if cur.startswith("services") else (dict(M.NAV)["contact"] if cur.startswith("contact") else info["title"]), i)
        txt += crumbs(i, cur, info)
    txt += '<main id="main" class="wrap main">%s</main>' % body
    txt += side_tabs(i, cur) + footer(i, cur) + tail(extra)
    return finish(txt, cur)


# ----------------------------------------------------------------------------- content blocks
def href(slug, cur):
    return rel(cur, BLOCK_TARGET.get(slug, SV + "/faq"))


def render_blocks(blocks, i, cur):
    out = []
    for b in blocks:
        k = b[0]
        if k == "p":
            out.append("<p>%s</p>" % g(b[1], i))
        elif k == "plain":
            out.append('<p>%s</p>' % g(b[1], i))
        elif k == "h2":
            out.append("<h2>%s</h2>" % html.escape(g(b[1], i)))
        elif k == "h3":
            out.append("<h3>%s</h3>" % html.escape(g(b[1], i)))
        elif k in ("ol", "ul"):
            out.append("<%s>%s</%s>" % (k, "".join("<li>%s</li>" % html.escape(g(x, i)) for x in b[1]), k))
        elif k == "btn":
            out.append('<p><a class="obtn" href="%s">%s</a></p>' % (href(b[2], cur), html.escape(g(b[1], i))))
        elif k == "table":
            head_ = "".join("<th>%s</th>" % html.escape(g(c, i)) for c in b[1])
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % g(c, i) for c in r) for r in b[2])
            out.append('<div class="tblw"><table class="dt"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head_, rows))
        elif k == "faq":
            items = "".join('<li><button type="button" class="faq-q" aria-expanded="false"><span>Q%d. %s</span><i class="pl"></i></button><div class="faq-a" hidden><p>%s</p></div></li>'
                            % (n, html.escape(g(q, i)), html.escape(g(a, i))) for n, (q, a) in enumerate(b[1], 1))
            out.append('<div class="faq"><p class="ftools"><button type="button" data-faq="open">%s</button><button type="button" data-faq="close">%s</button></p><ul>%s</ul></div>' % (U("expand_all", i), U("collapse_all", i), items))
    return "".join(out)


def poll_rev(i):
    return '<p class="rev">%s%s</p>' % (U("last_rev", i), U("rev_val", i))


def article(i, cur, info):
    title, blocks = ARTICLES[cur]
    return '<h1>%s</h1><div class="art">%s</div>%s' % (t(title, i), render_blocks(blocks, i, cur), poll_rev(i))


def services_page(i, cur, info):
    cards = "".join('<li><a href="%s"><span class="ic">%s</span><span>%s</span></a></li>' % (rel(cur, "services/" + s), icon(ic), t(tt, i)) for s, tt, ic in M.SERVICES)
    return '<h1>%s</h1><ul class="icons">%s</ul>' % (t(info["title"], i), cards)


def cat_page(i, cur, info):
    lis = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, SV + "/" + p), t(tt, i)) for p, tt in M.TD_PAGES)
    return '<h1>%s</h1><ul class="links">%s</ul>' % (t(info["title"], i), lis)


def online_page(i, cur, info):
    lis = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, p), t(tt, i)) for tt, p in M.ONLINE_ITEMS)
    return '<h1>%s</h1><ul class="links">%s</ul>' % (t(info["title"], i), lis)


def stub_page(i, cur, info):
    return '<h1>%s</h1><p>%s</p>' % (t(info["title"], i), U("stub", i))


def home_page(i, hl, cur, info):
    cards = "".join('<li><a href="%s"><span class="ic">%s</span><span>%s</span></a></li>' % (rel(cur, "services/" + s), icon(ic), t(tt, i)) for s, tt, ic in M.SERVICES)
    onl = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, p), t(tt, i)) for tt, p in M.ONLINE_ITEMS)
    body = ('<section class="hero"><div class="hero-in"><img src="%%A%%flag.jpg" alt="" class="hflag"><h1>%s</h1><p>%s</p></div></section>'
            '<section class="wrap"><h2 class="sec">%s</h2><ul class="icons">%s</ul></section>'
            '<section class="wrap"><h2 class="sec">%s</h2><ul class="links">%s</ul></section>'
            % (t(M.HERO, i), t(M.HERO_SUB, i), t(dict(M.NAV)["services"], i), cards, t(dict(M.NAV)["online-services"], i), onl))
    txt = head(i, hl, g(M.UI["dept"], i), cur, "home") + header(i, cur) + body + side_tabs(i, cur) + footer(i, cur) + tail()
    return finish(txt, cur)


# ----------------------------------------------------------------------------- application for passport (tabs)
def tab_sections(i, cur, place):
    tabs = T.GB_TABS[:2] if place == "in" else T.GB_TABS[2:]
    out = {}
    out["before"] = (
        '<details><summary>%s</summary><div><p>%s</p><ul>%s</ul></div></details>'
        '<details><summary>%s</summary><div><p>%s</p></div></details>'
        '<details><summary>%s</summary><div><p>%s</p></div></details>'
        '<details><summary>%s</summary><div><p><a href="%s">%s</a></p></div></details>'
        % (t(M.AP_SECT["elig"], i), t(T.GB_INTRO, i), "".join("<li>%s</li>" % t(x, i) for x in T.GB_ELIG),
           t(M.AP_SECT["proc"], i), t(M.AP_PROC, i), t(M.AP_SECT["child"], i), t(M.AP_CHILD, i),
           t(M.AP_SECT["faq"], i), rel(cur, SV + "/faq"), t(M.AP_SECT["faq"], i)))
    sub = []
    for tb in tabs:
        forms = "".join("<li><strong>%s</strong>%s</li>" % (html.escape(g(h, i)), ("<br>" + html.escape(g(b, i))) if b else "") for h, b in tb["forms"])
        docs = ""
        for hd, lines in tb["docs"]:
            docs += "<h4>%s</h4>" % t(hd, i) + "".join("<p>%s%s</p>" % (lab, t(tx, i)) for lab, tx in lines)
        cols, rows, note, _a, _b = tb["means"]
        th = "<th></th>" + "".join("<th>%s</th>" % t(c, i) for c in cols)
        tr = "".join("<tr><th>%s</th>%s</tr>" % (t(lab, i), "".join("<td>%s</td>" % ("✓" if m else "") for m in marks)) for lab, marks in rows)
        sub.append('<details><summary>%s</summary><div><h4>%s</h4><ul>%s</ul>%s<h4>%s</h4><div class="tblw"><table class="dt">%s%s</table></div><p class="fn">%s</p></div></details>'
                   % (t(tb["title"], i), t(T.GB_SEC["forms"], i), forms, docs, t(T.GB_SEC["means"], i), "<thead><tr>%s</tr></thead>" % th, "<tbody>%s</tbody>" % tr, t(note, i)))
    out["applying"] = (
        '<details open><summary>%s</summary><div><p>%s</p><p><a class="obtn" href="%s">%s</a> <a class="obtn alt" href="%s">%s</a></p></div></details>'
        % (t(M.AP_SECT["apply"], i), t(M.AP_APPLY_NOTE, i), rel(cur, "eservices/passport-application/loading"), t(M.AP_BTN_APPLY, i), rel(cur, "eservices/travel-document-booking/loading"), t(M.AP_BTN_BOOK, i))
        + "".join(sub)
        + '<details><summary>%s</summary><div><p><a href="%s">%s</a></p></div></details><details><summary>%s</summary><div><p><a href="%s">%s</a></p></div></details>'
        % (t(M.AP_SECT["photo"], i), rel(cur, SV + "/photo"), t(I.PHOTO_TITLE, i), t(M.AP_SECT["fees"], i), rel(cur, SV + "/fees"), t(I.FEES_TITLE, i)))
    col = "".join("<p><strong>%s</strong><br>%s</p>" % (t(h, i), t(b, i)) for h, b in tabs[0]["collect"])
    out["after"] = (
        '<details><summary>%s</summary><div>%s</div></details>' % (t(M.AP_SECT["collect"], i), col)
        + ('<details><summary>%s</summary><div><p><a href="%s">%s</a></p></div></details>' % (t(M.AP_SECT["kiosk"], i), rel(cur, SV + "/kiosk"), t(I.KIOSK_TITLE, i)) if place == "in" else "")
        + '<details><summary>%s</summary><div><p><a class="obtn" href="%s">%s</a></p></div></details>' % (t(M.AP_SECT["status"], i), rel(cur, "eservices/travel-document-status/loading"), t(M.AP_BTN_STATUS, i))
        + '<details><summary>%s</summary><div><p><a href="%s">%s</a></p></div></details>' % (t(M.AP_SECT["lost"], i), gov(i, "residents/immigration/traveldoc/lost"), t(I.LOST_TITLE, i)))
    return out


def apply_page(i, cur, info):
    sel = "".join('<option value="%s">%s</option>' % (k, t(tt, i)) for k, tt in M.AP_PLACES)
    tabs = "".join('<button type="button" data-tab="%s" class="%s">%s</button>' % (k, "on" if k == "before" else "", t(tt, i)) for k, tt in M.AP_TABS)
    panels = []
    for place, ptitle in M.AP_PLACES:
        secs = tab_sections(i, cur, place)
        for k, tt in M.AP_TABS:
            panels.append('<div class="tp" data-place="%s" data-tab="%s"%s><h3 class="pt">%s: %s</h3><hr><p class="ea"><button type="button" data-ea>%s</button></p>%s</div>'
                          % (place, k, "" if (place == "in" and k == "before") else " hidden", t(M.AP_PLACE_LABEL, i), t(ptitle, i), U("expand_all", i), secs[k]))
    return ('<h1 class="teal">%s</h1><div class="pick"><div class="circle">%s</div><div class="selw"><span>%s:</span><select id="place">%s</select></div></div>'
            '<div class="tabs3">%s</div><div class="tpanels">%s</div>'
            '<h3 class="rt"><span>%s</span></h3><ul class="links"><li><a href="%s">%s</a></li><li><a href="%s">%s</a></li></ul>%s'
            % (t(info["title"], i), t(M.AP_PLEASE, i), t(M.AP_PLACE_LABEL, i), sel, tabs, "".join(panels), t(M.UI["related"], i),
               rel(cur, SV + "/photo"), t(I.PHOTO_TITLE, i), rel(cur, SV + "/fees"), t(I.FEES_TITLE, i), poll_rev(i)))


# ----------------------------------------------------------------------------- e-services
def loc(o, i):
    if isinstance(o, tuple) and len(o) == 3 and all(isinstance(x, str) for x in o):
        return g(o, i)
    if isinstance(o, (list, tuple)):
        return [loc(x, i) for x in o]
    if isinstance(o, dict):
        return {k: loc(v, i) for k, v in o.items()}
    return o


def eservice_page(i, hl, cur, info):
    key = info["key"]
    cfg = loc(ESERVICES[key](), i)
    cfg["L"] = loc(E.L, i)
    cfg["cur"] = E.CUR
    cfg.setdefault("offices", loc(E.OFFICES, i))
    if key == "passport-application":
        cfg["passportPdf"] = True
    blob = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    term = key == "passport-application"
    menu = ""
    term_html = ""
    if term:
        menu = '<ul class="esm">%s</ul>' % "".join('<li><a href="#" data-stub>%s</a></li>' % t(x, i) for x in M.ES_MENU)
        terms = "".join("<h4>%s</h4><p>%s</p>" % (t(h, i), t(b, i)) for h, b in M.ES_TERMS)
        term_html = (
            '<div id="term"><section class="pn"><h3>%s</h3><div class="pb red">%s</div></section>'
            '<section class="pn"><h3>%s</h3><div class="pb sc">%s</div></section>'
            '<p class="decl"><strong>%s</strong></p><label class="chk"><input type="checkbox" id="agree"> <span>%s</span></label>'
            '<p class="err" id="agree-err" role="alert" data-msg="%s"></p>'
            '<p class="btns"><button type="button" class="eb" id="retrieve">%s</button><button type="button" class="eb" id="start">%s</button></p>'
            '<div id="retrieve-box" hidden><div class="pn"><h3>%s</h3><div class="pb"><label>%s <input type="text" id="r_id" autocomplete="off"></label> <label>%s <input type="text" id="r_code" autocomplete="off"></label> <button type="button" class="eb" id="r_go">%s</button><p class="err" id="r_msg" data-msg="%s"></p></div></div></div></div>'
            % (t(M.ES_ANN_TITLE, i), "".join("<p>%s</p>" % t(x, i) for x in M.ES_ANN), t(M.ES_TERMS_TITLE, i), terms,
               t(("Declaration", "선서", "聲明"), i), t(M.ES_DECLARE, i), t(M.ES_ERR_AGREE, i), t(M.ES_BTN_RETRIEVE, i), t(M.ES_BTN_START, i),
               t(M.ES_RETRIEVE["title"], i), t(M.ES_RETRIEVE["id"], i), t(M.ES_RETRIEVE["code"], i), t(M.ES_RETRIEVE["go"], i), t(M.ES_RETRIEVE["none"], i)))
    up = "../" * (depth(cur) + 1)
    txt = (
        '<!doctype html><html lang="%s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>%s | %s</title>'
        '<link rel="icon" href="%sassets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="%sassets/site.css"></head><body class="es lang-%s">'
        '<header class="es-h"><div class="es-logo"><img src="%%A%%flag.jpg" alt="" width="54" height="54"><span><strong>%s</strong><em>%s</em></span></div></header>'
        '<div class="es-bar wrap"><span class="langs">%s</span><a href="%s">%s</a></div>'
        '<div class="wrap"><div class="es-title">%s</div><div class="es-body%s">%s<div class="es-main">%s<div id="svc" class="svc"%s></div></div></div></div>'
        '<footer class="es-f"><div class="wrap"><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a></div></footer>'
        '<script type="application/json" id="svc-cfg">%s</script><script src="%%A%%immd.js"></script>%s<script src="%%A%%svc.js"></script></body></html>'
        % (hl, html.escape(g(info["title"], i)), html.escape(g(M.UI["dept"], i)), up, up, LANGS[i][0], U("dept", i), U("govline", i), lang_links(i, cur), rel(cur, ""), U("exit", i),
           t(info["title"], i), " has-menu" if term else "", menu, term_html, " hidden" if term else "",
           gov(i), U("govhk", i), gov(i, "misc/copyright"), U("copyright", i), gov(i, "misc/privacy"), U("privacy", i), gov(i, "misc/disclaimer"), U("disclaimer", i), blob, '<script src="%A%passport-pdf.js"></script>' if term else ""))
    return finish(txt, cur)


LOADING_SYS = {"passport-application": "EPASSPORT2", "travel-document-booking": "EPASSPORT2", "travel-document-status": "EPASSPORT2",
               "idcard-booking": "SMARTICS2", "application-status": "EVISA2"}


def loading_page(i, hl, cur, info):
    """Same behaviour as the Immigration Department's QueueIt.html: a bare spinner page that forwards to the
    e-service, with a manual link if the browser has not moved on after 20 seconds."""
    msg = g(("If you are not redirected, please click <a href='../'>here</a>...", "자동으로 이동하지 않으면 <a href='../'>여기</a>를 누르세요...",
             "如未能自動轉往，請按<a href='../'>此處</a>..."), i)
    return ('<!doctype html><html lang="%s"><head><meta charset="utf-8"><meta http-equiv="x-ua-compatible" content="ie=edge">'
            '<meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="cache-control" content="no-cache"><title>%s</title>'
            '<noscript><meta http-equiv="refresh" content="2;url=../"></noscript>'
            '<style>body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#fff}.loader{border:5px solid #f3f3f3;border-radius:50%%;border-top:5px solid #3498db;'
            'width:50px;height:50px;animation:spin 2s linear infinite}@keyframes spin{0%%{transform:rotate(0deg)}100%%{transform:rotate(360deg)}}'
            '.container{height:200px;position:relative}.center{margin:0;position:absolute;top:50%%;left:50%%;transform:translate(-50%%,-50%%);text-align:center}'
            '#myMessage{font-size:14px;margin-top:14px;white-space:nowrap}</style></head><body><h2></h2><p></p><div class="container"><div class="center">'
            '<div class="loader"></div><div id="myMessage"></div></div></div>'
            '<script>(function(){var t=setTimeout(function(){location.replace("../");},1800);'
            'setTimeout(function(){var p=document.createElement("p");p.innerHTML=%s;document.getElementById("myMessage").appendChild(p);},20000);})();</script>'
            '</body></html>' % (hl, LOADING_SYS[info["key"]], json.dumps(msg)))


# ----------------------------------------------------------------------------- main
ROOT_INDEX = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Immigration Department - Baekhyeon Hwarang SAR</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<noscript><meta http-equiv="refresh" content="0; url=en/"></noscript>
<script>
(function () {
  var l = (navigator.language || "en").toLowerCase(), d = "en/";
  if (l.indexOf("ko") === 0) d = "ko/";
  else if (l.indexOf("zh") === 0) d = /zh-(cn|sg|hans)/.test(l) ? "zh-hans/" : "zh-hant/";
  location.replace(d);
})();
</script></head>
<body style="font-family:sans-serif;padding:2em">
<p><a href="en/">English</a> &middot; <a href="ko/">한국어</a> &middot; <a href="zh-hant/">繁體中文</a> &middot; <a href="zh-hans/">简体中文</a></p>
</body></html>
"""


def main():
    build_registry()
    for _c, folder, _h, _l in LANGS:
        shutil.rmtree(os.path.join(ROOT, folder), ignore_errors=True)
    n = 0
    for code, folder, hl, _l in LANGS:
        i = IDX[code]
        for path, info in PAGES.items():
            k = info["kind"]
            if k == "home":
                txt = home_page(i, hl, path, info)
            elif k == "eservice":
                txt = eservice_page(i, hl, path, info)
            elif k == "loading":
                txt = loading_page(i, hl, path, info)
            else:
                body = {"services": services_page, "cat": cat_page, "online": online_page, "stub": stub_page, "article": article, "apply": apply_page}[k](i, path, info)
                txt = page(i, hl, path, info, body.replace("%A%", ""), "inner")
            out = os.path.join(ROOT, folder, path)
            os.makedirs(out, exist_ok=True)
            with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
                f.write(txt)
            n += 1
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_INDEX)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("built %d pages (%d per language)" % (n, len(PAGES)))


if __name__ == "__main__":
    main()
