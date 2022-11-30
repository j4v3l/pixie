from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import crud, schemas
from ..database.database import get_db
from .. auth import oauth2

router = APIRouter(
    tags=['Items']
)


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    """Get all items with pagination """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/item/{id}", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    """Get item based on user ID"""
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
