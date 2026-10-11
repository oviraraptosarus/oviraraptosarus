/* DUXIO reel kit: scene library. Every scene is a function (ctx) that builds DOM inside ctx.el and adds tweens
   to the master timeline ctx.tl at ABSOLUTE times. Cues come pre-resolved from the build (ctx.cue(i) in seconds).
   Seek-safe: no timers, no random at runtime, counters tween a proxy object. */
const S = {};
const $ = (p, c, css, html) => { const e = document.createElement("div"); if (c) e.className = c; if (css) e.style.cssText = css; if (html != null) e.innerHTML = html; p.appendChild(e); return e; };
const rise = { yPercent: 118 };
const EASE = "power4.out", POP = "back.out(1.7)";

/* statement: props {lines:["Four *sentences*","two apologies"], size:120, top:760, color}  *x* = accent serif word
   cue0 = reveal, cue1 (optional) = second line group starts at that time */
S.statement = (c) => {
  const { tl, el, props: p } = c, size = p.size || 124;
  const box = $(el, "stmt", `top:${p.top ?? 700}px;font-size:${size}px;${p.color ? "color:" + p.color : ""}`);
  p.lines.forEach((ln, li) => {
    const row = $(box, "line");
    const t0 = c.cue(li) ?? c.cue(0) + li * 0.32;
    ln.split(" ").forEach((w, wi) => {
      const em = w.startsWith("*") && w.endsWith("*"); const txt = em ? w.slice(1, -1) : w;
      const m = $(row, "mk"), i = $(m, em ? "serif red" : "", em ? `font-size:${size * 1.12}px` : "", txt);
      tl.fromTo(i, rise, { yPercent: 0, duration: 0.5, ease: EASE }, t0 + wi * 0.07);
    });
  });
};

/* stack: props {items:["Four sentences","Two apologies","Send"], top:520, gap:150, last:"red"}  item i at cue i */
S.stack = (c) => {
  const { tl, el, props: p } = c;
  p.items.forEach((t, i) => {
    const r = $(el, "row", `top:${(p.top ?? 520) + i * (p.gap ?? 150)}px`);
    $(r, "n", "", String(i + 1)); const mk = $(r, "mk"); const ti = $(mk, "t", `${p.last === "red" && i === p.items.length - 1 ? "color:var(--red)" : ""}`, t);
    tl.fromTo(r, { opacity: 0 }, { opacity: 1, duration: 0.01 }, c.cue(i));
    tl.fromTo(ti, rise, { yPercent: 0, duration: 0.45, ease: EASE }, c.cue(i));
  });
};

/* clock: props {from:127, to:470 (minutes after midnight), ampm:true, top:620, size:380, bgFrom:"#0D0E12", bgTo:"#F3F0EA", ink:"#fff", inkTo:"#111113"}
   cue0 = roll start, cue1 = roll end */
S.clock = (c) => {
  const { tl, el, props: p } = c, o = { m: p.from };
  const t = $(el, "clock", `top:${p.top ?? 620}px;font-size:${p.size ?? 380}px;color:${p.ink || "#fff"}`);
  const ap = $(el, "abs c", `left:0;width:1080px;top:${(p.top ?? 620) + (p.size ?? 380) + 30}px;font-size:84px;font-weight:700;letter-spacing:.06em;color:${p.ink || "#fff"};opacity:.6`);
  const fmt = () => { const mm = Math.round(o.m); const h24 = Math.floor(mm / 60) % 24, m = mm % 60; const h = h24 % 12 || 12; t.textContent = h + ":" + String(m).padStart(2, "0"); ap.textContent = h24 < 12 ? "AM" : "PM"; };
  fmt(); const t0 = c.cue(0), t1 = c.cue(1);
  tl.to(o, { m: p.to, duration: t1 - t0, ease: "power3.inOut", onUpdate: fmt }, t0);
  if (p.bgTo) { tl.fromTo(el, { backgroundColor: p.bgFrom }, { backgroundColor: p.bgTo, duration: t1 - t0, ease: "power2.inOut" }, t0);
    tl.fromTo([t, ap], { color: p.ink || "#fff" }, { color: p.inkTo || "#111113", duration: t1 - t0, ease: "power2.inOut" }, t0); }
};

