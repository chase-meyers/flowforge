from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.workflow import Workflow
from app.schemas.workflow import WorkflowCreate, WorkflowRead, WorkflowUpdate

router = APIRouter()

DEFAULT_USER_ID = UUID("00000000-0000-0000-0000-000000000001")


@router.get("/", response_model=list[WorkflowRead])
def list_workflows(db: Session = Depends(get_db)):
    result = db.scalars(select(Workflow))
    return result.all()


@router.get("/{id}", response_model=WorkflowRead)
def get_workflow(id: UUID, db: Session = Depends(get_db)):
    workflow = db.get(Workflow, id)
    if workflow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow not found")
    return workflow


@router.post("/", response_model=WorkflowRead, status_code=status.HTTP_201_CREATED)
def create_workflow(payload: WorkflowCreate, db: Session = Depends(get_db)):
    workflow = Workflow(
        name=payload.name,
        user_id=DEFAULT_USER_ID,
        trigger=payload.trigger,
        steps=payload.steps,
        edges=payload.edges,
    )
    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    return workflow


@router.put("/{id}", response_model=WorkflowRead)
def update_workflow(id: UUID, payload: WorkflowUpdate, db: Session = Depends(get_db)):
    workflow = db.get(Workflow, id)
    if workflow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow not found")

    for field, value in payload.model_dump(exclude_unset=True, by_alias=False).items():
        setattr(workflow, field, value)

    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    return workflow


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workflow(id: UUID, db: Session = Depends(get_db)):
    workflow = db.get(Workflow, id)
    if workflow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow not found")

    db.delete(workflow)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
