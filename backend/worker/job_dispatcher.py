from collections.abc import Callable
from uuid import UUID

from app.db.session import SessionLocal
from app.models.step_run import StepRun
from app.models.workflow_run import WorkflowRun
from worker.step_handlers.email_handler import handle_email_step
from worker.step_handlers.http_handler import handle_http_step
from worker.step_handlers.log_handler import handle_log_step

StepHandler = Callable[[dict, dict], None]

STEP_HANDLERS: dict[str, StepHandler] = {
    "email": handle_email_step,
    "http": handle_http_step,
    "log": handle_log_step,
}


def load_workflow_definition(workflow_run: WorkflowRun) -> dict:
    return {
        "trigger": workflow_run.trigger,
        "steps": workflow_run.steps,
        "edges": workflow_run.edges,
    }


def execute_step(step: dict, context: dict) -> None:
    step_type = step.get("type")
    handler = STEP_HANDLERS.get(step_type)

    if handler is None:
        raise ValueError(f"Unsupported step type: {step_type}")

    handler(step, context)


def create_step_run_log(
    workflow_run: WorkflowRun,
    step: dict,
    step_index: int,
    result_status: str,
    error_message: str | None = None,
) -> StepRun:
    log_entry = {
        "stepIndex": step_index,
        "status": result_status,
    }
    if error_message:
        log_entry["error"] = error_message

    return StepRun(
        name=step.get("name", f"step-{step_index + 1}"),
        user_id=workflow_run.user_id,
        workflow_id=workflow_run.workflow_id,
        workflow_run_id=workflow_run.id,
        trigger={"type": step.get("type")},
        steps=[step, log_entry],
        edges=[],
    )


def dispatch_workflow_run(workflow_run_id: UUID) -> None:
    with SessionLocal() as db:
        workflow_run = db.get(WorkflowRun, workflow_run_id)
        if workflow_run is None:
            return

        workflow_definition = load_workflow_definition(workflow_run)
        steps = workflow_definition.get("steps", [])
        context = {
            "workflow_run_id": str(workflow_run.id),
            "workflow_id": str(workflow_run.workflow_id),
        }

        try:
            for step_index, step in enumerate(steps):
                execute_step(step, context)
                db.add(
                    create_step_run_log(
                        workflow_run=workflow_run,
                        step=step,
                        step_index=step_index,
                        result_status="success",
                    )
                )

            workflow_run.status = "success"
            db.add(workflow_run)
            db.commit()
        except Exception as exc:
            failed_step_index = locals().get("step_index", -1)
            failed_step = locals().get("step", {"type": "unknown"})
            db.add(
                create_step_run_log(
                    workflow_run=workflow_run,
                    step=failed_step,
                    step_index=failed_step_index,
                    result_status="failed",
                    error_message=str(exc),
                )
            )
            workflow_run.status = "failed"
            db.add(workflow_run)
            db.commit()
