# Decision DEC-001

## Context
Need to define approach for SUNO audio extraction.

---

## Decision
Use reverse-engineering of frontend API calls instead of HTML scraping.

---

## Reasoning
- SUNO content is dynamically loaded
- No direct media URLs in DOM
- API layer is the only reliable source

---

## Consequences
- Requires network inspection tooling
- May break if SUNO changes API
- Higher robustness than scraping

---

## Affected Components
- Backend design
- Research module
- Downloader service

---

## Status
Approved
