import hashlib
from settings.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(255))
    password = Column(String(255))
    name = Column(String(255))
    salt = Column(String(255))

    sessions = relationship("Auth",  back_populates="user")

    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        password = password + salt
        return hashlib.sha512(password.encode('utf-8')).hexdigest()
