from sqlalchemy.orm import Session
from . import models, schemas
from .. auth.hashing import Hash


def get_user(db: Session, user_id: int):
    """Get use by ID from the database"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """Get use by email from the database"""
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get all users from the database 100 at a time"""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user in the database"""
    password = user.password
    db_user = models.User(
        email=user.email, hashed_password=Hash.bcrypt(password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, request: schemas.UserUpdate, db: Session):
    """Update a user password in the database"""
    db_user = db.query(models.User).filter(models.User.id == user_id)
    if not db_user.first():
        return None
    password = request.dict().get('hashed_password')
    db_user.update({'hashed_password': Hash.bcrypt(password)})
    db.commit()
    return {"success": True}


def delete_user(db: Session, user_id: int):
    """Delete a user from the database"""
    db_user = db.query(models.User).filter(models.User.id == user_id)
    db_user.delete(synchronize_session=False)
    db.commit()
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """Get all items from the database 100 at a time"""
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """Cretes a list of items for a user in the database"""
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
