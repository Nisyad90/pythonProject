
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status, Depends

from .database import get_db
from .routers import user


def create(request: schemas.User, db:Session):
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def get(id: int, db: Session):
    return db.query(models.User).filter(models.User.id == id).first()

def update(id: int, request: schemas.UserUpdate, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    for attr, value in request.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    db.commit()
    db.refresh(user)
    return user

def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    db.delete(user)
    db.commit()
    return {"message": f"User with id {id} has been deleted successfully"}