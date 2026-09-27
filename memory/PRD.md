# PRD — Keuangan-1 (Aplikasi Keuangan & HPP UMKM)

## Problem statement (asli)
Import repo GitHub `danarhuda59-commits/Keuangan-1` (app Emergent-generated: FastAPI + MongoDB + React CRA/CRACO), install dependensi reproducible dengan lockfile, siapkan env lokal & production, verifikasi e2e lokal, audit tanpa refactor, kesiapan deploy (frontend Vercel, backend Railway/Render/Fly via Dockerfile, MongoDB Atlas).

## Pilihan user
- Backend hosting: Railway/Render/Fly + Dockerfile (bukan Vercel)
- Data awal: DB kosong + seed 1 admin baru (`admin@keuangan.id` / `admin12345`)
- Package manager: yarn (commit `yarn.lock`)

## Persona
Pemilik/operator UMKM F&B: hitung HPP dari bahan & resep, catat pembelian/produksi/penjualan, lihat laporan.

## Arsitektur
- `backend/` FastAPI 0.110 (Python 3.11), Motor, JWT (PyJWT) + bcrypt, semua route prefix `/api`
- `frontend/` React 19 CRA + CRACO 7, Tailwind, shadcn/ui, SWR/axios
- MongoDB (lokal dev → Atlas prod)

## Yang sudah dikerjakan (Juni 2026)
- [x] Fase 0: clone, scan credential (bersih), catatan revoke PAT
- [x] Fase 1: `requirements.txt` minimal (18 paket, versi identik freeze asli), `requirements.lock`, `.env.example`, `Dockerfile`, `.python-version`, `runtime.txt`; backend jalan, admin ter-seed, 11 unit test HPP lulus
- [x] Fase 2: `yarn.lock`, `.env.example`, `vercel.json`, `.nvmrc`; audit craco (plugin Emergent sudah ter-gate untuk prod); `CI=true yarn build` lolos 0 warning
- [x] Fase 3: e2e via testing agent — login, bahan, produk, resep+HPP (math terverifikasi), pembelian→produksi→penjualan, laporan, isolasi multi-tenant: 8/8 backend + 7 route frontend lulus (`backend/tests/test_setup_e2e.py`)
- [x] Fase 4: `AUDIT.md` (keamanan S1–S11, HPP H1–H8, struktur, prioritas P0–P2)
- [x] Fase 5: checklist deploy di `AUDIT.md` + `README.md`

## Backlog prioritas (dari AUDIT.md)
- P0: CORS eksplisit; ganti Emergent Object Storage untuk upload logo; hapus script telemetri Emergent di `index.html`; JWT_SECRET prod
- P1: RBAC owner-only untuk restore/demo/users; hilangkan token di query string; rate limit via X-Forwarded-For + register; fix `pct_material` sub-resep di `expand_items`
- P2: Decimal/integer rupiah; lifespan API; `@emergentbase/*` → optionalDependencies; bersihkan test preview-only

## Tidak diubah (by design)
Seluruh kode aplikasi (`backend/*.py`, `frontend/src/**`, `craco.config.js`, `index.html`).
