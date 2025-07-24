# Project Flow

A monorepo containing both frontend and backend services for Project Flow.

## Structure

```
project-flow/
├── frontend/          # SvelteKit frontend application
├── backend/           # FastAPI backend application
├── package.json       # Root package.json for monorepo management
└── LICENSE.md         # GPL-3.0 license
```

## Tech Stack

- **Frontend**: SvelteKit with TypeScript and Vite
- **Backend**: FastAPI with Python (managed with pip and virtual environment)

## Development

### Prerequisites

- Node.js (for frontend)
- Python 3.12+ (for backend)
- Git Bash (recommended terminal for Windows)

### Getting Started

1. **Setup dependencies**:
   ```bash
   npm run setup
   ```

2. **Activate backend virtual environment** (in Git Bash):
   ```bash
   source backend/activate.sh
   # or manually: source backend/.venv/Scripts/activate
   pip install -r backend/requirements.txt
   ```

3. **Run both services** (frontend on :5173, backend on :8000):
   ```bash
   npm run dev
   ```

3. **Run services individually**:
   ```bash
   # Frontend only
   npm run dev:frontend
   
   # Backend only (make sure virtual environment is activated first)
   fastapi dev backend/main.py
   ```

### Building

```bash
npm run build
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
