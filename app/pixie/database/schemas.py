from typing import Union, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    """Base class for Item schema"""
    title: str
    description: Union[dict, None] = None


class ItemCreate(ItemBase):
    """Schema for creating an item"""
    pass


class Item(ItemBase):
    """Schema for an item"""
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    """Base class for User schema"""
    email: str


class UserCreate(UserBase):
    """Schema for creating a user password which extends UserBase"""
    password: str


class UserUpdate(BaseModel):
    """Schema for updating a user"""
    hashed_password: str

    class Config:
        orm_mode = True


class UserDestroy(BaseModel):
    """Schema for deleting a user"""

    class Config:

        orm_mode = True


class User(UserBase):
    """Schema for a user"""
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    """Schema for logging in a user"""
    username: str
    password: str


class Token(BaseModel):
    """Schema for a token"""
    access_token: str
    token_type: str


class TokenData(UserBase):
    """Schema for token data"""
    email: Optional[str] = None
