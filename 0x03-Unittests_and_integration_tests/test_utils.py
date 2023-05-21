#!/usr/bin/env python3
""" We test the access_nested_map method from the utils
    module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Dict,
    Any
)
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """ We implement a base class to test the utils class"""
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path:
                               Sequence, expected: Any):
        """WE test the access_nested_map
        args:
            nested_map : the nested dictionary
            path: the sequence of the keys to the dictionary
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """We test if a keyError is raised
        args:
            @nested_map : the nested dictionary
            @path : the sequence containg keys to the dict
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ We test the get_json method from the utils module"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """ We test the get_json method
            args:
                @test_url the unique resource locator
                @test_payload the expected dictionary
        """
        mocked = Mock()
        mocked.json.return_value = test_payload
        with patch("requests.get", return_value=mocked) as mock_request:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_request.assert_called_once()


class TestMemoize(unittest.TestCase):
    """We test the memoize method from the utils.py"""

    def test_memoize(self):
        """We test the memoize method"""
        class TestClass:
            """Class to test memoize"""

            def a_method(self):
                """Weturn 42 if the a_method is called"""
                return 42

            @memoize
            def a_property(self):
                """We return the a_method"""
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mocked:
            test_class = TestClass()
            result = test_class.a_property
            result = test_class.a_property
            self.assertEqual(result, 42)
            mocked.assert_called_once()
