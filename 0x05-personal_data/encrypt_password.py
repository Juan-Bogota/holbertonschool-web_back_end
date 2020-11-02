#!/usr/bin/env python3
"""
Encript password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password"""
    pswd = bytes(password, encoding="utf-8")
    hashed = bcrypt.hashpw(pswd, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Is Valid"""
    if bcrypt.checkpw(password.encode('utf8'), hashed_password):
        return True
    else:
        return False