/* msg: props {items:[{s:"me"|"them", t:"Hey, sorry for the late reply", meta:"2:11 AM"}], top:320, gap:...} item i at cue i
   Layout: stacked top-down; bubbles pop in. */
S.msg = (c) => {
  const { tl, el, props: p } = c; let y = p.top ?? 300;
  p.items.forEach((it, i) => {
    const long = it.t.length > 34, w = long ? 760 : null;
    const b = $(el, "bub " + it.s, `top:${y}px;${it.s === "me" ? "right" : "left"}:70px;${w ? "width:" + w + "px" : ""}`, it.t);
    const h = Math.ceil(it.t.length / (long ? 26 : 40)) * 62 + 68; y += h + (it.meta ? 64 : 26);
    tl.fromTo(b, { opacity: 0, scale: 0.86, y: 30, transformOrigin: it.s === "me" ? "100% 100%" : "0% 100%" }, { opacity: 1, scale: 1, y: 0, duration: 0.38, ease: POP }, c.cue(i));
    if (it.meta) { const m = $(el, "meta", `top:${y - 58}px;${it.s === "me" ? "right" : "left"}:90px`, it.meta); tl.fromTo(m, { opacity: 0 }, { opacity: 1, duration: 0.2 }, c.cue(i) + 0.25); }
  });
};

/* phone: dark phone screen with a composer that types then erases then types.
   props {time:"2:07 AM", battery:"14%", text:"Hey, so sorry for the late reply", ops:[[0,1.0],[0.35,0.5],[1,1.0]] (target fraction, seconds)} starts at cue0 */
S.phone = (c) => {
  const { tl, el, props: p } = c;
  const sc = $(el, "screen"); const sb = $(sc, "sb"); $(sb, "", "", p.time || "2:07 AM"); const bat = $(sb, "", "", p.battery || "14%");
  const comp = $(sc, "comp"); const txt = $(comp, "", "display:inline", ""); const car = $(comp, "caret", "display:inline-block");
  const o = { n: 0 }, full = p.text; const upd = () => { txt.textContent = full.slice(0, Math.round(o.n * full.length)); };
  upd(); let t = c.cue(0);
  (p.ops || [[1, 1.4]]).forEach(([to, d]) => { tl.to(o, { n: to, duration: d, ease: "none", onUpdate: upd }, t); t += d + 0.12; });
  tl.fromTo(car, { opacity: 1 }, { opacity: 0, duration: 0.01, repeat: 40, repeatDelay: 0.36, yoyo: true }, c.cue(0));
  if (p.battery2) tl.call(() => { bat.textContent = p.battery2; }, null, c.cue(1)), tl.call(() => { bat.textContent = p.battery || "14%"; }, null, 0);
  tl.fromTo(sc, { boxShadow: "0 0 160px 20px rgba(80,120,255,.12), inset 0 0 0 3px #1b1d24" }, { boxShadow: "0 0 240px 60px rgba(80,120,255,.32), inset 0 0 0 3px #1b1d24", duration: 1.2, repeat: 6, yoyo: true, ease: "sine.inOut" }, c.cue(0));
};

/* wall: a long apology text filling the frame, line by line. props {lines:[...], top:200, size:54}; cues: line i uses cue0 + i*step (step prop) */
S.wall = (c) => {
  const { tl, el, props: p } = c, size = p.size || 58; const t0 = c.cue(0), step = p.step ?? 0.26;
  p.lines.forEach((ln, i) => {
    const r = $(el, "abs", `left:80px;width:920px;top:${(p.top ?? 220) + i * (size * 1.5)}px;font-size:${size}px;font-weight:600;letter-spacing:-.01em;line-height:1.2;color:#e9ecf3;overflow:hidden;white-space:nowrap`);
    const i2 = $(r, "", "display:block", ln); tl.fromTo(i2, rise, { yPercent: 0, duration: 0.3, ease: EASE }, t0 + i * step);
  });
};

