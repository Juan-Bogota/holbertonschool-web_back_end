#!/usr/bin/env python3
"""Module: Database"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """Class: Database"""

    def __init__(self):
        """Method: Constructor"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Method: Creating a Session"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Method: The method should save the user to the database."""
        ed_user = User(email=email, hashed_password=hashed_password)
        self._session.add(ed_user)
        self._session.commit()
        return ed_user

    def find_user_by(self, **kwargs) -> User:
        """This method takes in arbitrary keyword arguments and returns the first
        row found in the table as filtered by the method's input arguments."""

        ed_user = self._session.query(User).filter_by(**kwargs).first()

        if ed_user is None:
            raise NoResultFound
        return ed_user
