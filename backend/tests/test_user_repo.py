import unittest

import os

from app import create_app
from app.repos.user import UserRepo
from settings import BASE_DIR


class UserRepoTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        with open(os.path.join(BASE_DIR, 'tests/users.json'), 'r') as f:
            self.repo = UserRepo(f.read())

    def test_should_get_by_email_success(self):
        expected = {
            "id": 1,
            "email": "test_user@t.ta",
            "password": "passw0rd",
            "access_token": "access token 1",
            "refresh_token": "refresh token 1"
        }
        actual = self.repo.get_by_email('test_user@t.ta')
        self.assertEqual(actual, expected)

    def test_should_get_by_email_failure(self):
        with self.assertRaises(self.repo.DoesNotExist):
            self.repo.get_by_email('invalid')

    def test_should_get_by_access_token_success(self):
        expected = {
            "id": 1,
            "email": "test_user@t.ta",
            "password": "passw0rd",
            "access_token": "access token 1",
            "refresh_token": "refresh token 1"
        }
        actual = self.repo.get_by_access_token('access token 1')
        self.assertEqual(actual, expected)

    def test_should_get_by_access_token_failure(self):
        with self.assertRaises(self.repo.DoesNotExist):
            self.repo.get_by_access_token('invalid')

    def test_should_get_by_refresh_token_success(self):
        expected = {
            "id": 1,
            "email": "test_user@t.ta",
            "password": "passw0rd",
            "access_token": "access token 1",
            "refresh_token": "refresh token 1"
        }
        actual = self.repo.get_by_refresh_token('refresh token 1')
        self.assertEqual(actual, expected)

    def test_should_get_by_refresh_token_failure(self):
        with self.assertRaises(self.repo.DoesNotExist):
            self.repo.get_by_refresh_token('invalid')

    def test_should_get_by_id_success(self):
        expected = {
            "id": 1,
            "email": "test_user@t.ta",
            "password": "passw0rd",
            "access_token": "access token 1",
            "refresh_token": "refresh token 1"
        }
        actual = self.repo.get_by_id(1)
        self.assertEqual(actual, expected)

    def test_should_get_by_id_failure(self):
        with self.assertRaises(self.repo.DoesNotExist):
            self.repo.get_by_id(999)
