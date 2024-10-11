from sqlalchemy import String, Enum, Boolean, ForeignKey, Integer, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import datetime
import enum

from app.db.admin.base import Base

class TenantStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(Enum(TenantStatus, name="tenantstatus"), default=TenantStatus.ACTIVE, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())

    users: Mapped[List["User"]] = relationship("UserTenant", back_populates="tenant")

    database: Mapped[Optional["Database"]] = relationship("Database", back_populates="tenant", uselist=False)

    def __repr__(self):
        return f"<Tenant(id={self.id}, name={self.name})>"