from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.database import engine, SessionLocal
from src.pereval import models, schemas, crud
from src.pereval.models import PerevalAdded
# from src.database import get_async_session
from src.pereval.schemas import PerevalCreate, PerevalUpdate

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/pereval",
    tags=['Pereval']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/submitData/", response_model=list[schemas.Pereval])
def read_pereval(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pereval = crud.get_specific_pereval(db, skip=skip, limit=limit)
    return pereval


@router.get("/submitData/email")
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


@router.get("/submitData/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_user_by_email(db, skip=skip, limit=limit)
    return users


@router.post("/submitData", response_model=schemas.PerevalCreate)
def create_pereval(pereval: schemas.PerevalCreate, db: Session = Depends(get_db)):
    db_pereval = crud.get_specific_pereval(db)
    if db_pereval:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_pereval(db=db, pereval=pereval)


# @router.post("/submitData/<id>")
# async def add_pereval(new_pereval: PerevalCreate, session: AsyncSession = Depends(get_async_session)):
#     pereval_smtm = insert(pereval_added).values(new_pereval.dict(
#         add_time=pereval_added.add_time,
#         title=pereval_added.title,
#         other_titles=pereval_added.other_titles,
#         beauty_title=pereval_added.beauty_title,
#         content=pereval_added.content,
#         level_winter=pereval_added.level_winter,
#         level_summer=pereval_added.level_summer,
#         level_autumn=pereval_added.level_autumn,
#         level_spring=pereval_added.level_spring,
#         date_added=pereval_added.date_added,
#         latitude=coords.latitude,
#         longitude=coords.longitude,
#         height=coords.height,
#     ))
# user_smtm = insert(user).values(**new_pereval.dict(
#     email=user.email,
#     username=user.username,
#     phone=user.phone,
# ))
# coords_smtm = insert(coords).values(**new_pereval.dict(
#     latitude=coords.latitude,
#     longitude=coords.longitude,
#     height=coords.height,
# ))
# pereval_status = insert(pereval_added).values(status_id=1)
# await session.execute(pereval_smtm)
# await session.execute(user_smtm)
# await session.execute(coords_smtm)
# await session.execute(pereval_status)
# print('new_pereval', new_pereval)
# return {'status': 'Успешно'}


@router.patch("/submitData/<id>", response_model=schemas.Pereval)
def update_pereval(pereval_id: int, update_pereval: schemas.PerevalUpdate, db: Session = Depends(get_db)):
    if PerevalAdded.status_id == 1:
        return crud.create_pereval(db=db, update_pereval=update_pereval, pereval_id=pereval_id)
    else:
        return {'status': 'Невозможно, данные уже на модерации'}

# @router.patch("/submitData/<id>")
# async def update_pereval(update_pereval: PerevalUpdate, session: AsyncSession = Depends(get_async_session)):
#     update_data = update(pereval_added).values(**update_pereval.dict(
#         title=pereval_added.title,
#         other_titles=pereval_added.other_titles,
#         beauty_title=pereval_added.beauty_title,
#         content=pereval_added.content,
#         level_winter=pereval_added.level_winter,
#         level_summer=pereval_added.level_summer,
#         level_autumn=pereval_added.level_autumn,
#         level_spring=pereval_added.level_spring,
#         date_added=pereval_added.date_added,
#         latitude=coords.latitude,
#         longitude=coords.longitude,
#         height=coords.height,)
#     )
#     if pereval_added.status_id == 1:
#         await session.execute(update_data)
#         return {'status': 'Успешно'}
#     else:
#         return {'status': 'Невозможно, данные уже на модерации'}
