#!/usr/bin/python3
""" Task 1 >> FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache Class"""

    def __init__(self):
        """Constructor Method"""
        super().__init__()
        self.list_name = []

    def put(self, key, item):
        """Put Method"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key not in self.list_name:
            self.list_name.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(self.list_name[0]))
            del self.cache_data[self.list_name[0]]
            self.list_name.pop(0)

    def get(self, key):
        """Get Method"""
        if key is None or key is not self.cache_data:
            return None
        return self.cache_data[key]
