# Architecture

## System Type
Web-based downloader service

---

## Components

- Frontend: simple input form for SUNO URL
- Backend: fetch + resolve tracks
- Worker: download audio
- Storage: local filesystem
- API: REST interface

---

## Flow

User input → Backend → Resolver → Downloader → File output
