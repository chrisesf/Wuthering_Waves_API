from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from factions.models import Faction

class Resonator(Base):
    __tablename__ = "resonators"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    rarity: Mapped[int] = mapped_column(Integer)
    element: Mapped[str] = mapped_column(String(50))
    weapon_type: Mapped[str] = mapped_column(String(50))
    faction_id: Mapped[int] = mapped_column(ForeignKey("factions.id"))

    hp: Mapped[float] = mapped_column(Integer, base=934)
    attack: Mapped[float] = mapped_column(Float)
    defense: Mapped[float] = mapped_column(Float)
    crit_rate: Mapped[float] = mapped_column(Float)
    crit_dmg: Mapped[float] = mapped_column(Float)
    energy_regen: Mapped[float] = mapped_column(Float)
    elemental_damage: Mapped[float] = mapped_column(Float)
    healing_bonus: Mapped[float] = mapped_column(Float)

    # Relationships
    faction: Mapped["Faction"] = relationship(back_populates="resonators")
    active_skills = relationship("ActiveSkill", back_populates="resonator")
    passive_skills = relationship("PassiveSkill", back_populates="resonator")
    concerto_skills = relationship("ConcertoSkill", back_populates="resonator")
    resonance_chains = relationship("ResonanceChain", back_populates="resonator")
    ascension_costs = relationship("AscensionCost", back_populates="resonator")
    stats_per_level = relationship(
        "ResonatorStatsPerLevel",
        back_populates="resonator",
        cascade="all, delete-orphan",
    )

class ResonatorStatsPerLevel(Base):
    __tablename__ = "resonator_stats_per_level"

    resonator_id = Mapped[int] = mapped_column(
        ForeignKey("resonators.id", ondelete="CASCADE"), primary_key=True, index=True
    )
    level: Mapped[int] = mapped_column(primary_key=True, index=True)

    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)

    resonator = relationship("Resonator", back_populates="stats_per_level")
