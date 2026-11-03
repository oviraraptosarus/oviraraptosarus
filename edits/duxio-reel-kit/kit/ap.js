/* ap: Apple style element world (the look of the owner's liked 59s reel): Inter + Instrument Serif italic highlights in a violet gradient,
   glass cards, iOS notifications, a call screen, toggles, calendar, lock screen. Each slide = a headline + one built element.
   Icons: Feather (MIT). Slide: {c0, eye, hl:[lines], hc:[cue per line], gr:"red", plain, flash, x:"call", xc:[cues], props:{...}}.
   *word* = Instrument Serif italic highlight (violet gradient, red with gr:"red"). All motion is seek safe (no timers, no tl.call).
   Every element reads its words from `props` (P) and falls back to the defaults below, so one element serves any topic.
   Element catalog and cue meanings: kit/ELEMENTS.md. To add an element: one function E.name here + one entry in ap_sfx.json. */
const ICO = (d, s = 48, col = "#fff", w = 2.2) => `<svg viewBox="0 0 24 24" width="${s}" height="${s}" fill="none" stroke="${col}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round">${d}</svg>`;
const PATH = {
  send: '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
  mail: '<path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><polyline points="22,6 12,13 2,6"/>',
  form: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
  bell: '<path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/>',
  check: '<polyline points="20 6 9 17 4 12"/>',
  x: '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
  moon: '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
  play: '<polygon points="6 3 20 12 6 21 6 3"/>',
  cal: '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
  phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
  msg: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
  link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
  user: '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
  star: '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
  heart: '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
  trend: '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
  dollar: '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
};
const ab = (p, css, html, cls) => $(p, cls || "", "position:absolute;" + css, html);
const gl = (p, css) => $(p, "ap-glass", css);
const IN = (tl, e, t, from = {}, to = {}) => tl.fromTo(e, { opacity: 0, y: 44, scale: 0.94, ...from }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "back.out(1.4)", ...to }, t);
const XF = (tl, a, b, t) => { tl.to(a, { opacity: 0, duration: 0.15 }, t); tl.fromTo(b, { opacity: 0 }, { opacity: 1, duration: 0.2 }, t + 0.05); };
const ACC = "var(--acc,#7300f0)", ACC2 = "var(--acc2,#a66bff)", GRAD = `linear-gradient(140deg,${ACC2},${ACC})`;
const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const E = {};

E.call = (tl, inn, X, END, P) => {
  const card = gl(inn, "left:150px;top:690px;width:780px;height:640px;border-radius:52px;overflow:hidden;background:linear-gradient(170deg,#24222e,#121118)");
  const rings = [0, 1].map(() => ab(card, "left:290px;top:110px;width:200px;height:200px;border-radius:50%;border:4px solid #b98cff;opacity:0"));
  const av = ab(card, "left:290px;top:110px;width:200px;height:200px;border-radius:50%;background:linear-gradient(140deg,#5a5a68,#2c2c36);display:flex;align-items:center;justify-content:center;font-size:104px;font-weight:300;color:#d6d6de", esc(P.glyph ?? "?"));
  ab(card, "left:0;top:340px;width:780px;text-align:center;font-size:46px;font-weight:700;letter-spacing:-.02em", esc(P.name ?? "Cold lead"));
  const s1 = ab(card, "left:0;top:404px;width:780px;text-align:center;font-size:32px;font-weight:550;color:#a1a1aa", esc(P.sub ?? "calling…"));
  const s2 = ab(card, "left:0;top:404px;width:780px;text-align:center;font-size:32px;font-weight:650;color:#ff453a;opacity:0", esc(P.sub2 ?? "Call declined"));
  const dec = ab(card, "left:208px;top:490px;width:116px;height:116px;border-radius:50%;background:#ff453a;display:flex;align-items:center;justify-content:center", ICO(PATH.x, 54));
  const acc = ab(card, "left:456px;top:490px;width:116px;height:116px;border-radius:50%;background:#30d158;display:flex;align-items:center;justify-content:center", ICO(PATH.phone, 54));
  IN(tl, card, X(0));
  for (let t = X(0) + 0.25; t < X(1) - 0.2; t += 0.85) rings.forEach((r, i) => tl.fromTo(r, { scale: 0.9, opacity: 0.7 }, { scale: 1.7, opacity: 0, duration: 0.9, ease: "power2.out" }, t + i * 0.28));
  tl.to(dec, { scale: 0.86, duration: 0.09, yoyo: true, repeat: 1, ease: "power2.out" }, X(1));
  tl.to(acc, { opacity: 0.25, duration: 0.2 }, X(1));
  tl.to(av, { opacity: 0.4, duration: 0.25 }, X(1) + 0.05);
  XF(tl, s1, s2, X(1) + 0.05);
  tl.to(card, { x: -14, duration: 0.05, yoyo: true, repeat: 3, ease: "sine.inOut" }, X(1) + 0.12);
};

