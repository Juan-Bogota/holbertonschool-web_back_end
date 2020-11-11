#!/usr/bin/env python3
"""
Module: Session Auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ CLass: Session Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Method:creates a Session ID"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method: User ID for session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Method: Current User Session ID"""
        valueCookie = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(valueCookie)
        return User.get(user_id)
