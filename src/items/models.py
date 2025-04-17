from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from src.database import Base
from datetime import datetime
from src.items.enum import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resonators.models import Resonator


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[ItemType] = mapped_column(Enum(ItemType), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    ascension_costs: Mapped[list["AscensionCost"]] = relationship(
        "AscensionCost", back_populates="item", cascade="all, delete-orphan"
    )


class AscensionCost(Base):
    __tablename__ = "ascension_costs"

    character_id: Mapped[int] = mapped_column(
        ForeignKey("resonators.id", ondelete="CASCADE"), primary_key=True
    )
    item_id: Mapped[int] = mapped_column(
        ForeignKey("items.id", ondelete="CASCADE"), primary_key=True
    )
    tier: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    resonator: Mapped["Resonator"] = relationship(
        "Resonator", back_populates="ascension_costs"
    )
    item: Mapped["Item"] = relationship("Item", back_populates="ascension_costs")
