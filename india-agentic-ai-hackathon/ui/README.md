# HackGrid Pipeline Demo UI

Vite + React + TypeScript front-end for the HackGrid pipeline demo.

## Setup

```bash
cd ui
npm install
npm run dev
```

Opens at http://localhost:5173. Proxies `/api` → `http://127.0.0.1:8765`.

## Modes

- **Replay** (default on load): animates the newest successful past run (~30–45s).
- **Run live**: `POST /api/runs` then SSE on `/api/runs/{id}/stream`.

The UI builds without the API; controls show empty/unavailable states until FastAPI is up.
