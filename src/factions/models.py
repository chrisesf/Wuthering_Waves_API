from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from src.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resonators.models import Resonator

class Faction(Base):
    __tablename__ = "factions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    resonators: Mapped[list["Resonator"]] = relationship(back_populates="faction")
