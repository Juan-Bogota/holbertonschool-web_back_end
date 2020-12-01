#!/usr/bin/env python3
"""Module: Redis Server"""

import redis
import uuid


class Cache:
    def __init__(self):
        """Method: Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """Method: should generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(data, key)
        return key
