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
