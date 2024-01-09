from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.pereval.models import pereval_added
from src.pereval.schemas import PerevalCreate

router = APIRouter(
    prefix="/pereval",
    tags=['Pereval']
)


@router.get("/")
async def get_specific_pereval(pereval_added_title: str, session: AsyncSession = Depends(get_async_session)):
    query = select(pereval_added).where(pereval_added.c.title == pereval_added_title)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_pereval(new_pereval: PerevalCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(pereval_added).values(**new_pereval.dict())
    await session.execute(stmt)
    return {'status': 'success'}