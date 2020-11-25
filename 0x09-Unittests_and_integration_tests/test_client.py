#!/usr/bin/env python3
"""Module Test Github org client
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class: Test GitHub Org Client"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc",  {"payload": True}),
    ])
    @patch('client.get_json')
    def test_org(
         self, test_url: str, test_payload: dict, mock_get: Any) -> Any:
        """Method: Test Org - Git Hub"""
        mock_get.return_value = test_payload
        mock = GithubOrgClient(test_url)
        info = mock.org

        self.assertEqual(test_payload, info)
