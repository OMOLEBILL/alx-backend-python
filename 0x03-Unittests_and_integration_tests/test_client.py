#!/usr/bin/env python3
""" We test the client module
"""


from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """We test the _public_repos_url"""
        expected = "https://api.github.com/orgs/google/repos"
        diction = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch("client.GithubOrgClient.org",
                   PropertyMock(return_value=diction)):
            Instance = GithubOrgClient("added")
            self.assertEqual(Instance._public_repos_url, expected)

    @patch("client.get_json")
    def test_public_repos(self, Mocked: Mock):
        """ We test the public_repos"""
        Mocked.return_value = {"repos_url": {"name": "fatal not a git repo"}}
        result = "fatal not a git repo"
        with patch("client.GithubOrgClient._public_repos_url",
                   PropertyMock(return_value=result)):
            Instance = GithubOrgClient("added")
            self.assertCountEqual(Instance._public_repos_url, result)
