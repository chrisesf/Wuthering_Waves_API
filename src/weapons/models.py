from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base
from typing import TYPE_CHECKING