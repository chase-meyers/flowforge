from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class WorkflowBase(BaseModel):
    name: str
    user_id: UUID = Field(alias="userId")
    trigger: dict[str, Any]
    steps: list[dict[str, Any]]
    edges: list[dict[str, Any]]

    model_config = ConfigDict(populate_by_name=True)


class WorkflowCreate(WorkflowBase):
    pass


class WorkflowUpdate(BaseModel):
    name: str | None = None
    user_id: UUID | None = Field(default=None, alias="userId")
    trigger: dict[str, Any] | None = None
    steps: list[dict[str, Any]] | None = None
    edges: list[dict[str, Any]] | None = None

    model_config = ConfigDict(populate_by_name=True)


class WorkflowRead(WorkflowBase):
    id: UUID
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
