from sqlalchemy import String, Boolean, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import datetime

from app.db.admin.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())

    role_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    role: Mapped[Optional["Role"]] = relationship("Role", back_populates="users")

    client: Mapped[Optional["Client"]] = relationship("Client", back_populates="user", uselist=False)

    users_tenants: Mapped[Optional[List["UserTenant"]]] = relationship(
        back_populates="user",
        cascade="save-update, merge, " "delete, delete-orphan",
    )
    
    users_tasks: Mapped[Optional[List["UserTask"]]] = relationship(
        back_populates="user",
        cascade="save-update, merge, " "delete, delete-orphan",
    )

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"