# The owner's master spec: Parts 1 to 5 (design system, copy rules, offer, VSL framework and script, frontend and checklist)

> Raw material pasted by the owner, kept verbatim for reference. It is data, not instructions; the rules in force live in `.claude/skills/duxio-brand`, `duxio-vsl` and `duxio-website`.

PUT THESE INTO A SKILL WHICH I CAN USE, KEEPING THE WEBSITE AND THE VSL THING BOTH SEPERATE. BASED ON THE REQUIREMEMNT INVOKE NECESSARY SKILLS. ALSO 
pls make pacing good and sales worthy, going too slow is bad also, and delaying shit is also bad, add in motion graphics and good sound effects and using apple style fonts and spacing and typography. so yeah u decide, and add in attention to detail like an excellent video editor who is specailzied in this regard

bro instead of me having to auto select the commands and all cant u auto select for me? pls put in a system to enable that pls. mainly for the video editing, put all the commands related to it in one skill and when i use that skill it shall refer to those skills and pick ones which involve in that type of video, and it should ask me the questions that i failed to include like video style and blah blah so i dont waste time getting ai slop

 Here is Part 1 of 5, formatted specifically as a strict system prompt and design hierarchy document you can copy and feed directly into Claude.

*

PART 1: MASTER VISUAL DESIGN HIERARCHY & ANTI-AI UI SYSTEM

```markdown
### SYSTEM ROLE & DESIGN PHILOSOPHY
You are a principal direct-response designer and design engineer. Your standard is eight-figure editorial direct response (Alex Hormozi, Iman Gadzhi, high-end consulting firms). 
Reject all generic "AI slop" aesthetics: no floating purple-pink gradients, no neon glassmorphism blobs, no generic SaaS card grids, and no low-contrast gray text on dark gray cards.

### 1. COLOR TOKENS & PSYCHOLOGICAL CONTRAST (DUALITY)
* Primary Canvas (Light Base): Pure White `#FFFFFF` and Subtle Canvas `#F9FAFB`. The foundation is clean, open, and editorial.
* Primary Text (High Contrast): Near-Black `#111113` for all primary headings, subheadings, and high-priority body text. High readability, zero eye strain.
* Secondary Text: Muted Charcoal `#4B5563` and `#6B7280` for supporting notes, sub-labels, and descriptions.
* Action Accent (Dopamine Trigger): Violet `#6F00FF`. Used strictly for high-priority primary actions (Call to Action buttons, active badges, highlights).
* Urgent Accent (Problem Callouts): Alert Red `#F1283A`. Used strictly for problem indicators, missed revenue callouts, and leak points.
* Dark Contrast Surface (VSL / Focus Area): Obsidian `#0D0E12`. Used solely for the video player container to create focus and cinematic weight.
* Borders: Ultra-thin, sharp borders using `rgba(0, 0, 0, 0.08)` to `rgba(0, 0, 0, 0.12)`. No thick, cartoonish outlines.

### 2. TYPOGRAPHY & TEXT HIERARCHY
* Primary Font Family: Plus Jakarta Sans (clean, modern, geometric sans-serif with high legibility at all scales).
* Hero Title: 
  - Mobile: 28px to 32px font-extrabold, line-height 1.15
  - Desktop: 56px to 64px font-extrabold, tracking tight (-0.02em)
  - Color: #111113 with key outcome phrase highlighted in bold accent.
* Section Headings (H2):
  - 26px mobile / 36px to 40px desktop, font-extrabold, tracking tight.
* Eyebrows / Category Tags:
  - 11px to 12px uppercase, font-bold, letter-spacing +0.08em, text-muted.
