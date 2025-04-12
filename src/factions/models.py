from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from src.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resonators.models import Resonator

class Faction(Base):
    __tablename__ = "factions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text)

    resonators: Mapped[list["Resonator"]] = relationship(back_populates="faction")
