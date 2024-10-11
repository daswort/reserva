from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from app.db.tenant.base import Base

class Professional(Base):
    __tablename__ = "professionals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    specialty: Mapped[str] = mapped_column(String(100), nullable=False)
    biography: Mapped[Optional[str]] = mapped_column(String(500))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="professional")
    
    # Relación con las citas que el profesional tiene
    appointments: Mapped[List["Appointment"]] = relationship("Appointment", back_populates="professional")