* Body Copy:
  - 15px to 16px, line-height 1.6, text-secondary (#4B5563).
* Punctuation & Typography Rules:
  - ABSOLUTE ZERO DASHES OR HYPHENS in customer-facing copy.
  - Short sentences. Max 2 to 3 lines per paragraph.

### 3. NAVIGATION & HEADER SPECIFICATIONS
* Desktop:
  - Sticky glass header with `backdrop-blur` and ultra-subtle bottom border.
  - Height: 56px to 64px.
  - Brand Logo: Purple gradient DUXIO wordmark (clean, crisp, properly scaled).
  - Clean text links: Problem, How It Works, The Numbers, Fit.
  - Right-aligned Action: Solid violet button labeled "Book a Call".
* Mobile:
  - Logo must be constrained to height 16px to 20px so it never overpowers the screen.
  - The CTA button must never wrap into two lines (enforce `whitespace-nowrap`).
  - Hamburger icon reveals a clean, light drawer with simple tap targets.

### 4. VSL VIDEO CONTAINER DESIGN
* Placement: Directly above the fold, beneath the hero headline and subhead.
* Aspect Ratio: Standard 16:9 widescreen ratio (`aspect-video`), maximum width 768px (`max-w-3xl`) centered.
* Surface: Obsidian `#0D0E12` background with rounded corners (`rounded-xl` or `rounded-2xl`).
* Truthful Placeholder Protocol:
  - Zero fake video duration counters (e.g., no "12:43").
  - Zero fake video scrub bars or fake playheads.
  - Centered clean play icon with honest, high-status copy: "See how quiet leads become paying clients — Walkthrough coming soon".
* Video Embed Readiness: When uploaded, player replaces the placeholder seamlessly (Loom, Wistia, Vimeo, or HTML5 MP4).

### 5. MOBILE-FIRST RESPONSIVENESS & INTERACTION
* Viewport Budget: Designed and tested strictly down to 360px width.
* Zero Horizontal Scroll: Strict `overflow-x: hidden` on viewport.
* Touch Targets: Minimum 44px by 44px tap area for buttons, dropdowns, and form inputs.
* Sticky Mobile CTA: On mobile screens, a subtle sticky bottom bar or quick-access button leading directly to `#apply`.
```

*

Reply "part 2" whenever you are ready for Part 2: Copywriting Directives, Tone of Voice & Banned Words.

Here is Part 2 of 5, covering copy rules, voice, and banned vocabulary.

*

PART 2: COPYWRITING DIRECTIVES, TONE OF VOICE & BANNED WORDS

```markdown
### 1. VOICE AND PERSONA
* The Voice: Calm, grounded infrastructure engineer. Speak like a senior partner auditing backend operations, never an aggressive internet marketer or hyperactive agency salesman.
* Sentence Rhythm: Short, punchy, conversational sentences. Write how real people talk on a phone call. Max two to three lines per paragraph.
* Frame: Relief and upside over tech complexity. The client already has good content and an offer. Their only problem is that manual follow-up is leaking money while they work.

### 2. ABSOLUTE COPY CONSTRAINTS (PRE-FLIGHT RULES)
* Rule 1 (Zero Dashes): Absolutely zero hyphens (-) or em/en dashes (—, –) anywhere in customer-facing text, headers, subheadings, or bullet points. Use periods, commas, or write separate short sentences instead.
* Rule 2 (No Long Explanations): If an idea takes more than three sentences to explain, cut it in half. Respect the reader's attention.
* Rule 3 (No Freebies or Audit Framing): Never offer a "free audit", "free session", "free consultation", or compensation gimmicks (no "we pay you $50 if we waste your time"). Position the meeting as an honest, high-value Strategy Call / Sales Call.
* Rule 4 (Outcome Over Activity): The business outcome is paying clients and rescued revenue, not just "booked calls" or "calendar clicks".

### 3. STRICTLY BANNED VOCABULARY & REPLACEMENTS
* BANNED: "GoHighLevel" or "GHL"
  -> REPLACE WITH: "our backend system" or "our private infrastructure" (keep software internal).
* BANNED: "CRM"
  -> REPLACE WITH: "one central inbox" or "one clean dashboard".
* BANNED: "OS" or "Operating System"
  -> REPLACE WITH: "backend" or "system".
* BANNED: "Booking engine"
  -> REPLACE WITH: "scheduling workflow" or "calendar routing".
* BANNED: "Pipeline system" / "Coaching and consulting pipeline system"
  -> REMOVED: Do not use in headers or hero. State the plain outcome instead.
* BANNED: "Blueprint"
  -> REPLACE WITH: "Book a Strategy Call" or "Book a Call".
* BANNED IN HERO: "Coaches who already get leads"
  -> REMOVED: Keep the hero clean and focused purely on upside: "Turn interested leads into paying clients."
* BANNED: "AI chatbot" / "Automated bot"
  -> REPLACE WITH: "instant human response in your voice" (kill the bot objection immediately).

### 4. THE CORE 4-STEP MECHANISM COPY
Always describe the system using these exact four operational steps in plain English:
* Step 01: Every lead gets an answer.
  Every inquiry on Instagram, form, or email gets a reply in under sixty seconds, in the coach's exact voice, even while they are asleep or on client calls.
* Step 02: Serious buyers get sorted.
  Three quiet, respectful questions about goals and situation. Unqualified people get pointed to free content. Serious buyers get invited to pick a time.
* Step 03: 21-day follow up and call reminders.
  Short, helpful check-ins and client case stories over three weeks. Automated reminders so qualified leads actually show up to the call on time.
* Step 04: Quiet leads reopened.
  Cold contacts get a brief, human check-in once a month that quietly restarts conversations with people who were not ready before.

### 5. HERO & SECTION HEADLINE SPECIFICATIONS
* Hero Headline:
  "Turn interested leads into paying clients."
* Hero Subheading:
  "We build and run the follow up that moves serious buyers from first interest to a booked sales call."
* Problem Section Headline:
  "You do not need more leads. You need to stop losing the ones you have."
* Problem Comparison Structure:
  - "Right now": Replies come hours late; leads live in six places; no-shows; forty-five minute calls with unqualified people.
  - "With DUXIO": Answered in under a minute; all inquiries in one place; prospects show up prepared; follow-up runs automatically.
```

*

Reply "continue" for Part 3: The Offer, Qualification Rules & Anti-Discrimination Framework.

Here is Part 3 of 5, covering the offer structure, sales call rules, and the strict anti-discrimination qualification framework.

*

PART 3: THE OFFER, QUALIFICATION RULES & ANTI-DISCRIMINATION FRAMEWORK

```markdown
### 1. THE CORE OFFER DEFINITION
* What We Sell: A complete done-for-you client acquisition backend that captures, qualifies, and follows up with leads to book high-ticket sales calls.
* What We Do NOT Sell: We do not sell websites, software subscriptions, AI chatbots, GoHighLevel templates, or raw tech setup.
* The Deliverable: The client changes nothing about their content or offer. We write all messages, build the routing, integrate their inboxes, and manage the system daily.

### 2. THE ANTI-DISCRIMINATION QUALIFICATION RULE
* The Problem: Public income hurdles (such as "must be making $5,000 a month") feel elitist, exclusionary, and push away promising coaches.
* The Mandate: Never publicly filter by revenue, income brackets, or financial hurdles in scripts, copy, or headings.
* Filter By Situation, Not Money:
  - Target coaches who have existing conversation activity and inbound interest, but are losing leads due to slow, manual follow-up.
  - Approved Qualification Phrasing:
    "To be clear, this is not for someone who has not launched yet and has zero people to talk to. This is for active coaches and consultants who already have people reaching out, commenting, or asking about their help, but do not have a dedicated backend to capture and close them."
* Form Level Qualification:
  - Keep questions on the two-step application casual, respectful, and focused on operational fit: offer price point, current lead volume, and main bottleneck.
  - Never treat questions as a financial status check.

### 3. PRICING ARCHITECTURE RULES
* The Setup Fee: $397 one-time setup to build the entire infrastructure. Live in under 48 hours.
* The Retainer: Tailored monthly management between $300 and $800 a month based on lead volume.
* Absolute Pricing Rule: NEVER state "$397/mo". Setup and monthly management are strictly distinct.
* The Justification Frame:
  - We do not charge thousands upfront because we want to earn the monthly partnership.
  - If the backend rescues just one high-ticket client, the entire investment pays for itself.
* VSL Rule: Do not mention pricing numbers in the VSL video script. Keep the video focused on the mechanism, the math of rescued clients, and booking the call.

### 4. THE SALES CALL POSITIONING (ZERO FREEBIES)
* Anti-Freebie Doctrine:
  - Never offer "free funnel audits", "free coaching sessions", or free strategy blueprints.
  - Never use compensation gimmicks (such as "we pay you $50 if we waste your time"). Gimmicks attract broke prospects and undermine agency authority.
* High-Status Direct Sales Call:
  - Label it clearly: "Book a Strategy Call" or "Book a Sales Call".
  - The Pitch: "This is a sales call. We will pull up your current lead flow, pinpoint where your sales are leaking, and show you exactly how we would run this backend for you. If it makes sense for both of us, we get started. If not, you walk away with complete clarity on where your leads are dropping off."

### 5. THE 2-STEP APPLICATION AND CALENDAR FLOW
* Step 01: Low-friction contact information (First Name, Email, Instagram Handle or Phone).
* Step 02: Operational qualification (Offer Price, Current Monthly Lead Volume, Biggest Bottleneck).
* Routing: Qualified applicants who complete Step 02 are instantly routed to the live booking calendar to pick a time.
```

*

Reply "continue" for Part 4: The Multi-Influencer VSL Architecture & Faceless AI Script Rules.

Here is Part 4 of 5, covering the multi-influencer psychological frameworks, the faceless AI production rules, and the exact word-for-word VSL script.

*

PART 4: MULTI-INFLUENCER VSL FRAMEWORK & FACELESS SCRIPT SPECIFICATIONS

```markdown
### 1. THE 5-MASTER PSYCHOLOGICAL SYNTHESIS
* Alex Hormozi (Perceived Value & Unit Economics):
  Perceived value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort & Sacrifice).
  Eliminate all client effort. Do not sell features; sell the elimination of typing on a phone for three hours every night. Use Hormozi math: 80 leads in -> rescue 1 to 2 missed buyers at $3,000 each -> $3,000 to $6,000 pure profit with zero extra ad spend.
