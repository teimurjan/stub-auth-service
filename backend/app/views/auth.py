from flask import request

from app.common.views import ApiView


class LoginView(ApiView):

    def post(self, service):
        return service.log_in(
            request.json.get('email'),
            request.json.get('password')
        )


class VerifyTokenView(ApiView):

    def post(self, service):
        authorization = request.headers.get('Authorization')
        if authorization is None:
            return {}, 401
        return service.verify(
            authorization.replace('JWT ', '')
        )


class CheckTokenView(ApiView):

    def post(self, service):
        authorization = request.headers.get('Authorization')
        if authorization is None:
            return {}, 401
        return service.check(
            authorization.replace('JWT ', '')
        )


class RefreshTokenView(ApiView):

    def post(self, service):
        token = request.json.get('refresh_token')
        return service.refresh(token)
