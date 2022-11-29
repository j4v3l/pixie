from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import crud, models, schemas
from ..database.database import SessionLocal, engine, get_db
from .. auth import oauth2

router = APIRouter(
    tags=['Items']
)


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/item/{id}", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
