---
name: duxio-website
description: Build, edit, redesign or review the DUXIO website and funnel (landing page, hero, nav, problem section, 4-step mechanism, value calculator, pricing, 2-step application form, booking flow, VSL embed placeholder). Holds the visual design hierarchy, page copy, section headlines, frontend stack, form and database schema, calculator logic and the pre-launch checklist. Use for any DUXIO site, page, section, copy-on-page, form, Lovable or TanStack work. Not for videos (use duxio-vsl).
---

# DUXIO website

Brand files: `brand/duxio/` (logos, fonts, tokens, live site copy in `docs/site-copy.md`, repo facts and known issues in `docs/website.md`).

First load `duxio-brand`, then `site-design-gate` (the 30 vibecoded tells and the audit; run it before and after building) (voice, banned words, zero dashes, offer, claims). This skill adds the website-only rules. Videos live in `duxio-vsl`; never mix the two.

Standard: eight-figure editorial direct response. Clean, light, high contrast, honest. Reject AI slop: no floating purple-pink gradients, no neon glassmorphism blobs, no generic SaaS card grids, no low-contrast grey on dark grey.

## 1. Design system
**Colour (light base, two accents with fixed jobs)**
- Canvas `#FFFFFF`, subtle sections `#F9FAFB`.
- Ink `#111113` for headings and priority body. Secondary `#4B5563`, muted `#6B7280`.
- Violet `#6F00FF` only for primary CTAs, active badges and the single highlighted phrase.
- Red `#F1283A` only for problem indicators, missed revenue, leak points.
- Obsidian `#0D0E12` only for the video container.
- Borders `rgba(0,0,0,.08)` to `.12`, 1px.

**Type: Plus Jakarta Sans**
| Role | Mobile | Desktop | Weight / tracking |
|---|---|---|---|
| Hero | 28 to 32px, lh 1.15 | 56 to 64px | extrabold, -0.02em; key outcome phrase in violet |
| H2 | 26px | 36 to 40px | extrabold, tight |
| Eyebrow | 11 to 12px uppercase | same | bold, +0.08em, muted |
| Body | 15 to 16px, lh 1.6 | same | `#4B5563` |

Paragraphs of two to three lines max. Spacing on an 8px grid.

**Header**
- Desktop: sticky glass bar (`backdrop-blur bg-white/90`), 56 to 64px tall (`h-14 sm:h-16`), ultra-subtle bottom border. DUXIO wordmark (`h-5 sm:h-6 w-auto`). Links: Problem, How It Works, The Numbers, Fit. Right: solid violet "Book a Call".
- Mobile: logo 16 to 20px tall, CTA `whitespace-nowrap` (never wraps), hamburger opens a light drawer with large tap targets.

**VSL container**
- Directly under the hero headline and subhead. `aspect-video`, `max-w-3xl`, centred, obsidian, `rounded-xl` or `rounded-2xl`.
- Truthful placeholder until a video exists: no fake duration, no fake scrub bar or playhead. A centred play icon plus "See how quiet leads become paying clients. Walkthrough coming soon."
- Swaps cleanly to Loom, Wistia, Vimeo or an HTML5 MP4 when uploaded.

**Mobile**
- Designed and tested at 360px. `overflow-x: hidden`, zero horizontal scroll.
- Tap targets at least 44×44px.
- Sticky bottom CTA on mobile, linking to `#apply`.

## 2. Page copy
- **Hero headline:** "Turn interested leads into paying clients."
- **Hero subhead:** "We build and run the follow up that moves serious buyers from first interest to a booked sales call."
- **Problem headline:** "You don't need more leads. You need to stop losing the ones you have."
- **Problem comparison**
  - Right now: replies come hours late. Leads live in six places. People book and never show. Forty five minute calls with people who were never a fit.
  - With DUXIO: answered in under a minute. Every inquiry in one place. Prospects show up prepared. Follow up runs on its own.
- **How it works:** the four steps from `duxio-brand` §4, numbered 01 to 04, in that wording.
- **Fit section:** the approved situation wording from `duxio-brand` §6. Never an income gate.
- **Pricing:** $397 one time to build, live in under 48 hours. Then $300 to $800 a month to run it, based on lead volume. Add the justification frame. Never "$397/mo".
- **CTA everywhere:** "Book a Strategy Call" (nav may say "Book a Call"). Use the Strategy Call pitch from `duxio-brand` §5 near the form.

## 3. Stack
- TanStack Start v1 (React 19) + Vite + Tailwind CSS v4.
- A single content-driven funnel at `src/routes/index.tsx`, rendering semantic HTML from `src/content/page.html`.
- Tokens as CSS variables: `--canvas:#FFFFFF; --canvas-subtle:#F9FAFB; --ink:#111113; --secondary:#4B5563; --muted:#6B7280; --accent-violet:#6F00FF; --accent-red:#F1283A; --obsidian:#0D0E12`.
- Plus Jakarta Sans loaded with a `<link>` in `src/routes/__root.tsx`.

## 4. Two-step application and booking
- Step 1, contact: `full_name` (required), `email` (required), `phone_or_handle` (phone or Instagram, required).
- Step 2, fit: `offer_price` (select: $1,000 to $3,000 · $3,000 to $5,000 · $5,000+), `monthly_inquiries` (10 to 30 · 30 to 80 · 80+), `biggest_bottleneck` (Slow replies · Leads going cold · Unqualified calls · Messy inboxes).
- No page reloads between steps. After step 2 succeeds, route straight to the booking calendar.
- Keep the questions casual and respectful. They check operational fit, not financial status.
- **Database** (Lovable Cloud / Postgres): table `public.lead_applications` with `id uuid`, `full_name`, `email`, `phone_or_handle`, `offer_price`, `monthly_inquiries`, `biggest_bottleneck`, `created_at`. RLS enabled. Public `INSERT` only, with strict validation (lengths, email format, the select values whitelisted).

## 5. Value calculator
- Sliders: average offer value ($1,000 to $10,000, default $3,000); monthly inbound leads (20 to 200, default 80).
- Outputs: conservative rescued clients (1 to 2 a month); revenue rescued = rescued clients × offer value; net added = revenue rescued minus the monthly fee.
- Label it as an illustration, not a forecast.

## 6. Pre-launch checklist (all must pass)
- `site-design-gate` audit passed: none of the 30 tells, Terms and Privacy linked, skeleton loaders, no fake testimonials.
1. `duxio-brand` pre-flight (§9): zero dashes, no banned words, no freebies, no income gate, four steps, claims allowed.
2. 360px viewport: no horizontal overflow; nav CTA on one line; logo proportioned.
3. Video container: truthful placeholder, or the real embed; no fake counters.
4. Hero reads "Turn interested leads into paying clients."
5. Form: both steps validate, the insert lands in `lead_applications`, and the redirect reaches the calendar.
6. Lighthouse accessibility: contrast passes and tap targets are at least 44px.
7. Check the rendered page in a browser at 360, 768 and 1440 widths, with screenshots, before calling it done.
