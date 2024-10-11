from datetime import datetime
from sqlalchemy import String, Boolean, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.db.admin.base import Base


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="client", uselist=False)
    
    def __repr__(self):
        return f"<Client(id={self.id}, user_id={self.user_id})>"