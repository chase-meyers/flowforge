from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_workflows():
    pass


@router.get("/{workflow_id}")
def get_workflow(workflow_id: int):
    pass


@router.post("/")
def create_workflow():
    pass


@router.put("/{workflow_id}")
def update_workflow(workflow_id: int):
    pass


@router.delete("/{workflow_id}")
def delete_workflow(workflow_id: int):
    pass
