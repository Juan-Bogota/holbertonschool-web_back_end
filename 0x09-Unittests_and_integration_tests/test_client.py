#!/usr/bin/env python3
"""Module Test Github org client
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch, PropertyMock
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
        test = GithubOrgClient(test_url)
        info = test.org

        self.assertEqual(test_payload, info)

    def test_public_repos_url(self):
        """Method: Test Public Repository URL"""
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock,
                          return_value={"repos_url": "google"}) as mock_req:
            thing = GithubOrgClient('google')
            repos = thing._public_repos_url
            """mock_request.assert_called_once"""

        self.assertEqual(repos, mock_req.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(
         self, mock_get: Any) -> Any:
        """Method: Test Public Repos"""
        mock_get.return_value = [{"name": "google"}]
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value={"repos_url": "google"}) as mock_req:
            thing = GithubOrgClient('google')
            repos = thing.public_repos()
            self.assertEqual(['google'], repos)
            mock_req.assert_called_once()
            mock_get.assert_called_once()
