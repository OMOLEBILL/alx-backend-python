#!/usr/bin/env python3
""" We test the client module
"""


from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """ We test the has license method"""
        instance = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(instance, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """ We try to introduce intergraion testing"""
    @classmethod
    def setUpClass(cls) -> None:
        """We set the class"""
        own = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        own_mock = Mock()
        own_mock.json = Mock(return_value=own)
        cls.own_mock = own_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch("requests.get")
        cls.get = cls.get_patcher.start()
        Dict = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda x: Dict.get(x, own_mock)

    @classmethod
    def tearDownClass(cls) -> None:
        """stops the get_patcher"""
        cls.get_patcher.stop()
