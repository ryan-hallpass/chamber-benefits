# Ardmore Chamber — Membership Landing Page

Conversion-focused landing page recruiting members for the **Ardmore Chamber of Commerce**.
Traffic arrives via a QR code on a hand-delivered postcard (mobile-first, warm audience).

- **Primary conversion:** RSVP to be a guest at the next *Business After Hours* (free) → GoHighLevel.
- **Secondary conversion:** "Join now" → the Chamber membership application.

Single self-contained `index.html` (inline CSS/JS, no build step). Destined for a dedicated
subdomain (e.g. `chamberbenefits.ardmore.org`); served meanwhile via GitHub Pages.

### Swappable config (top of the `<script>` block)
- `CAPTURE_ENDPOINT` — GoHighLevel inbound webhook (empty = reveal-first, no send).
- `JOIN_URL` — membership application URL (empty = falls back to the RSVP form).
- `NEXT_EVENT` — optional `{ date, venue }`; empty shows an evergreen line (never stale).

Built by Hallpass Digital.
