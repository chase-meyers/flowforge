from fastapi import FastAPI

from app.api.routes import auth, workflows

app = FastAPI(title="FlowForge API")

app.include_router(workflows.router, prefix="/workflows", tags=["workflows"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
