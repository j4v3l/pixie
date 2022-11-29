from fastapi import APIRouter, Depends, HTTPException, status
from ..database import database, models
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . hashing import Hash
from . import token


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED,
                            detail=f'User with the username {request.username} is not available')
    if not Hash.verify(user.hashed_password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid credentials')
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
