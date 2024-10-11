from sqlalchemy import String, Boolean, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import datetime

from app.db.admin.base import Base

class Database(Base):
    __tablename__ = "databases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(16), nullable=False)
    user: Mapped[str] = mapped_column(String(16), nullable=False)
    password: Mapped[str] = mapped_column(String(16), nullable=False)

    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), unique=True)
    tenant: Mapped["Tenant"] = relationship("Tenant", back_populates="database")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())


    