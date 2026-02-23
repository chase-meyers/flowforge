from uuid import UUID, uuid4

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    workflows: Mapped[list["Workflow"]] = relationship(back_populates="user")
    workflow_runs: Mapped[list["WorkflowRun"]] = relationship(back_populates="user")
    step_runs: Mapped[list["StepRun"]] = relationship(back_populates="user")
