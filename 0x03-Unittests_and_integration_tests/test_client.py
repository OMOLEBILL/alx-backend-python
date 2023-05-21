#!/usr/bin/env python3
""" We test the client module
"""


from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import (
    Dict
)


class TestGithubOrgClient(TestCase):
    """We impelement a class to test the TestGithubOrgClient"""
    @parameterized.expand([
        ("google", {"ping": "pong"}),
        ("abc", {"pined": "yes"})
    ])
    @patch("client.get_json")
    def test_org(self, url: str, expected: Dict, mocked: Mock):
        """ We test the org method"""
        mocked.return_value = expected
        instance = GithubOrgClient(url)
        self.assertEqual(instance.org, expected)
        mocked.assert_called_once()
