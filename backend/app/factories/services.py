import os

from app.repos.user import UserRepo
from app.services.auth import AuthService
from settings import BASE_DIR


class AuthServiceFactory:
    @staticmethod
    def create():
        with open(os.path.join(BASE_DIR, 'storage/users.json'), 'r') as f:
            repo = UserRepo(f.read())
            return AuthService(repo)
