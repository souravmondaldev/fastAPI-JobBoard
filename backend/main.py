from fastapi import FastAPI
from core.config import settings
from DB.session import engine
from DB.base import Base
from apis.base import api_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,
                  VERSION=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}
