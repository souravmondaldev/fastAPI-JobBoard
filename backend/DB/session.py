from typing import Generator
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import false

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine) 
def get_db()-> Generator:
    try:
        db= SessionLocal()
        yield db  
    finally:
         db.close()
 
