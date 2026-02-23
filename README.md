# FlowForge
A full‑stack workflow automation engine with triggers, actions, scheduling, and a visual editor.

FlowForge lets users create automated workflows that run on schedules or events, execute multi‑step actions (email, HTTP requests, logging, etc.), and track run history with detailed logs.

---

## Features

### Workflow Automation
- Create workflows composed of triggers and multi‑step actions  
- JSON‑based workflow definitions  
- Sequential step execution with branching support (future)

### Triggers
- Cron‑based scheduling (run every minute, hour, day, etc.)  
- Manual triggers  
- Webhook/event triggers (planned)

### Actions
- Send emails  
- Make HTTP requests  
- Write logs  
- Slack notifications (planned)  
- Custom action registry for easy extension

### Orchestration Engine
- Background worker executes workflows step‑by‑step  
- Retry logic (planned)  
- Delays & wait steps (planned)  
- Execution logs stored per step

### Monitoring & Logs
- Workflow run history  
- Step‑level logs  
- Error tracking  
- Execution timeline (planned)

### Frontend
- React‑based dashboard  
- Workflow list  
- Workflow editor (form‑based → visual builder planned)  
- Run history viewer  
- Run detail page

---

## Tech Stack

### Backend
- Python (FastAPI)
- PostgreSQL (or SQLite for development)
- Background worker (Python)

### Frontend
- React + Vite
- TypeScript (optional but recommended)

### Infrastructure
- Docker & Docker Compose
- Shared types & utilities across services