/* stamp: props {text:"SENT 2:11 AM", size:130, top:900, rot:-6}  hits at cue0 with a short shake of the whole scene */
S.stamp = (c) => {
  const { tl, el, props: p } = c, s = $(el, "stamp", `left:50%;top:${p.top ?? 900}px;font-size:${p.size ?? 130}px;margin-left:-0px`, p.text);
  s.style.transform = "translateX(-50%)"; const t = c.cue(0);
  tl.fromTo(s, { opacity: 0, scale: 3.4, rotation: p.rot ?? -6, xPercent: -50 }, { opacity: 1, scale: 1, rotation: p.rot ?? -6, xPercent: -50, duration: 0.2, ease: "power4.in" }, t - 0.2);
  [[6, 0.04], [-5, 0.04], [3, 0.04], [0, 0.05]].forEach(([x, d], i) => tl.to(el, { x, duration: d, ease: "none" }, t + i * 0.04));
};

/* dots: props {cols:6, rows:5, offs:[8,17,24,30], label:"still answering", top:380, size:96, gap:30}  at cue i, dots up to offs[i] go dark
   remaining count shown live (proxy) */
S.dots = (c) => {
  const { tl, el, props: p } = c, size = p.size || 96, gap = p.gap || 28, cols = p.cols || 6, rows = p.rows || 5, total = cols * rows;
  const w = cols * size + (cols - 1) * gap, x0 = (1080 - w) / 2, y0 = p.top ?? 380; const dots = [];
  for (let i = 0; i < total; i++) { const d = $(el, "dot", `left:${x0 + (i % cols) * (size + gap)}px;top:${y0 + Math.floor(i / cols) * (size + gap)}px;width:${size}px;height:${size}px;background:var(--red)`); dots.push(d); tl.fromTo(d, { scale: 0 }, { scale: 1, duration: 0.3, ease: POP }, c.cue(0) - 0.4 + (i % cols + Math.floor(i / cols)) * 0.035); }
  const num = $(el, "abs c", `left:0;width:1080px;top:${y0 + rows * (size + gap) + 30}px;font-size:200px;font-weight:800;letter-spacing:-.05em;color:var(--ink);height:220px`);
  const lab = $(el, "abs c", `left:0;width:1080px;top:${y0 + rows * (size + gap) + 250}px;font-size:56px;font-weight:700;color:var(--mute)`, p.label || "");
  const o = { n: total }; const upd = () => { num.textContent = Math.round(o.n); }; upd();
  (p.offs || []).forEach((k, i) => {
    const from = i === 0 ? 0 : p.offs[i - 1], t = c.cue(i);
    for (let j = from; j < k; j++) tl.to(dots[j], { backgroundColor: "#cfc9bf", scale: 0.78, duration: 0.18, ease: "power2.out" }, t + (j - from) * 0.045);
    tl.to(o, { n: total - k, duration: (k - from) * 0.045 + 0.1, ease: "none", onUpdate: upd }, t);
  });
};

/* chain: props {n:12, gapAt:7, top:900, bw:46, bh:210, labels:{0:"Day 1",...}}  cue0 = first block falls; blocks topple 0.09s apart; blocks after gapAt stay up */
S.chain = (c) => {
  const { tl, el, props: p } = c, n = p.n || 12, bw = p.bw || 46, bh = p.bh || 210, sp = (900 - bw) / (n - 1), top = p.top ?? 900, t0 = c.cue(0);
  for (let i = 0; i < n; i++) {
    const b = $(el, "blk", `left:${90 + i * sp}px;top:${top}px;width:${bw}px;height:${bh}px;background:${i > (p.gapAt ?? n) ? "#bdb7ad" : "var(--ink)"}`);
    tl.fromTo(b, { opacity: 0, y: -60 }, { opacity: 1, y: 0, duration: 0.25, ease: EASE }, c.cue(0) - 0.7 + i * 0.03);
    if (i <= (p.gapAt ?? n - 1)) tl.to(b, { rotation: 72, duration: 0.26, ease: "power2.in" }, t0 + i * 0.09);
  }
  if (p.caption) { const cp = $(el, "abs c", `left:60px;width:960px;top:${top + 380}px;font-size:84px;font-weight:800;letter-spacing:-.03em`, p.caption); tl.fromTo(cp, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: EASE }, c.cue(1) ?? t0 + n * 0.09); }
};

