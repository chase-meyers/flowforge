from worker.step_handlers.email_handler import handle_email_step
from worker.step_handlers.http_handler import handle_http_step
from worker.step_handlers.log_handler import handle_log_step


def load_workflow_definition(workflow_run: dict) -> dict:
    """Placeholder for workflow definition loading."""
    return workflow_run.get("definition", {})


def execute_step(step: dict, context: dict) -> None:
    step_type = step.get("type")

    if step_type == "email":
        handle_email_step(step, context)
    elif step_type == "http":
        handle_http_step(step, context)
    elif step_type == "log":
        handle_log_step(step, context)


def dispatch_workflow_run(workflow_run: dict) -> None:
    workflow_definition = load_workflow_definition(workflow_run)
    steps = workflow_definition.get("steps", [])
    context = {"workflow_run": workflow_run}

    for step in steps:
        execute_step(step, context)
