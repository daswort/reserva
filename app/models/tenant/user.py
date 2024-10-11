from sqlalchemy import String, Boolean, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import datetime

from app.db.tenant.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_professional: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())

    # Relación con roles
    role_id: Mapped[Optional[int]] = mapped_column(ForeignKey("roles.id"))
    role: Mapped[Optional["Role"]] = relationship("Role", back_populates="users")
    
    # Relación con citas
    appointments: Mapped[List["Appointment"]] = relationship("Appointment", back_populates="user")
    
    # Relación con el perfil profesional si es un profesional
    professional: Mapped[Optional["Professional"]] = relationship("Professional", back_populates="user", uselist=False)