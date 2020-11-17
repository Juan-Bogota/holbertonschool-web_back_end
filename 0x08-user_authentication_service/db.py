#!/usr/bin/env python3
"""Module: Database and SQLAlchemy Libraries"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """Class: Database Method: _session, add_user, find_user_by"""

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
        """ Method: Takes in arbitrary keyword arguments(kwargs)
        Return: First row found in the users table as filtered by arguments
        """
        if not kwargs:
            raise InvalidRequestError

        c_names = User.__table__.columns._data.keys()

        for key in kwargs.keys():
            if key in c_names:
                ed_user = self._session.query(User).filter_by(**kwargs).first()
                if ed_user is None:
                    raise NoResultFound
                return ed_user
        raise InvalidRequestError
