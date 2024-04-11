from sqlalchemy import  Column, Integer, String, DDL
from sqlalchemy.types import Enum
from database import Base,engine
from enum import Enum as PyEnum

class IsActiveEnum(PyEnum):
    ACTIVE = 1
    INACTIVE = 0

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    login_id = Column(Integer, index=True)
    username = Column(String(45))
    firstname = Column(String(45))
    lastname = Column(String(45))
    photo = Column(String(45))
    isactive = Column(Enum(IsActiveEnum), default=IsActiveEnum.ACTIVE)


alter_enum_default = DDL("ALTER TABLE users ALTER COLUMN isactive SET DEFAULT 'ACTIVE';")
with engine.connect() as connection:
    connection.execute(alter_enum_default)
