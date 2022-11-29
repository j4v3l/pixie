from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import crud, models, schemas
from ..database.database import SessionLocal, engine, get_db
from ..auth import oauth2, authentication

router = APIRouter(
    tags=['Users']
)


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", response_model=schemas.UserDestroy)
def delete(user_id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_user = crud.delete_user(db, user_id=user_id)
    return db_user


@router.put("/users/{user_id}")
def update(user_id: int, request: schemas.UserUpdate, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_user = crud.update_user(user_id=user_id, request=request, db=db)
    return db_user


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
