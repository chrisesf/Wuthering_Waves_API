from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from src.resonators.enum import CharacterRarity, Element
from src.weapons.enum import WeaponType

class ResonatorBase(BaseModel):
    name: str
    description: str | None = None
    rarity: CharacterRarity
    element: Element
    weapon_type: WeaponType

    hp: int
    attack: float
    defense: float
    crit_rate: float
    crit_dmg: float
    energy_regen: float
    elemental_damage: float
    healing_bonus: float


class ResonatorCreate(ResonatorBase):
    pass


class ResonatorUpdate(ResonatorBase):
    pass


class ResonatorRead(ResonatorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