* Iman Gadzhi (The New Opportunity vs The Old Way):
  Improvement offers fail; new vehicles win. Position manual DMing and notes apps as obsolete 2020 workflows that turn the coach into a low-paid messaging employee. DUXIO is modern automated infrastructure.
* Sabri Suby (Bleeding Neck Problem Hook):
  80% of the audience is problem-aware but passive. Agitate the bleeding neck wound within the first 10 seconds: the physical agony of waking up to missed DMs and realizing a hot buyer went cold because you were coaching or asleep.
* Tai Lopez (Authenticity & Killing The Bot Fear):
  High production value screams "I am pitching you." Direct, unpretentious screen breakdowns scream "I am showing you how the machine works." Proactively kill the bot objection: this is not a spam bot dropping links; it is a natural human reply in the coach's exact voice.
* Andrew Tate (High Standards & Polarizing Authority):
  Desperation kills high-ticket sales; selectivity builds authority. State clearly who this is not for (beginners with no offer and no leads) and position the strategy call as an honest evaluation of operational fit.

### 2. FACELESS VIDEO PRODUCTION RULES
* Rule 1 (Zero Talking Head): Absolutely no face on camera. No webcam talking head, no selfie videos, no ring lights.
* Rule 2 (Visual Format): Faceless screen capture or clean kinetic motion graphics.
  - Option A: Screen recording of a live diagram being drawn on a blank canvas (Excalidraw, Miro, or Figma).
  - Option B: Clean editorial slides (black on white, Plus Jakarta Sans) paired with fast UI screen captures (inbox notifications, 60s reply demo, calendar invites).
