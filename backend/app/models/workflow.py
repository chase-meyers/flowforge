from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, JSON, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Workflow(Base, TimestampMixin):
    __tablename__ = "workflows"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id"), nullable=False)

    trigger: Mapped[dict] = mapped_column(JSON, nullable=False)
    steps: Mapped[list] = mapped_column(JSON, nullable=False)
    edges: Mapped[list] = mapped_column(JSON, nullable=False)

    user: Mapped["User"] = relationship(back_populates="workflows")
    runs: Mapped[list["WorkflowRun"]] = relationship(back_populates="workflow")
    step_runs: Mapped[list["StepRun"]] = relationship(back_populates="workflow")
