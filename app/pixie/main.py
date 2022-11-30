from fastapi import FastAPI
from .database.database import engine
from .database import models
from .routers import item, user
from .auth import authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(item.router)
app.include_router(user.router)
