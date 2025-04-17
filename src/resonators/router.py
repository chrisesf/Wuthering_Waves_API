from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.database import get_async_session
from src.resonators import crud
from src.resonators.schemas import ResonatorCreate, ResonatorUpdate, ResonatorRead

router = APIRouter(prefix="/resonators", tags=["Resonators"])


@router.post(
    "/", response_model=List[ResonatorRead], status_code=status.HTTP_201_CREATED
)
async def create_resonators(
    resonators_data: List[ResonatorCreate],
    db: AsyncSession = Depends(get_async_session),
):
    return await crud.create_resonators(db, resonators_data)


@router.get("/", response_model=List[ResonatorRead])
async def get_all_resonators(db: AsyncSession = Depends(get_async_session)):
    return await crud.get_all_resonators(db)


@router.get("/{resonator_id}", response_model=ResonatorRead)
async def get_resonator(
    resonator_id: int, db: AsyncSession = Depends(get_async_session)
):
    resonator = await crud.get_resonator(db, resonator_id)
    if not resonator:
        raise HTTPException(status_code=404, detail="Resonator not found")
    return resonator


@router.put("/{resonator_id}", response_model=ResonatorRead)
async def update_resonator(
    resonator_id: int,
    data: ResonatorUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    updated = await crud.update_resonator(db, resonator_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Resonator not found")
    return updated


@router.delete("/{resonator_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_resonator(
    resonator_id: int, db: AsyncSession = Depends(get_async_session)
):
    deleted = await crud.delete_resonator(db, resonator_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Resonator not found")
