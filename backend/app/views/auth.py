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
        return service.verify(
            request.json.get('token')
        )


class CheckTokenView(ApiView):

    def post(self, service):
        return service.check(
            request.json.get('token')
        )


class RefreshTokenView(ApiView):

    def post(self, service):
        return service.refresh(
            request.json.get('token')
        )
