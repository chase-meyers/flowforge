from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, JSON, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class StepRun(Base, TimestampMixin):
    __tablename__ = "step_runs"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id"), nullable=False)
    workflow_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("workflows.id"), nullable=False)
    workflow_run_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("workflow_runs.id"),
        nullable=False,
    )

    trigger: Mapped[dict] = mapped_column(JSON, nullable=False)
    steps: Mapped[list] = mapped_column(JSON, nullable=False)
    edges: Mapped[list] = mapped_column(JSON, nullable=False)

    user: Mapped["User"] = relationship(back_populates="step_runs")
    workflow: Mapped["Workflow"] = relationship(back_populates="step_runs")
    workflow_run: Mapped["WorkflowRun"] = relationship(back_populates="step_runs")
