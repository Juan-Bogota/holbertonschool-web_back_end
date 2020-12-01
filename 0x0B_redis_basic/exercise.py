#!/usr/bin/env python3
"""Module: Redis Server"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Method: Constructor Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method: should generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