E.notifs = (tl, inn, X, END, P) => {
  const rows = P.rows ?? [["send", "Instagram", "Maya R.", "Hey! Is your coaching program still open?"], ["form", "Form", "Daniel K.", "I'd like to know more about 1:1 coaching."], ["mail", "Mail", "Priya S.", "Do you have a spot open this month?"]];
  rows.forEach((r, i) => {
    const c = gl(inn, `left:110px;top:${640 + i * 228}px;width:860px;height:204px;border-radius:48px`);
    ab(c, `left:36px;top:36px;width:84px;height:84px;border-radius:24px;background:${GRAD};display:flex;align-items:center;justify-content:center`, ICO(PATH[r[0]] ?? PATH.send, 42));
    ab(c, "left:148px;top:30px;right:40px;display:flex;justify-content:space-between;font-size:28px;font-weight:600;color:#c7c7cf", `<span>${esc(r[1])}</span><span>${esc(P.when ?? "now")}</span>`);
    ab(c, "left:148px;top:74px;font-size:36px;font-weight:700;letter-spacing:-.02em", esc(r[2]));
    ab(c, "left:148px;top:122px;width:670px;font-size:32px;font-weight:450;color:#e9e9ee;letter-spacing:-.015em;white-space:nowrap", esc(r[3]));
    ab(c, "right:40px;top:104px;width:20px;height:20px;border-radius:50%;background:#9b5cff");
    IN(tl, c, X(i), { y: -70, scale: 0.92 });
  });
  IN(tl, ab(inn, "left:0;top:1338px;width:1080px;text-align:center;font-size:26px;font-weight:600;color:#8e8e98;letter-spacing:.12em", esc(P.tag ?? "EXAMPLE")), X(rows.length - 1) + 0.2, { y: 10 });
};

E.age = (tl, inn, X, END, P) => {
  const c = gl(inn, "left:110px;top:760px;width:860px;height:244px;border-radius:52px");
  ab(c, `left:44px;top:44px;width:96px;height:96px;border-radius:26px;background:${GRAD};display:flex;align-items:center;justify-content:center`, ICO(PATH[P.icon ?? "send"], 48));
  ab(c, "left:168px;top:40px;font-size:30px;font-weight:600;color:#c7c7cf", esc(P.app ?? "Instagram"));
  const ts = P.times ?? ["now", "2 min ago", "1 h ago", "8 h ago", "2 days ago"];
  const times = ts.map((t, i) => ab(c, `right:46px;top:40px;font-size:30px;font-weight:${i === ts.length - 1 ? 700 : 600};color:${i === ts.length - 1 ? "#ff453a" : "#c7c7cf"};opacity:${i ? 0 : 1}`, esc(t)));
  ab(c, "left:168px;top:86px;font-size:38px;font-weight:700;letter-spacing:-.02em", esc(P.name ?? "Maya R."));
  ab(c, "left:168px;top:138px;width:640px;font-size:36px;font-weight:450;color:#e9e9ee;letter-spacing:-.015em;white-space:nowrap", esc(P.text ?? "Is your coaching program still open?"));
  const chip = gl(inn, "left:230px;top:1070px;width:620px;height:100px;border-radius:50px;display:flex;align-items:center;gap:18px;padding:0 34px;font-size:34px;font-weight:650");
  chip.innerHTML = ICO(PATH.cal, 38, "#c9adff") + `<span>${esc(P.chip ?? "You: with a client")}</span>`;
  IN(tl, c, X(0)); IN(tl, chip, X(0) + 0.15);
  for (let i = 1; i < ts.length; i++) XF(tl, times[i - 1], times[i], X(i));
  tl.to(c, { opacity: 0.5, filter: "grayscale(1)", duration: X(ts.length - 1) - X(0), ease: "none" }, X(0) + 0.2);
};

