#!/usr/bin/python3
""" Task 0 >> Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache Class"""

    def put(self, key, item):
        """Put Method"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get Method"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