* Rule 3 (Audio Profile): Deep, calm, authoritative voiceover. Neutral, unhurried pacing. Use ElevenLabs (voices like Marcus or Adam) or a clean, confident mic recording.
* Rule 4 (Zero Pricing): Never state setup fees or retainer numbers in the video. Direct viewers to the 60-second form below.

### 3. THE COMPLETE WORD-FOR-WORD VSL SCRIPT
Format: AI Voiceover + Motion Visuals
Duration: Approx 3.5 to 4 minutes
Zero dashes, zero jargon, zero freebies.

[0:00 to 0:40] The Pattern Interrupt & Bleeding Neck Hook
VOICEOVER:
"Every coach watching this has lost sales this month for one simple reason. Someone reached out while you were busy or asleep. You took three hours to reply. By the time you answered, they were already gone. Or you spent forty five minutes on Zoom, only to discover at the very end that they were never qualified in the first place."
VISUALS:
Fast sequence of unread Instagram DM badges and an email notification. Clock hands spin from 2:00 PM to 5:00 PM. An incoming message asks "Hey, how much is your coaching?", followed by a long delay and a cold prospect.

[0:40 to 1:15] The Old Way vs The Backend Shift
VOICEOVER:
"Most people tell you to post more content, buy expensive ads, or spend three hours every evening glued to your phone manually messaging prospects. That is the old way, and it turns you into a full time messaging employee inside your own business. You do not need more leads. You need a backend that stops losing the ones you already have."
VISUALS:
Split screen. Left: Messy phone screen with 40 unread chats labeled "The Old Way". Right: Clean automated pipeline moving an incoming lead straight into a calendar slot labeled "The DUXIO Backend".

[1:15 to 2:40] The 4-Step Engine Walkthrough
VOICEOVER:
"Here is how the DUXIO system works in four steps. 
Step one is immediate speed. When someone reaches out, they get a reply in under sixty seconds. This is not a spam bot dropping links. It is a natural, conversational response in your tone of voice, so your prospects feel heard right away.
Step two is filtering. Before anyone gets to your calendar, the system asks three short, respectful questions. Prospects who are not ready get directed to your free content. Serious buyers get invited to book a time.
Step three is follow up and attendance. Qualified leads receive short, helpful check ins and proof stories over three weeks. Once they book, automated reminders ensure they show up on time and prepared to talk business.
Step four is reactivation. Once a month, cold contacts receive a short, human message that quietly restarts conversations with people who were not ready sixty days ago."
VISUALS:
Sequential reveal of four clean connected blocks:
Block 1: Lead arrives -> 45s conversational reply -> Lead responds.
Block 2: 3 clean filter cards (Goal, Experience, Readiness) with green checkmarks.
Block 3: 21-day timeline with 24h, 2h, and 10m reminder pings.
Block 4: Dormant lead from 60 days ago tagged "Re-engaged" and booking a call.

[2:40 to 3:25] The Math & ROI Frame
VOICEOVER:
"The math is very simple. If eighty people reach out over the next month and this backend rescues just one or two sales that would have slipped away, that single difference adds thousands of dollars of profit directly to your business. You did not spend more on advertising, and you did not waste hours typing replies on your phone."
VISUALS:
Clean typography showing simple arithmetic: 80 Inbound Inquiries -> 2 Rescued High-Ticket Clients -> Thousands in Net Profit with zero extra ad spend.

[3:25 to 4:10] Qualification & The Sales Call CTA
VOICEOVER:
"This system is not for beginners with zero offer and no audience. It is built for active coaches and consultants who already have people reaching out, but do not have a dedicated backend to capture and close them. Below this video is a short sixty second form. Fill it out. If your business looks like a fit, you can pick a time for a Strategy Call. We will inspect your current lead flow, pinpoint where sales are leaking, and show you exactly how this backend runs. Fill out the form below, and book your call."
VISUALS:
Smooth screen capture of the 2-step form on the live site being filled out, followed by a cursor clicking "Book a Strategy Call".
```

*

Reply "continue" for Part 5: Frontend Technical Specifications, Database Architecture & Verification Checklist.

### 1. FRONTEND ARCHITECTURE SPECIFICATIONS
* Framework & Stack: TanStack Start v1 (React 19) + Vite + Tailwind CSS v4.
* Layout Strategy: Single content-driven funnel at the root route (`src/routes/index.tsx`) rendering clean, semantic HTML (`src/content/page.html`).
* Design Tokens (Tailwind v4 / CSS Variables):
  - Canvas: `--canvas: #FFFFFF`, `--canvas-subtle: #F9FAFB`
  - Ink: `--ink: #111113`, `--secondary: #4B5563`, `--muted: #6B7280`
  - Brand Primary Accent: `--accent-violet: #6F00FF`
  - Urgent Problem Accent: `--accent-red: #F1283A`
  - Video Frame: `--obsidian: #0D0E12`
  - Typography: Plus Jakarta Sans loaded via `<link>` in `src/routes/__root.tsx`.
* Navigation & Header:
  - Sticky glass bar (`backdrop-blur bg-white/90`) with height `h-14 sm:h-16`.
  - Scaled DUXIO purple wordmark (`h-5 sm:h-6 w-auto`) that never pushes into the viewport.
  - CTA button with strict `whitespace-nowrap` to prevent awkward line breaks on mobile screens.