E.chat = (tl, inn, X, END, P) => {
  const RC = 2 * Math.PI * 105;
  const ring = ab(inn, "left:420px;top:640px;width:240px;height:240px", `<svg width="240" height="240" viewBox="0 0 240 240"><circle cx="120" cy="120" r="105" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="14"/><circle class="arc" cx="120" cy="120" r="105" fill="none" stroke="#9b5cff" stroke-width="14" stroke-linecap="round" transform="rotate(-90 120 120)" stroke-dasharray="${RC}" stroke-dashoffset="${RC}"/></svg>`);
  ab(ring, "left:0;top:64px;width:240px;text-align:center;font-size:86px;font-weight:250;letter-spacing:-.05em;line-height:1", esc(P.num ?? "60"));
  ab(ring, "left:0;top:152px;width:240px;text-align:center;font-size:26px;font-weight:600;color:#a1a1aa", esc(P.unit ?? "seconds"));
  const chip = ab(inn, "left:0;top:912px;width:1080px;display:flex;justify-content:center");
  const ok = $(chip, "", "display:flex;align-items:center;gap:12px;height:62px;border-radius:31px;padding:0 24px 0 18px;font-size:28px;font-weight:700;background:#30d158;color:#06210f", ICO(PATH.check, 28, "#06210f", 3) + esc(P.done ?? "Replied"));
  const b1 = ab(inn, "left:90px;top:1010px;max-width:640px;padding:26px 34px;border-radius:44px;border-bottom-left-radius:14px;font-size:38px;line-height:1.28;font-weight:480;letter-spacing:-.015em;background:#26262d;color:#f2f2f5", esc(P.inText ?? "Hey! Is your coaching program still open?"));
  const b2 = ab(inn, "right:90px;top:1190px;max-width:640px;padding:26px 34px;border-radius:44px;border-bottom-right-radius:14px;font-size:38px;line-height:1.28;font-weight:480;letter-spacing:-.015em;background:linear-gradient(140deg,#8a3dff,#6a00e0);color:#fff", esc(P.outText ?? "Hi Maya! Yes, we are. What are you hoping to work on?"));
  const ex = ab(inn, "left:0;top:984px;width:1080px;text-align:center;font-size:24px;font-weight:600;color:#8e8e98;letter-spacing:.12em", esc(P.tag ?? "EXAMPLE"));
  IN(tl, ring, X(0)); IN(tl, ex, X(0) + 0.2, { y: 8 }); IN(tl, b1, X(0) + 0.3, { y: 30, x: -30, transformOrigin: "0% 100%" });
  tl.to(ring.querySelector(".arc"), { attr: { "stroke-dashoffset": RC * (P.arcLeft ?? 0.32) }, duration: X(2) - X(1), ease: "power1.inOut" }, X(1));
  IN(tl, b2, X(2), { y: 30, x: 30, transformOrigin: "100% 100%" }); IN(tl, ok, X(3), { y: 10, scale: 0.8 });
};