/* tier: props {rows:["S","A","B","C","D","F"], items:[{t:"Just checking in!", row:"F"}], top:300} item i drops in at cue i */
S.tier = (c) => {
  const { tl, el, props: p } = c, rows = p.rows || ["S", "A", "B", "C", "D", "F"];
  const cols = ["#111113", "#2b2b30", "#4a4a52", "#8a5560", "#c23a4a", "#F1283A"];
  rows.forEach((r, i) => { const t = $(el, "tier", `top:${(p.top ?? 300) + i * 170}px`); const b = document.createElement("b"); b.textContent = r; b.style.background = cols[i]; t.appendChild(b); $(t, "", ""); tl.fromTo(t, { xPercent: -110 }, { xPercent: 0, duration: 0.45, ease: EASE }, c.cue(0) - 0.6 + i * 0.05); });
  p.items.forEach((it, i) => { const ri = rows.indexOf(it.row), slot = it.slot ?? 0;
    const ch = $(el, "chip", `left:${260 + slot * 330}px;top:${(p.top ?? 300) + ri * 170 + 52}px`, it.t);
    tl.fromTo(ch, { y: -(300 + ri * 170), opacity: 0, rotation: -8 }, { y: 0, opacity: 1, rotation: 0, duration: 0.42, ease: "bounce.out" }, c.cue(i + 1)); });
};

/* compare: props {left:{h:"Before",t:"2:07 AM"},right:{h:"After",t:"7:50 AM"}, top:420}  left at cue0, right at cue1 */
S.compare = (c) => {
  const { tl, el, props: p } = c;
  [["left", 60], ["right", 560]].forEach(([k, x], i) => {
    const d = p[k], cd = $(el, "abs", `left:${x}px;top:${p.top ?? 420}px;width:460px;height:760px;border-radius:36px;background:${i ? "var(--ink)" : "#fff"};color:${i ? "#fff" : "var(--ink)"};box-shadow:inset 0 0 0 3px var(--line);padding:56px 44px`);
    $(cd, "", "font-size:40px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;opacity:.55", d.h); $(cd, "", "font-size:96px;font-weight:800;letter-spacing:-.04em;margin-top:30px;line-height:1", d.t);
    (d.lines || []).forEach((l) => $(cd, "", "font-size:46px;font-weight:600;margin-top:34px;line-height:1.2;opacity:.85", l));
    tl.fromTo(cd, { y: 140, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: EASE }, c.cue(i));
  });
};

/* cta: props {word:"DRAFT", pre:"Comment", post:"and I'll DM you the notes template and three morning replies", top:640}  pill lands at cue0, post line at cue1 */
S.cta = (c) => {
  const { tl, el, props: p } = c, top = p.top ?? 640;
  const a = $(el, "abs c", `left:0;width:1080px;top:${top - 150}px;font-size:84px;font-weight:700;letter-spacing:-.02em;opacity:.7`, p.pre || "Comment");
  const pill = $(el, "pill", `top:${top}px;font-size:${p.size ?? 230}px`); const sp = $(pill, "", "", p.word);
  const post = $(el, "abs c", `left:90px;width:900px;top:${top + 400}px;font-size:70px;font-weight:700;letter-spacing:-.02em;line-height:1.15`, p.post);
  tl.fromTo(a, { opacity: 0 }, { opacity: 0.7, duration: 0.3 }, c.cue(0) - 0.2);
  tl.fromTo(sp, { scale: 0.4, opacity: 0, rotation: -4 }, { scale: 1, opacity: 1, rotation: 0, duration: 0.45, ease: POP }, c.cue(0));
  tl.fromTo(post, { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: EASE }, c.cue(1) ?? c.cue(0) + 0.4);
};

