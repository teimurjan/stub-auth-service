import json


class UserRepo:
    def __init__(self, users_json):
        self._users = json.loads(users_json)

    def _get_by(self, attr, value):
        users = [user for user in self._users if user.get(attr) == value]
        if len(users) == 0:
            raise self.DoesNotExist
        else:
            return users[0]

    def get_by_id(self, id_):
        return self._get_by('id', id_)

    def get_by_email(self, email):
        return self._get_by('email', email)

    def get_by_access_token(self, token):
        return self._get_by('access_token', token)

    def get_by_refresh_token(self, token):
        return self._get_by('refresh_token', token)

    class DoesNotExist(Exception):
        pass
