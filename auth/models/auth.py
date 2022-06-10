from __future__ import annotations
from typing import Union

from main import Window
from datetime import datetime
from app.models.user import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from PyQt5.QtWidgets import QMainWindow
from auth.contollers import authentication
from settings.settings import COMPUTER_NAME
from sqlalchemy.exc import ProgrammingError
from settings.database import db_session, Base, database
from sqlalchemy import Column, Integer, String, DateTime


class Auth(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    computer_name = Column(String(255))
    date = Column(DateTime, default=datetime.now())
    language = Column(String(255), default='en')

    user = relationship("User", back_populates="sessions")

    @staticmethod
    def check_session() -> bool:
        try:
            session = db_session.query(Auth).filter(Auth.computer_name == COMPUTER_NAME).first()
            if not session:
                return False
            return True
        except ProgrammingError:
            Base.metadata.create_all(database)

    @staticmethod
    def get_session() -> Union[Auth, bool]:
        session = db_session.query(Auth).filter(Auth.computer_name == COMPUTER_NAME).first()
        if session:
            return session
        return False

    @staticmethod
    def write_session(user_id: int, instance: QMainWindow) -> None:
        new_session = Auth(
            user=db_session.get(User, user_id),
            computer_name=COMPUTER_NAME
        )
        db_session.add(
            new_session
        )
        db_session.commit()
        instance.main = Window()
        instance.main.show()
        instance.hide()

    @staticmethod
    def set_language(lang: str) -> None:
        session = Auth.get_session()
        session.language = lang
        db_session.commit()

    @staticmethod
    def forget_session(instance: QMainWindow) -> None:
        db_session.delete(
            db_session.query(Auth).filter(Auth.computer_name == COMPUTER_NAME).first()
        )
        db_session.commit()
        instance.login = authentication.LoginController()
        instance.login.show()
        instance.main_window.hide()
