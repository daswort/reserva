from sqlalchemy import String, Boolean, ForeignKey, Integer, Enum, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import datetime

from app.db.admin.base import Base

class UserTenant(Base):
    __tablename__ = "users_tenants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    tenant_id: Mapped[int] = mapped_column(Integer, ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="users_tenants",)
    tenant: Mapped["Tenant"] = relationship("Tenant", back_populates="users")

    def __repr__(self):
        return f"<UserTenant(user_id={self.user_id}, tenant_id={self.task_id}, status={self.status})>"
    