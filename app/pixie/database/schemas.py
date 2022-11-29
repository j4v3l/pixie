from typing import Union, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[dict, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    hashed_password: str

    class Config():
        orm_mode = True


class UserDestroy(BaseModel):

    class Config():

        orm_mode = True


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(UserBase):
    email: Optional[str] = None
