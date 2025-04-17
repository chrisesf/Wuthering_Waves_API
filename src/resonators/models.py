from __future__ import annotations
from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from src.database import Base
from datetime import datetime
from src.resonators.enum import *
from src.weapons.enum import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from factions.models import Faction, FactionMember

from src.factions.models import FactionMember

class Resonator(Base):
    __tablename__ = "resonators"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    rarity: Mapped[int] = mapped_column(Enum(CharacterRarity), nullable=False)
    element: Mapped[str] = mapped_column(Enum(Element), nullable=False)
    weapon_type: Mapped[str] = mapped_column(Enum(WeaponType), nullable=False)

    hp: Mapped[int] = mapped_column(Integer)
    attack: Mapped[int] = mapped_column(Float)
    defense: Mapped[int] = mapped_column(Float)
    crit_rate: Mapped[float] = mapped_column(Float)
    crit_dmg: Mapped[float] = mapped_column(Float)
    energy_regen: Mapped[float] = mapped_column(Float)
    elemental_damage: Mapped[float] = mapped_column(Float)
    healing_bonus: Mapped[float] = mapped_column(Float)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    faction_members: Mapped[list["FactionMember"]] = relationship(
        back_populates="resonator", cascade="all, delete-orphan"
    )
    factions: Mapped[list["Faction"]] = relationship(
        secondary="faction_member", back_populates="resonators"
    )
    skills: Mapped[list["Skill"]] = relationship(
        back_populates="resonator", cascade="all, delete-orphan"
    )
    resonance_chains: Mapped[list["ResonanceChain"]] = relationship(
        "ResonanceChain", back_populates="resonator"
    )
    stats_per_level: Mapped[list["ResonatorStatsPerLevel"]] = relationship(
        "ResonatorStatsPerLevel",
        back_populates="resonator",
        cascade="all, delete-orphan",
    )


class ResonatorStatsPerLevel(Base):
    __tablename__ = "resonator_stats_per_level"

    resonator_id: Mapped[int] = mapped_column(
        ForeignKey("resonators.id", ondelete="CASCADE"), primary_key=True, index=True
    )
    level: Mapped[int] = mapped_column(primary_key=True, index=True)
    hp: Mapped[int] = Column(Integer, nullable=False)
    attack: Mapped[int] = Column(Integer, nullable=False)
    defense: Mapped[int] = Column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    resonator: Mapped["Resonator"] = relationship(
        "Resonator", back_populates="stats_per_level"
    )

class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    resonator_id: Mapped[int] = mapped_column(
        ForeignKey("resonators.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    cooldown: Mapped[int | None] = mapped_column(nullable=True)
    energy_cost: Mapped[int | None] = mapped_column(nullable=True)
    skill_type: Mapped[SkillType] = mapped_column(Enum(SkillType), nullable=False)
    skill_category: Mapped[SkillCategory] = mapped_column(
        Enum(SkillCategory), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    resonator: Mapped["Resonator"] = relationship(back_populates="skills")


class ResonanceChain(Base):
    __tablename__ = "resonance_chains"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    resonator_id: Mapped[int] = mapped_column(
        ForeignKey("resonators.id", ondelete="CASCADE")
    )
    description: Mapped[str] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    resonator: Mapped["Resonator"] = relationship(back_populates="resonance_chains")

from src.items.models import AscensionCost

Resonator.ascension_costs = relationship(
    "AscensionCost", back_populates="resonator", cascade="all, delete-orphan"
)
