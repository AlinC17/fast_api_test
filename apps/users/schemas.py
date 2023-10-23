from sqlalchemy import Column, String, Boolean
from database import Base
from utils.orm.mixins import DefaultTable


class User(Base, DefaultTable):
    __tablename__ = 'users'
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    banned = Column(Boolean, default=False)
    ban_reason = Column(String, nullable=True)
