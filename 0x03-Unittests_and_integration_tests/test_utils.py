#!/usr/bin/env python3
""" We test the access_nested_map method from the utils
    module
"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any
)
access_nested_map = __import__("utils").access_nested_map


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
