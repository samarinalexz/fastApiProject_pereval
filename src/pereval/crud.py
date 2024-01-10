from sqlalchemy.orm import Session

from src.pereval import schemas, models


def get_specific_pereval(db: Session, pereval_id: int):
    return db.query(models.PerevalAdded).filter(models.PerevalAdded.id == pereval_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_pereval(db: Session, pereval: schemas.PerevalCreate):
    db_pereval = models.PerevalAdded(id=pereval.id)
    db.add(db_pereval)
    db.commit()
    db.refresh(db_pereval)
    return db_pereval