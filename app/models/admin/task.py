from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from app.db.admin.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[int] = mapped_column(String(100), nullable=False)
    description: Mapped[int] = mapped_column(String(255), nullable=True)

    users: Mapped[List["User"]] = relationship("UserTask", back_populates="task",)

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name})>"
