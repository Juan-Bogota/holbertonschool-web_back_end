#!/usr/bin/env python3
"""Module: Authentication"""
import bcrypt

def _hash_password(password: str) -> str:
    """Method: Return a string hash"""
    passwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed