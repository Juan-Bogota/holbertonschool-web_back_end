#!/usr/bin/env python3
"""Module: Test Unittest
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Class: Test Access Nested Map Function"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> Any:
        """Method: Test Access Nested Map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",), 1),
                           ({"a": 1}, ("a", "b"), {"b": 2})])
    def test_access_nested_map_exception(
         self, nested_map: Mapping, path: Sequence, expected: Any) -> Any:
        """Method: Test Access Nested Map Exception"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """Class: Test Get Json(Javasript On Notation)"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(
         self, test_url: str, test_payload: dict,  mock_get: Any) -> Any:
        """Method: Test Get JSON - Mockup"""
        mock_get.return_value = test_payload
        data = get_json(test_url)
        self.assertEqual(data, test_payload)


class TestMemoize(unittest.TestCase):
    """Class: Test Memoize"""

    def test_memoize(self):
        """Method: Test Memoize"""
        class TestClass:
            """Class: Test CLass Memoize"""
            def a_method(self):
                """Method: A method"""
                return 42

            @memoize
            def a_property(self):
                """Decorator to memoize a method."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            thing = TestClass()
            thing.a_property()

        mock_method.assert_called_once()
