from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete
from src.resonators.models import Resonator
from src.resonators.schemas import ResonatorCreate, ResonatorUpdate
from typing import List, Optional

async def create_resonators(
    db: AsyncSession, resonators_data: List[ResonatorCreate]
) -> List[Resonator]:
    resonators = [Resonator(**res.model_dump()) for res in resonators_data]
    db.add_all(resonators)
    await db.commit()
    for r in resonators:
        await db.refresh(r)
    return resonators


async def get_resonator(db: AsyncSession, resonator_id: int) -> Optional[Resonator]:
    result = await db.execute(select(Resonator).where(Resonator.id == resonator_id))
    return result.scalar_one_or_none()


async def get_all_resonators(db: AsyncSession) -> List[Resonator]:
    result = await db.execute(select(Resonator))
    return result.scalars().all()


async def update_resonator(
    db: AsyncSession, resonator_id: int, data: ResonatorUpdate
) -> Optional[Resonator]:
    result = await db.execute(select(Resonator).where(Resonator.id == resonator_id))
    resonator = result.scalar_one_or_none()
    if resonator is None:
        return None

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(resonator, field, value)

    await db.commit()
    await db.refresh(resonator)
    return resonator


async def delete_resonator(db: AsyncSession, resonator_id: int) -> bool:
    result = await db.execute(select(Resonator).where(Resonator.id == resonator_id))
    resonator = result.scalar_one_or_none()
    if resonator is None:
        return False

    await db.delete(resonator)
    await db.commit()
    return True
