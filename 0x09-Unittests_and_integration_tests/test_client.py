#!/usr/bin/env python3
"""Module Test Github org client
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Class: Test GitHub Org Client"""
    @parameterized.expand([
        ("http://google.com", {"payload": True}),
        ("http://abc.com", {"payload": False}),
    ])
    @patch('test_client.get_json')
    def test_org(
         self, test_url: str, test_payload: dict,  mock_get: Any) -> Any:
        """Method: Test Org"""
        mock_get.return_value = test_payload
        data = get_json(test_url)
        self.assertEqual(data, test_payload)
