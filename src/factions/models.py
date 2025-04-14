from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime
from src.database import Base
from sqlalchemy.sql import func
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resonators.models import Resonator, FactionMember

class Faction(Base):
    __tablename__ = "factions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    resonators: Mapped[list["Resonator"]] = relationship(back_populates="faction")
    members: Mapped[list["FactionMember"]] = relationship(
        back_populates="faction", cascade="all, delete-orphan"
    )
