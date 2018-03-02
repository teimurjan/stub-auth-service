import unittest

import os

from app import create_app
from app.messages import LOGIN_ERROR, INVALID_TOKEN_ERROR
from app.repos.user import UserRepo
from app.services.auth import AuthService
from settings import BASE_DIR


class AuthServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        with open(os.path.join(BASE_DIR, 'tests/users.json'), 'r') as f:
            self.repo = UserRepo(f.read())

    def test_log_in_success(self):
        service = AuthService(self.repo)
        email = 'test_user@t.ta'
        expected = (self.repo.get_by_email(email), 200)
        actual = service.log_in(email, 'passw0rd')
        self.assertEqual(actual, expected)

    def test_log_in_invalid_email(self):
        service = AuthService(self.repo)
        email = 'invalid'
        expected = ({'message': LOGIN_ERROR}, 400)
        actual = service.log_in(email, 'passw0rd')
        self.assertEqual(actual, expected)

    def test_log_in_invalid_password(self):
        service = AuthService(self.repo)
        email = 'test_user@t.ta'
        expected = ({'message': LOGIN_ERROR}, 400)
        actual = service.log_in(email, 'invalid')
        self.assertEqual(actual, expected)

    def test_verify_success(self):
        service = AuthService(self.repo)
        token = 'access token 1'
        expected = (self.repo.get_by_access_token(token), 200)
        actual = service.verify(token)
        self.assertEqual(actual, expected)

    def test_verify_failure(self):
        service = AuthService(self.repo)
        token = 'access token invalid'
        expected = ({'message': INVALID_TOKEN_ERROR}, 401)
        actual = service.verify(token)
        self.assertEqual(actual, expected)

    def test_check_success(self):
        service = AuthService(self.repo)
        token = 'access token 1'
        user = self.repo.get_by_access_token(token)
        expected = ({'user_id': user.get('id')}, 200)
        actual = service.check(token)
        self.assertEqual(actual, expected)

    def test_check_failure(self):
        service = AuthService(self.repo)
        token = 'access token invalid'
        expected = ({'message': INVALID_TOKEN_ERROR}, 401)
        actual = service.check(token)
        self.assertEqual(actual, expected)

    def test_refresh_success(self):
        service = AuthService(self.repo)
        token = 'refresh token 1'
        expected = (self.repo.get_by_refresh_token(token), 200)
        actual = service.refresh(token)
        self.assertEqual(actual, expected)

    def test_refresh_failure(self):
        service = AuthService(self.repo)
        token = 'refresh token invalid'
        expected = ({'message': INVALID_TOKEN_ERROR}, 401)
        actual = service.refresh(token)
        self.assertEqual(actual, expected)
