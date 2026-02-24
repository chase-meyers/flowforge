import time
from uuid import UUID

from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.workflow_run import WorkflowRun
from worker.job_dispatcher import dispatch_workflow_run

POLL_INTERVAL_SECONDS = 5


def poll_pending_workflow_run_ids() -> list[UUID]:
    with SessionLocal() as db:
        pending_runs = db.scalars(
            select(WorkflowRun).where(WorkflowRun.status == "pending")
        ).all()

        if not pending_runs:
            return []

        run_ids = [workflow_run.id for workflow_run in pending_runs]

        for workflow_run in pending_runs:
            workflow_run.status = "running"
            db.add(workflow_run)

        db.commit()
        return run_ids


def run_worker_loop() -> None:
    while True:
        pending_run_ids = poll_pending_workflow_run_ids()

        for workflow_run_id in pending_run_ids:
            dispatch_workflow_run(workflow_run_id)

        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    run_worker_loop()
