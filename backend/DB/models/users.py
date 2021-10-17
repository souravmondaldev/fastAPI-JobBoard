from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false

from DB.base_class import Base

class User(Base):
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, unique=True, nullable=False)
    email=Column(String, unique=True, nullable=False, index=True)
    hashed_password =Column(String, nullable=False)
    is_active=Column(Boolean(), default=True)
    is_superuser=Column(Boolean(), default=False)
    jobs=relationship("Job", back_populates="owner")