/* thread: one continuous DM thread world for "the dots that stopped". The three typing dots are physical objects:
   they pulse, fall out of the bubble when the lead stops typing, and hop back into a new bubble at the end.
   props {name:"Sam", time:"11:47 PM", reply:"No rush. Anything I can clear up?", statement:["That's not","a *no.*"], ring:20, save:"Save this for the next one."}
   cues: 0 start · 1 dots freeze · 2 statement in · 3 strike · 4 ring in · 5 ring draws · 6 type part 1 · 7 type part 2 ·
         8 send · 9,10,11 dot hops · 12 save line */
S.thread = (c) => {
  const { tl, el, props: p } = c, T = (k) => c.cue(k), END = c.end;
  const FLOOR = 1240, D = 104, GAP = 56;
  $(el, "grain"); $(el, "vig");
  // header
  const hd = $(el, "th-head"); $(hd, "th-av", "", (p.name || "Sam")[0]); const nm = $(hd, "th-nm"); $(nm, "th-name", "", p.name || "Sam");
  const st = $(nm, "th-status", "", "typing…"); $(hd, "th-ex", "", "Example");
  $(el, "th-stamp", "", p.time || "11:47 PM");
  const setStatus = (t, txt, col) => tl.call(() => { st.textContent = txt; st.style.color = col; }, null, t);
  setStatus(0, "typing…", "#B794FF"); setStatus(T(1) + 0.05, "Active now", "#9A9AA5"); setStatus(T(9), "typing…", "#B794FF");
  // first typing bubble (frame 0)
  const b1 = $(el, "th-bub", "left:160px;top:720px;width:760px;height:300px");
  const tails = [$(el, "th-tail", "left:150px;top:978px;width:58px;height:58px"), $(el, "th-tail", "left:108px;top:1046px;width:28px;height:28px")];
  const dx0 = 160 + (760 - (3 * D + 2 * GAP)) / 2, dy0 = 720 + (300 - D) / 2;
  const dots = [0, 1, 2].map((i) => $(el, "th-dot", `left:${dx0 + i * (D + GAP)}px;top:${dy0}px;width:${D}px;height:${D}px`));
  tl.fromTo([b1, ...tails], { scale: 0.94 }, { scale: 1, duration: 0.35, ease: "back.out(2)" }, 0);
  const pulse = (t0, t1, base) => { for (let t = t0; t < t1 - 0.3; t += 0.55) dots.forEach((d, i) => {
    tl.to(d, { y: base - 26, backgroundColor: "#D7D7DE", duration: 0.18, ease: "sine.out" }, t + i * 0.12);
    tl.to(d, { y: base, backgroundColor: "#8E8E98", duration: 0.2, ease: "sine.in" }, t + i * 0.12 + 0.18); }); };
  pulse(0, T(1), 0);
  // stop: freeze, bubble collapses, dots fall and bounce on the floor
  const floor = $(el, "th-floor", `top:${FLOOR}px`);
  tl.to(dots, { y: 0, backgroundColor: "#8E8E98", duration: 0.08 }, T(1));
  tl.to([b1, ...tails], { scale: 0, opacity: 0, duration: 0.22, ease: "power3.in", stagger: 0.03 }, T(1) + 0.1);
  tl.fromTo(floor, { scaleX: 0, opacity: 0 }, { scaleX: 1, opacity: 1, duration: 0.4, ease: "power2.out" }, T(1) + 0.15);
  const fall = FLOOR - D - dy0;
  dots.forEach((d, i) => tl.to(d, { y: fall, rotation: [-24, 12, 30][i], duration: 0.62, ease: "bounce.out" }, T(1) + 0.2 + i * 0.06));
  // statement: That's not a no.
  const box = $(el, "stmt", "top:470px;font-size:150px;color:#F5F5F7;visibility:hidden"); let strike = null;
  tl.set(box, { visibility: "visible" }, T(2) - 0.02); tl.set(box, { visibility: "hidden" }, T(4) + 0.15);
  (p.statement || ["That's not", "a *no.*"]).forEach((ln, li) => { const row = $(box, "line");
    ln.split(" ").forEach((w, wi) => { const em = w.startsWith("*") && w.endsWith("*"); const m = $(row, "mk", "position:relative"), i = $(m, "", em ? "color:#F1283A" : "", em ? w.slice(1, -1) : w);
      if (em) strike = $(m, "th-strike"); tl.fromTo(i, rise, { yPercent: 0, duration: 0.42, ease: EASE }, T(2) + (li * 2 + wi) * 0.08); }); });
  if (strike) tl.fromTo(strike, { scaleX: 0 }, { scaleX: 1, duration: 0.22, ease: "power3.out" }, T(3));
  dots.forEach((d, i) => { tl.to(d, { y: fall - 34, duration: 0.14, ease: "power2.out" }, T(3) + 0.1 + i * 0.05); tl.to(d, { y: fall, duration: 0.2, ease: "bounce.out" }, T(3) + 0.24 + i * 0.05); });
  tl.to(box, { y: -90, opacity: 0, duration: 0.25, ease: "power2.in" }, T(4) - 0.12);
  // twenty minute ring
  const R = 290, C = 2 * Math.PI * R;
  const ring = $(el, "th-ring", "", `<svg width="660" height="660" viewBox="0 0 660 660"><circle cx="330" cy="330" r="${R}" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="26"/><circle class="arc" cx="330" cy="330" r="${R}" fill="none" stroke="#6F00FF" stroke-width="26" stroke-linecap="round" transform="rotate(-90 330 330)" stroke-dasharray="${C}" stroke-dashoffset="${C}"/></svg>`);
  const num = $(ring, "th-num", "", "0"); $(ring, "th-min", "", "minutes");
  const arc = ring.querySelector(".arc"), cnt = { n: 0 };
  tl.fromTo(ring, { opacity: 0, scale: 0.86 }, { opacity: 1, scale: 1, duration: 0.4, ease: EASE }, T(4));
  tl.fromTo(arc, { attr: { "stroke-dashoffset": C } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.75, ease: "power3.out" }, T(5));
  tl.fromTo(cnt, { n: 0 }, { n: p.ring || 20, duration: 0.75, ease: "power3.out", onUpdate: () => { num.textContent = Math.round(cnt.n); } }, T(5));
  tl.fromTo(num, { scale: 1 }, { scale: 1.07, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out" }, T(5) + 0.75);
  tl.to(ring, { opacity: 0, scale: 0.9, duration: 0.2, ease: "power2.in" }, T(6) - 0.48);
  // composer types the reply, then sends it as a violet bubble
  const reply = p.reply || "No rush. Anything I can clear up?", cut = reply.indexOf(".") + 1 || reply.length;
  const comp = $(el, "th-comp"); const txt = $(comp, "", "display:inline"); const car = $(comp, "caret th-caret"); const send = $(el, "th-send", "", "&#8593;");
  const typed = { n: 0 }, upd = () => { txt.textContent = reply.slice(0, Math.round(typed.n)); };
  tl.fromTo([comp, send], { y: 260, opacity: 0 }, { y: 0, opacity: 1, duration: 0.3, ease: EASE }, T(6) - 0.26);
  tl.fromTo(typed, { n: 0 }, { n: cut, duration: 0.42, ease: "none", onUpdate: upd }, T(6));
  tl.to(typed, { n: reply.length, duration: 0.9, ease: "none", onUpdate: upd }, T(7));
  tl.fromTo(car, { opacity: 1 }, { opacity: 0, duration: 0.01, repeat: 7, repeatDelay: 0.2, yoyo: true }, T(6) - 0.3);
  const me = $(el, "th-me", "", reply);
  tl.fromTo(send, { scale: 1 }, { scale: 0.82, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.out" }, T(8));
  tl.to(typed, { n: 0, duration: 0.01, onUpdate: upd }, T(8) + 0.06);
  tl.fromTo(me, { y: 520, scale: 0.86, opacity: 0, transformOrigin: "100% 100%" }, { y: 0, scale: 1, opacity: 1, duration: 0.45, ease: EASE }, T(8));
  tl.to([comp, send], { y: 260, opacity: 0, duration: 0.25, ease: "power2.in" }, T(8) + 0.12);
  // the dots come back: a new bubble, each dot hops in on its own word
  const b2 = $(el, "th-bub", "left:60px;top:700px;width:760px;height:300px;opacity:0");
  const t2 = [$(el, "th-tail", "left:50px;top:958px;width:58px;height:58px;opacity:0"), $(el, "th-tail", "left:8px;top:1026px;width:28px;height:28px;opacity:0")];
  tl.fromTo([b2, ...t2], { scale: 0.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.38, ease: "back.out(1.8)", stagger: 0.04 }, T(9) - 0.42);
  const dx1 = 60 + (760 - (3 * D + 2 * GAP)) / 2, dy1 = 700 + (300 - D) / 2, back = dy1 - dy0;
  dots.forEach((d, i) => { const k = T(9 + i);
    tl.to(d, { x: dx1 - dx0, rotation: 0, duration: 0.34, ease: "power2.out" }, k);
    tl.to(d, { y: back - 70, duration: 0.2, ease: "power2.out" }, k); tl.to(d, { y: back, duration: 0.16, ease: "power2.in" }, k + 0.2);
    tl.to(d, { scaleY: 0.82, scaleX: 1.12, duration: 0.06, yoyo: true, repeat: 1 }, k + 0.36); });
  tl.to(floor, { opacity: 0, duration: 0.4 }, T(11));
  pulse(T(11) + 0.45, END, back);
  const save = $(el, "th-save", "", p.save || "Save this for the next one.");
  tl.fromTo(save, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.35, ease: EASE }, T(12));
  tl.fromTo(el.querySelector(".grain"), { backgroundPosition: "0px 0px" }, { backgroundPosition: "480px 360px", duration: END, ease: "steps(240)" }, 0);
};

/* captions: one block per phrase (or per chunk of <= chunk words when chunk > 0), word highlight as spoken.
   phrases: [{cap,start,end}]; cap "" hides the caption (use when the line is already on screen). */
function buildCaptions(tl, root, phrases, lightText, chunk) {
  const cap = $(root, "", ""); cap.id = "cap"; if (lightText) cap.className = "paper-cap";
  const HL = getComputedStyle(document.documentElement).getPropertyValue("--hl").trim() || "#F1283A";
  phrases.forEach((p) => {
    const words = (p.cap ?? p.text).split(/\s+/).filter(Boolean); if (!words.length) return;
    const wt = (w) => w.length + 1.5, tot = words.reduce((s, w) => s + wt(w), 0), dur = p.end - p.start;
    const groups = [];
    if (chunk > 0) { let g = []; words.forEach((w, i) => { g.push(w); if (g.length >= chunk || /[.,?!:]$/.test(w) || i === words.length - 1) { groups.push(g); g = []; } }); }
    else groups.push(words);
    let t = p.start;
    groups.forEach((g, gi) => {
      const ln = $(cap, "cl"); const pill = $(ln, "cp"); const spans = g.map((w) => $(pill, "cw", "", w));
      const gDur = dur * g.reduce((s, w) => s + wt(w), 0) / tot, g0 = t;
      tl.set(ln, { visibility: "visible" }, g0 - 0.02); tl.set(ln, { visibility: "hidden" }, gi === groups.length - 1 ? p.end + 0.06 : g0 + gDur);
      g.forEach((w, i) => { const wd = dur * (wt(w) / tot);
        tl.fromTo(spans[i], { opacity: 0, y: 26, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.14, ease: "power3.out" }, t);
        tl.to(spans[i], { color: HL, duration: 0.05 }, t); tl.to(spans[i], { color: "#fff", duration: 0.05 }, t + wd); t += wd; });
    });
  });
}
