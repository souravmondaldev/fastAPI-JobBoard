from fastapi import FastAPI
from core.config import settings
from DB.session import engine
from DB.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,
                  VERSION=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}
