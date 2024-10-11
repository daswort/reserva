from datetime import datetime
from sqlalchemy import Integer, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import Mapped, relationship, mapped_column
import enum

from app.db.admin.base import Base

class TaskStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    ERROR = "error"

class UserTask(Base):
    __tablename__ = "user_tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="users_tasks")

    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    task: Mapped["Task"] = relationship("Task", back_populates="users")

    status: Mapped[str] = mapped_column(Enum(TaskStatus, name="taskstatus"), default=TaskStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<UserTask(user_id={self.user_id}, task_id={self.task_id}, status={self.status})>"
