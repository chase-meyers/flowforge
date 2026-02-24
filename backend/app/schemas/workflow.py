from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class WorkflowCreate(BaseModel):
    name: str
    trigger: dict[str, Any]
    steps: list[dict[str, Any]]
    edges: list[dict[str, Any]]


class WorkflowUpdate(BaseModel):
    name: str | None = None
    trigger: dict[str, Any] | None = None
    steps: list[dict[str, Any]] | None = None
    edges: list[dict[str, Any]] | None = None


class WorkflowRead(BaseModel):
    id: UUID
    name: str
    user_id: UUID = Field(alias="userId")
    trigger: dict[str, Any]
    steps: list[dict[str, Any]]
    edges: list[dict[str, Any]]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
