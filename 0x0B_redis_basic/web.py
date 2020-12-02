#!/usr/bin/env python3
""" Module: Redis Server,  Implementing an
expiring web cache and tracker"""
import redis
from typing import Union, Optional, Callable
import requests

redis = redis.Redis()
incr = 0


def get_page(my_url: str) -> str:
    """Function: expiring web cache and tracker"""

    response = requests.get(my_url)
    redis.set(f"cached:{my_url}", incr)
    redis.incr(f"count:{my_url}")
    redis.setex(f"cached:{my_url}", 10, r.get(f"cached:{my_url}"))
    return resp.text

get_page('http://slowwly.robertomurray.co.uk')
