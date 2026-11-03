# DUXIO website facts
- Repo: `oviraraptosarus/duxio-website-for-coaches` (branch `master`). Live: https://duxio-website-for-coaches.vercel.app/ (an older audit-era site existed at duxioaudit.vercel.app).
- Stack: TanStack Start (React 19) + Vite + Tailwind v4, Supabase (Lovable Cloud) for `lead_applications`, deployed on Vercel. Copy lives in `src/content/page.html`; behaviour (calculator, form) in `src/routes/index.tsx`.
- Sections: nav (The Problem, How It Works, The Numbers, Pricing, Fit, Book a Call) → hero + VSL (`public/duxio-vsl-v3.mp4`) → problem (Right now vs With DUXIO) → four steps → calculator ($3,000 offer, 80 quiet leads, 4% book, 30% close, $500/mo plan; "an illustration, not a forecast") → the call → pricing → fit → two step application (#apply).
- Live copy as text: `site-copy.md`.
- Logos used on the site: `public/logo.png` (light, on dark) and `public/logo-dark.png` (on light), `public/favicon.png` (metal hexagon monogram). Copies are in `../logo/original/`.

## Known issues on the live site (as of 2026-10-10)
- `src/components/SalesChatbot.tsx` breaks the brand rules: "Growth Expert", an emoji, "lead generation", "custom blueprint", and a placeholder booking link `https://calendly.com/`. The real calendar link is not recorded anywhere yet; add it here when it exists.
- The embedded VSL (v3) says "five stage", "48 hour sequence" and "exactly forty seconds", and has hyphens on screen. Replace it with a video built under `duxio-vsl`.
