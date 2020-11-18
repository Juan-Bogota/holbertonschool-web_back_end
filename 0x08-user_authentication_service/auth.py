#!/usr/bin/env python3
"""Module: Authentication"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """Function: Return a string hash of the input password"""
    passwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def _generate_uuid() -> str:
    """Function: Generate UUIDs"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Method: Constructor"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method: Register new User"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user
        raise ValueError('User {} already exists'.format(user.email))

    def valid_login(self, email: str, password: str) -> bool:
        """Method: Credentials Validation"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Method: Get session ID """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        user.session_id = _generate_uuid()
        return user.session_id
