# blog/routers/user.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, schemas, user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.put('/{id}', response_model=schemas.ShowUser)
def update_user(id: int, request: schemas.UserUpdate, db: Session = Depends(get_db)):
    existing_user = user.get(id, db)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user.update(id, request, db)

@router.delete('/{id}', response_model=dict)
def delete_user(id: int, db: Session = Depends(get_db)):
    existing_user = user.get(id, db)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    user.delete(id, db)
    return {"message": f"User with id {id} has been deleted successfully"}