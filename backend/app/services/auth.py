from app.messages import LOGIN_ERROR, INVALID_TOKEN_ERROR


class AuthService:
    def __init__(self, user_repo):
        self._user_repo = user_repo

    def log_in(self, email, password):
        try:
            user = self._user_repo.get_by_email(email)
            if user.get('password') == password:
                return user, 200
            else:
                return {'message': LOGIN_ERROR}, 400
        except self._user_repo.DoesNotExist:
            return {'message': LOGIN_ERROR}, 400

    def verify(self, token):
        try:
            user = self._user_repo.get_by_access_token(token)
            return user, 200
        except self._user_repo.DoesNotExist:
            return {'message': INVALID_TOKEN_ERROR}, 401

    def check(self, token):
        try:
            user = self._user_repo.get_by_access_token(token)
            return {'user_id': user.get('id')}, 200
        except self._user_repo.DoesNotExist:
            return {'message': INVALID_TOKEN_ERROR}, 401

    def refresh(self, token):
        try:
            user = self._user_repo.get_by_refresh_token(token)
            return user, 200
        except self._user_repo.DoesNotExist:
            return {'message': INVALID_TOKEN_ERROR}, 401
