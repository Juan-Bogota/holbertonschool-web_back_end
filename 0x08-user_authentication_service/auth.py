#!/usr/bin/env python3
"""Module: Authentication"""
import bcrypt

def _hash_password(password: str) -> str:
    """Method: Return a string is a salted hash of the input password"""
    passwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed