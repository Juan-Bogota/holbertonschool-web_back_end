#!/usr/bin/env python3
"""
Module: Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    This class is the template for all authentication
    system you will implement.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method: Required Authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method: Authorization Header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method: Current User"""
        return None