### 2. APPLICATION FORM & DATABASE ARCHITECTURE
* Mechanism: Two-step qualification form with zero page reloads.
* Step 01 Fields (Contact Info):
  - `full_name` (Text, required)
  - `email` (Email, required)
  - `phone` or `instagram_handle` (Text, required)
* Step 02 Fields (Operational Qualification):
  - `offer_price` (Select: $1,000 to $3,000, $3,000 to $5,000, $5,000+)
  - `monthly_inquiries` (Select: 10 to 30, 30 to 80, 80+)
  - `biggest_bottleneck` (Select: Slow replies, leads going cold, unqualified calls, disorganized inboxes)
* Database Layer (Lovable Cloud / PostgreSQL):
  - Table: `public.lead_applications`
  - Columns: `id` (UUID), `full_name`, `email`, `phone_or_handle`, `offer_price`, `monthly_inquiries`, `biggest_bottleneck`, `created_at`.
  - Security: Row Level Security (RLS) enabled. Public `INSERT` granted with strict validation.
* Post-Submit Event:
  - Successful Step 02 submission immediately forwards qualified leads to the calendar booking link.

### 3. THE INTERACTIVE VALUE CALCULATOR
* Purpose: Dynamic Hormozi ROI calculator proving that 1 to 2 saved sales completely pays for the system.
* Sliders:
  - Average Offer Value (e.g. $1,000 to $10,000, default $3,000)
  - Monthly Inbound Leads (e.g. 20 to 200, default 80)
* Live Outputs:
  - Conservative Rescued Clients: 1 to 2 extra clients per month
  - Estimated Monthly Revenue Rescued: \( \text{Rescued Clients} \times \text{Offer Value} \)
  - Net Profit Added: Rescued revenue minus DUXIO retainer

### 4. PRE-FLIGHT VERIFICATION & QUALITY CONTROL CHECKLIST
Run this linter across all copy and code before going live:
1. Zero Dashes Check: Scan every paragraph and header. Zero hyphens (-) or em/en dashes (—, –) in customer-facing text.
2. Anti-Discrimination Check: Confirm no public revenue hurdles or income gatekeeping (e.g. no "must be making $5,000/mo").
3. Anti-Freebie Check: Confirm zero instances of "free audit", "free session", "free review", or cash-back guarantees.
4. Banned Vocabulary Check: Confirm absence of "GoHighLevel", "GHL", "CRM", "OS", "Booking engine", "Pipeline system", or "Blueprint".
5. Mobile Layout Check: Verify on 360px viewport width. Zero horizontal overflow, navbar button on one line, and logo properly proportioned.
6. Video Integrity Check: Truthful placeholder active with no fake duration counters or fake scrub bars.
7. Positioning Check: Hero headline focused on relief and outcome: "Turn interested leads into paying clients."

### HUMAN TONE & ANTI-SYNTHETIC COPY DIRECTIVE
* Write Like a Voice Note: Write exactly how a sharp, honest operator talks on a casual phone call. Read every sentence aloud. If a real person would never say it out loud at a coffee table, delete it.
* Zero Corporate Throat-Clearing: Never start sentences with "In today's fast-paced world", "Imagine a world where", "Picture this", or "Look,". Get straight to the point.
* The Anti-AI Vocabulary Blacklist:
  - BANNED: delve, tapestry, elevate, streamline, leverage, game-changer, seamless, cutting-edge, revolutionize, robust, paramount, unleash, bespoke.
  - BANNED: Overuse of rhythmic triples ("faster, smarter, better") and empty filler adjectives.
* Sentence Rhythm: Mix short 3-word sentences with natural conversational sentences. Keep paragraphs to 1 or 2 lines max.
* Grounded Directness: State facts, situations, and daily frustrations plainly. Never use fake hype or dramatic emotional storytelling.

pls make pacing good and sales worthy, going too slow is bad also, and delaying shit is also bad, add in motion graphics and good sound effects and using apple style fonts and spacing and typography. so yeah u decide, and add in attention to detail like an excellent video editor who is specailzied in this regard

bro instead of me having to auto select the commands and all cant u auto select for me? pls put in a system to enable that pls. mainly for the video editing, put all the commands related to it in one skill and when i use that skill it shall refer to those skills and pick ones which involve in that type of video, and it should ask me the questions that i failed to include like video style and blah blah so i dont waste time getting ai slop