E.qual = (tl, inn, X, END, P) => {
  const av = ab(inn, "left:465px;top:660px;width:150px;height:150px;border-radius:50%;background:linear-gradient(140deg,#ff7aa8,#c2185b);display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:700", esc(P.letter ?? "M"));
  const ring = ab(inn, "left:453px;top:648px;width:174px;height:174px;border-radius:50%;border:6px solid #b98cff");
  IN(tl, av, X(0), { y: 20 }); IN(tl, ring, X(0) + 0.05, { y: 20 });
  (P.questions ?? ["What's your goal?", "Where are you stuck?", "When do you want to start?"]).forEach((q, i) => {
    const row = ab(inn, `left:90px;width:900px;top:${870 + i * 92}px;display:flex;justify-content:center`);
    const chip = $(row, "ap-glass", "position:relative;height:76px;border-radius:38px;padding:0 22px 0 30px;display:flex;align-items:center;gap:18px;font-size:32px;font-weight:650;color:#e9e9ee");
    chip.innerHTML = `<span>${esc(q)}</span>`;
    const tick = $(chip, "", "width:44px;height:44px;border-radius:50%;background:#30d158;display:flex;align-items:center;justify-content:center", ICO(PATH.check, 26, "#06210f", 3.4));
    IN(tl, chip, X(1 + i), { y: 24, scale: 0.92 }, { duration: 0.4 });
    tl.fromTo(tick, { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.4)" }, X(1 + i) + 0.35);
  });
  const badge = ab(inn, "left:0;top:1170px;width:1080px;display:flex;justify-content:center");
  const bd = $(badge, "", "display:flex;align-items:center;gap:12px;height:66px;border-radius:33px;padding:0 28px 0 20px;font-size:30px;font-weight:700;background:rgba(48,209,88,.16);color:#5ee07f", ICO(PATH.check, 28, "#5ee07f", 3) + esc(P.badge ?? "Serious buyer"));
  tl.to(ring, { borderColor: "#30d158", duration: 0.25 }, X(4)); IN(tl, bd, X(4), { y: 14, scale: 0.85 });
  const sms = ab(inn, "left:90px;top:1252px;width:900px;height:176px;border-radius:46px;padding:30px 40px 0 150px;background:rgba(245,245,247,.96);color:#1d1d1f");
  ab(sms, "left:38px;top:34px;width:84px;height:84px;border-radius:22px;background:linear-gradient(180deg,#5df27a,#28c840);display:flex;align-items:center;justify-content:center", ICO(PATH.msg, 44, "#fff", 2.4));
  ab(sms, "left:150px;top:28px;right:40px;display:flex;justify-content:space-between;font-size:26px;font-weight:600;color:#6e6e73", `<span>${esc(P.smsApp ?? "Text message")}</span><span>now</span>`);
  ab(sms, "left:150px;top:70px;font-size:36px;font-weight:650;letter-spacing:-.02em", esc(P.sms ?? "Maya looks ready to talk."));
  IN(tl, sms, X(5), { y: -60, scale: 0.94 });
};

E.cal = (tl, inn, X, END, P) => {
  const c = gl(inn, "left:110px;top:660px;width:860px;height:250px;border-radius:46px;display:flex;align-items:center;gap:36px;padding:0 40px");
  c.innerHTML = `<div style="width:150px;height:166px;border-radius:30px;background:#f5f5f7;color:#1d1d1f;overflow:hidden;flex:none;text-align:center"><b style="display:block;background:#ff453a;color:#fff;font-size:28px;font-weight:700;letter-spacing:.08em;padding:10px 0">${esc(P.day ?? "TUE")}</b><span style="display:block;font-size:84px;font-weight:600;letter-spacing:-.04em;line-height:1.3">${esc(P.date ?? "14")}</span></div><div><div style="font-size:44px;font-weight:700;letter-spacing:-.025em">${esc(P.title ?? "Strategy Call")}</div><div style="font-size:32px;font-weight:500;color:#a1a1aa;margin-top:6px">${esc(P.sub ?? "10:00 AM · Example")}</div></div>`;
  const bk = ab(c, "right:34px;top:30px;height:58px;border-radius:29px;padding:0 22px;display:flex;align-items:center;gap:10px;font-size:28px;font-weight:700;background:#30d158;color:#06210f", ICO(PATH.check, 26, "#06210f", 3.2) + esc(P.badge ?? "Booked"));
  IN(tl, c, X(0)); IN(tl, bk, X(0) + 0.35, { y: 0, scale: 0.7 });
  (P.reminders ?? ["24 hours before", "2 hours before", "10 minutes before"]).forEach((t, i) => {
    const r = gl(inn, `left:190px;top:${990 + i * 126}px;height:104px;border-radius:52px;display:flex;align-items:center;gap:22px;padding:0 40px 0 22px;font-size:40px;font-weight:650;letter-spacing:-.02em`);
    const bell = $(r, "", `width:66px;height:66px;border-radius:50%;background:${ACC};display:flex;align-items:center;justify-content:center;flex:none`, ICO(PATH.bell, 36));
    $(r, "", "", esc(t));
    IN(tl, r, X(1 + i), { x: -40, y: 10 });
    tl.fromTo(bell, { rotation: -16 }, { rotation: 0, duration: 0.5, ease: "elastic.out(1,.35)" }, X(1 + i) + 0.2);
  });
};

E.typing = (tl, inn, X, END, P) => {
  const q = ab(inn, "left:90px;top:640px;width:900px;text-align:center;font-family:var(--fs,'Instrument Serif'),serif;font-style:italic;font-size:760px;line-height:1;color:rgba(255,255,255,.06);height:760px;overflow:hidden", esc(P.glyph ?? "?"));
  tl.fromTo(q, { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }, X(0));
  const b = gl(inn, "left:260px;top:900px;width:560px;height:220px;border-radius:110px");
  const dots = [0, 1, 2].map((i) => ab(b, `left:${130 + i * 120}px;top:76px;width:68px;height:68px;border-radius:50%;background:#8e8e98`));
  IN(tl, b, X(0), { scale: 0.7 });
  for (let t = X(0) + 0.4; t < END - 0.5; t += 0.6) dots.forEach((d, i) => { tl.to(d, { y: -26, backgroundColor: "#e4e4ec", duration: 0.2, ease: "sine.out" }, t + i * 0.13); tl.to(d, { y: 0, backgroundColor: "#8e8e98", duration: 0.22, ease: "sine.in" }, t + i * 0.13 + 0.2); });
};

E.appr = (tl, inn, X, END, P) => {
  const c = gl(inn, "left:110px;top:660px;width:860px;height:150px;border-radius:50px;display:flex;align-items:center;justify-content:space-between;padding:0 44px 0 40px;font-size:38px;font-weight:650;letter-spacing:-.02em");
  c.innerHTML = `<span style="display:flex;align-items:center;gap:20px">${ICO(PATH.user, 40, "#c9adff")}${esc(P.label ?? "Approve before sending")}</span>`;
  const sw = $(c, "", "position:relative;width:104px;height:60px;border-radius:30px;background:#3a3a44;flex:none");
  const on = $(sw, "", "position:absolute;inset:0;border-radius:30px;background:#30d158;opacity:0"), kn = $(sw, "", "position:absolute;left:4px;top:4px;width:52px;height:52px;border-radius:50%;background:#fff");
  IN(tl, c, X(0));
  tl.to(on, { opacity: 1, duration: 0.2 }, X(1)); tl.to(kn, { x: 44, duration: 0.25, ease: "back.out(1.6)" }, X(1));
  const b = ab(inn, "right:110px;top:900px;max-width:660px;padding:30px 38px;border-radius:48px;border-bottom-right-radius:14px;font-size:40px;line-height:1.28;font-weight:480;letter-spacing:-.015em;background:linear-gradient(140deg,#8a3dff,#6a00e0);color:#fff", esc(P.draft ?? "Hi Maya! Yes, we are open. What are you hoping to work on?"));
  const lab = ab(inn, "left:0;top:1160px;width:1080px;display:flex;justify-content:center");
  $(lab, "", "display:flex;align-items:center;gap:12px;font-size:30px;font-weight:650;color:#c7c7cf", ICO(PATH.check, 28, "#30d158", 3) + esc(P.note ?? "Written in your voice"));
  IN(tl, b, X(2), { x: 30, y: 30, transformOrigin: "100% 100%" }); IN(tl, lab, X(3), { y: 10 });
};

E.badge = (tl, inn, X, END, P) => {
  const ic = ab(inn, "left:425px;top:680px;width:230px;height:230px;border-radius:58px;background:linear-gradient(180deg,#5df27a,#28c840);display:flex;align-items:center;justify-content:center", ICO(PATH[P.icon ?? "msg"], 110, "#fff", 2));
  const bd = ab(inn, "left:560px;top:650px;min-width:96px;height:96px;border-radius:48px;padding:0 24px;background:#ff453a;display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:700;letter-spacing:-.03em;font-variant-numeric:tabular-nums;box-shadow:0 0 0 8px #07060b", "1");
  const cnt = { n: 1 };
  IN(tl, ic, X(0), { y: 30 }); IN(tl, bd, X(0) + 0.25, { y: 0, scale: 0.2 });
  tl.to(cnt, { n: P.count ?? 27, duration: X(2) - X(0) - 0.1, ease: "power1.in", onUpdate: () => { bd.textContent = Math.round(cnt.n); } }, X(0) + 0.5);
  IN(tl, ab(inn, "left:0;top:960px;width:1080px;text-align:center;font-size:30px;font-weight:600;color:#a1a1aa", esc(P.caption ?? "Unread messages · Example")), X(0) + 0.3, { y: 10 });
  const chip = gl(inn, "left:230px;top:1090px;width:620px;height:100px;border-radius:50px;display:flex;align-items:center;gap:18px;padding:0 34px;font-size:34px;font-weight:650");
  chip.innerHTML = ICO(PATH.cal, 38, "#c9adff") + `<span>${esc(P.chip ?? "You: with a client")}</span>`;
  IN(tl, chip, X(1));
};

E.lock = (tl, inn, X, END, P) => {
  const moon = ab(inn, "left:0;top:585px;width:1080px;display:flex;justify-content:center;align-items:center;gap:14px;font-size:30px;font-weight:600;color:#a1a1aa", ICO(PATH.moon, 34, "#a1a1aa") + esc(P.mode ?? "Sleep"));
  const tm = ab(inn, "left:0;top:640px;width:1080px;text-align:center;font-size:300px;font-weight:250;letter-spacing:-.07em;line-height:1;font-variant-numeric:tabular-nums", esc(P.time ?? "2:04"));
  IN(tl, moon, X(0), { y: 10 }); IN(tl, tm, X(0) + 0.1, { y: 30, scale: 0.97 });
  const n = gl(inn, "left:110px;top:990px;width:860px;height:180px;border-radius:46px");
  ab(n, `left:36px;top:34px;width:84px;height:84px;border-radius:24px;background:${GRAD};display:flex;align-items:center;justify-content:center`, ICO(PATH.send, 42));
  ab(n, "left:148px;top:26px;right:40px;display:flex;justify-content:space-between;font-size:26px;font-weight:600;color:#c7c7cf", `<span>${esc(P.app ?? "DUXIO")}</span><span>now</span>`);
  ab(n, "left:148px;top:66px;font-size:36px;font-weight:700;letter-spacing:-.02em", esc(P.title ?? "Reply sent to Maya R."));
  ab(n, "left:148px;top:116px;font-size:30px;font-weight:450;color:#c7c7cf", esc(P.body ?? "In your voice. Approved by you."));
  IN(tl, n, X(1), { y: -50 });
  ab(inn, "left:0;top:1196px;width:1080px;text-align:center;font-size:26px;font-weight:650;letter-spacing:.14em;color:#a1a1aa", esc(P.caption ?? "21 DAYS OF FOLLOW UP"));
  const grid = ab(inn, "left:0;top:1246px;width:1080px;display:flex;justify-content:center");
  const wrap = $(grid, "", "display:grid;grid-template-columns:repeat(7,40px);gap:18px 20px");
  const N = P.dots ?? 21;
  for (let i = 0; i < N; i++) {
    const d = $(wrap, "", "width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.1)"), f = $(d, "", `width:100%;height:100%;border-radius:50%;background:linear-gradient(140deg,#c9adff,${ACC})`);
    tl.fromTo(f, { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.2)" }, X(2) + (i / N) * (X(3) - X(2)));
  }
};

E.notready = (tl, inn, X, END, P) => {
  const av = ab(inn, "left:440px;top:650px;width:200px;height:200px;border-radius:50%;background:linear-gradient(140deg,#5a5a68,#2c2c36);display:flex;align-items:center;justify-content:center;font-size:80px;font-weight:700;color:#d6d6de", esc(P.letter ?? "M"));
  const ring = ab(inn, "left:422px;top:632px;width:236px;height:236px;border-radius:50%;border:5px dashed rgba(255,255,255,.35)");
  IN(tl, av, X(0), { y: 20 }); IN(tl, ring, X(0) + 0.05, { y: 20 });
  tl.to(ring, { rotation: 360, duration: END - X(0), ease: "none" }, X(0));
  const chip = gl(inn, "left:330px;top:930px;width:420px;height:92px;border-radius:46px;display:flex;align-items:center;justify-content:center;gap:14px;font-size:34px;font-weight:650");
  chip.innerHTML = ICO(PATH.cal, 36, "#c9adff") + `<span>${esc(P.chip ?? "Not ready yet")}</span>`;
  IN(tl, chip, X(1));
};

E.route = (tl, inn, X, END, P) => {
  (P.cards ?? [["play", "Not ready", "Pointed to your content"], ["cal", "Quiet lead", "A human check in, every month"]]).forEach((r, i) => {
    const c = gl(inn, `left:110px;top:${700 + i * 260}px;width:860px;height:210px;border-radius:50px`);
    ab(c, `left:40px;top:60px;width:90px;height:90px;border-radius:26px;background:${GRAD};display:flex;align-items:center;justify-content:center`, ICO(PATH[r[0]] ?? PATH.play, 44));
    ab(c, "left:162px;top:48px;font-size:28px;font-weight:650;letter-spacing:.1em;color:#a1a1aa;text-transform:uppercase", esc(r[1]));
    ab(c, "left:162px;top:92px;width:520px;font-size:40px;font-weight:700;letter-spacing:-.025em;line-height:1.1", esc(r[2]));
    IN(tl, c, X(i), { x: i ? 40 : -40, y: 20 });
    if (i && P.ping !== false) {
      const p = ab(c, "right:44px;top:58px;width:90px;height:90px;border-radius:50%;border:5px solid #b98cff;opacity:0");
      const d = ab(c, "right:44px;top:58px;width:90px;height:90px;border-radius:50%;background:linear-gradient(140deg,#ff7aa8,#c2185b);display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700", esc(P.letter ?? "M"));
      IN(tl, d, X(i) + 0.3, { y: 0, scale: 0.4 });
      tl.fromTo(p, { scale: 0.9, opacity: 0.9 }, { scale: 1.9, opacity: 0, duration: 0.9, ease: "power2.out", repeat: 1, repeatDelay: 0.1 }, X(i) + 0.6);
    }
  });
};

E.report = (tl, inn, X, END, P) => {
  const c = ab(inn, "left:130px;top:640px;width:820px;height:640px;border-radius:48px;padding:44px 48px;background:linear-gradient(180deg,#1b1a22,#131219);border:1.5px solid rgba(255,255,255,.12);box-shadow:0 60px 110px -40px rgba(0,0,0,.9)");
  ab(c, "left:48px;top:44px;right:48px;display:flex;justify-content:space-between;align-items:baseline;font-size:46px;font-weight:750;letter-spacing:-.03em", `<span>${esc(P.title ?? "This week")}</span><span style="font-size:28px;font-weight:550;color:#a1a1aa;letter-spacing:0">${esc(P.tag ?? "Example")}</span>`);
  IN(tl, c, X(0));
  (P.rows ?? [["Leads answered", 0.96], ["Serious buyers", 0.62], ["Calls booked", 0.48], ["Paying clients", 0.34]]).forEach((r, i) => {
    const row = ab(c, `left:48px;top:${150 + i * 108}px;width:724px;height:84px`);
    ab(row, "left:0;top:0;font-size:32px;font-weight:600;color:#d8d8de", esc(r[0]));
    ab(row, "left:0;top:50px;width:724px;height:14px;border-radius:7px;background:rgba(255,255,255,.08)");
    const f = ab(row, `left:0;top:50px;width:${724 * r[1]}px;height:14px;border-radius:7px;background:linear-gradient(90deg,${ACC},#b98cff);transform-origin:0 50%`);
    tl.fromTo(f, { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: "power3.out" }, X(1) + i * 0.18);
  });
};

E.handset = (tl, inn, X, END, P) => {
  const hs = ab(inn, "left:390px;top:700px;width:300px;height:300px", `<svg viewBox="0 0 24 24" width="300" height="300"><path fill="${P.color ?? "#ff453a"}" d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>`);
  IN(tl, hs, X(0), { scale: 0.7 });
  for (let t = X(0) + 0.3; t < X(1) - 0.2; t += 0.5) for (let k = 0; k < 4; k++) tl.to(hs, { rotation: k % 2 ? 10 : -10, duration: 0.06, ease: "sine.inOut" }, t + k * 0.06);
  const sl = ab(inn, "left:180px;top:848px;width:720px;height:14px;border-radius:7px;background:#ff453a;transform-origin:0 50%;transform:rotate(-24deg)");
  tl.fromTo(sl, { scaleX: 0 }, { scaleX: 1, duration: 0.25, ease: "power3.out" }, X(1));
  tl.to(hs, { rotation: 0, opacity: 0.55, duration: 0.2 }, X(1));
};

E.logo = (tl, inn, X, END, P) => {
  const lg = ab(inn, "left:219px;top:760px;width:642px;height:120px", `<img src="${P.logo ?? "assets/duxio-wordmark-white.svg"}" style="position:absolute;left:0;top:0;width:642px;height:120px">`);
  tl.fromTo(lg, { opacity: 0, scale: 0.9, y: 20 }, { opacity: 1, scale: 1, y: 0, duration: 0.5, ease: "power3.out" }, X(0));
  const w = ab(inn, "left:0;top:930px;width:1080px;text-align:center;font-family:var(--fs,'Instrument Serif'),serif;font-style:italic;font-size:230px;line-height:1.1;letter-spacing:-.02em;color:#fff;overflow:hidden;height:300px");
  const i = $(w, "", "display:inline-block", esc(P.word ?? "answers."));
  tl.fromTo(i, { yPercent: 110 }, { yPercent: 0, duration: 0.5, ease: "power4.out" }, X(1));
};

E.cta = (tl, inn, X, END, P) => {
  const b = ab(inn, "left:110px;top:760px;width:860px;height:170px;border-radius:85px;background:linear-gradient(140deg,#8a3dff,#7300f0);box-shadow:0 40px 90px -30px rgba(115,0,240,.9);display:flex;align-items:center;justify-content:center;gap:24px;font-size:60px;font-weight:720;letter-spacing:-.03em;color:#fff;overflow:hidden", ICO(PATH[P.icon ?? "link"] ?? PATH.link, 56) + `<span>${esc(P.label ?? "Link in bio")}</span>`);
  const tap = $(b, "", "position:absolute;left:600px;top:25px;width:120px;height:120px;border-radius:50%;background:rgba(255,255,255,.55);opacity:0");
  IN(tl, b, X(0), { scale: 0.88 });
  tl.fromTo(tap, { scale: 0.4, opacity: 0.9 }, { scale: 1.6, opacity: 0, duration: 0.7, ease: "power2.out" }, X(1));
  tl.to(b, { scale: 0.96, duration: 0.1, yoyo: true, repeat: 1, ease: "power2.out" }, X(1));
};

S.ap = (c) => {
  const { tl, el, props: p } = c, T = (k) => c.cue(k), END = c.end, N = p.slides.length;
  const bg = $(el, "ap-bg"), b1 = $(bg, "ap-blob", "left:-420px;top:-260px;width:1400px;height:1400px;background:radial-gradient(closest-side,rgba(115,0,240,.5),rgba(115,0,240,0))");
  const b2 = $(bg, "ap-blob", "left:240px;top:900px;width:1300px;height:1300px;background:radial-gradient(closest-side,rgba(80,40,220,.38),rgba(80,40,220,0))");
  const b3 = $(bg, "ap-blob", "left:-300px;top:1250px;width:1000px;height:1000px;background:radial-gradient(closest-side,rgba(190,90,255,.2),rgba(190,90,255,0))");
  tl.fromTo(b1, { x: 0, y: 0 }, { x: 160, y: 120, duration: END, ease: "none" }, 0);
  tl.fromTo(b2, { x: 0, y: 0 }, { x: -200, y: -140, duration: END, ease: "none" }, 0);
  tl.fromTo(b3, { x: 0 }, { x: 180, duration: END, ease: "none" }, 0);
  const st = p.slides.map((s) => T(s.c0) - 0.08);
  p.slides.forEach((s, si) => {
    const t0 = si === 0 ? 0 : st[si], t1 = si + 1 < N ? st[si + 1] : END;
    const sl = $(el, "ap-sl"), inn = $(sl, "ap-in");
    tl.set(sl, { visibility: "visible" }, t0); tl.set(sl, { visibility: "hidden" }, t1 + 0.01);
    if (s.flash) { const f = $(sl, "ap-flash"); tl.fromTo(f, { opacity: 0 }, { opacity: 1, duration: 0.3 }, t0); inn.style.zIndex = 2; }
    if (si > 0) tl.fromTo(sl, { opacity: 0, scale: 1.03, filter: "blur(10px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.32, ease: "power3.out" }, t0);
    if (si + 1 < N) tl.to(sl, { opacity: 0, scale: 0.97, filter: "blur(8px)", duration: 0.18, ease: "power2.in" }, t1 - 0.16);
    tl.fromTo(inn, { scale: 1, y: 0 }, { scale: 1.035, y: -12, duration: t1 - t0, ease: "none", transformOrigin: "50% 50%" }, t0);
    if (s.eye) { const e = $(inn, "ap-eye", "top:262px", esc(s.eye)); tl.fromTo(e, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.35, ease: EASE }, t0 + 0.05); }
    if (s.hl && s.hl.length) {
      const hl = $(inn, "ap-hl", `top:${s.top ?? 330}px${s.fs ? ";font-size:" + s.fs + "px" : ""}`);
      s.hl.forEach((ln, li) => {
        const row = $(hl, "ln"), t = T(s.hc[li]);
        const ws = ln.split(" ");
        ws.forEach((w, wi) => {
          if (wi) row.appendChild(document.createTextNode(" "));
          const em = w.startsWith("*") && w.endsWith("*"), m = $(row, "ap-mw"), i = $(m, em ? "ap-it gr" + (s.gr === "red" ? " red" : "") : "", "", esc(em ? w.slice(1, -1) : w));
          if (s.plain && em) { i.className = "ap-it"; i.style.color = "#fff"; }
          tl.fromTo(i, rise, { yPercent: 0, duration: 0.5, ease: EASE }, t + wi * 0.06);
        });
      });
    }
    if (s.x) {
      if (!E[s.x]) throw new Error("unknown ap element: " + s.x);
      E[s.x](tl, inn, (k) => T(s.xc[k]), t1, s.props || {});
    }
  });
  tl.fromTo($(el, "grain"), { backgroundPosition: "0px 0px" }, { backgroundPosition: "480px 360px", duration: END, ease: "steps(240)" }, 0);
  $(el, "vig");
};
