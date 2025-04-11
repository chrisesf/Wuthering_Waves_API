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

    base_hp: Mapped[float] = mapped_column(Float)
    base_attack: Mapped[float] = mapped_column(Float)
    base_defense: Mapped[float] = mapped_column(Float)
    base_crit_rate: Mapped[float] = mapped_column(Float)
    base_crit_dmg: Mapped[float] = mapped_column(Float)
    base_energy_regen: Mapped[float] = mapped_column(Float)
    base_damage: Mapped[float] = mapped_column(Float)

    # Relationships
    faction: Mapped["Faction"] = relationship(back_populates="resonators")
    active_skills = relationship("ActiveSkill", back_populates="resonator")
    passive_skills = relationship("PassiveSkill", back_populates="resonator")
    concerto_skills = relationship("ConcertoSkill", back_populates="resonator")
    resonance_chains = relationship("ResonanceChain", back_populates="resonator")
    ascension_costs = relationship("AscensionCost", back_populates="resonator")
