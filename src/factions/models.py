from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime, ForeignKey
from src.database import Base
from sqlalchemy.sql import func
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resonators.models import Resonator

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

    faction_members: Mapped[list["FactionMember"]] = relationship(
        back_populates="faction", cascade="all, delete-orphan"
    )
    resonators: Mapped[list["Resonator"]] = relationship(
        secondary="faction_member", back_populates="factions"
    )


class FactionMember(Base):
    __tablename__ = "faction_member"

    resonator_id: Mapped[int] = mapped_column(
        ForeignKey("resonators.id"), primary_key=True
    )
    faction_id: Mapped[int] = mapped_column(ForeignKey("factions.id"), primary_key=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    resonator: Mapped["Resonator"] = relationship(back_populates="faction_members")
    faction: Mapped["Faction"] = relationship(back_populates="faction_members")
