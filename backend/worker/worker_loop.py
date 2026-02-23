import time

from worker.job_dispatcher import dispatch_workflow_run

POLL_INTERVAL_SECONDS = 5


def poll_pending_workflow_runs() -> list[dict]:
    """Placeholder polling method for pending workflow runs."""
    return []


def run_worker_loop() -> None:
    while True:
        pending_runs = poll_pending_workflow_runs()

        for workflow_run in pending_runs:
            dispatch_workflow_run(workflow_run)

        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    run_worker_loop()
