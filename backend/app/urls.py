from app.factories.services import AuthServiceFactory
from app.views.auth import LoginView, VerifyTokenView, CheckTokenView, RefreshTokenView
from app.views.uniform import create_uniform_view
from app.views.unknown import create_unknown_view


def init_urls(app):
    app.add_url_rule(
        '/api/login', view_func=LoginView.as_view('api_login', service_factory=AuthServiceFactory)
    )
    app.add_url_rule(
        '/api/verify', view_func=VerifyTokenView.as_view('api_verify', service_factory=AuthServiceFactory)
    )
    app.add_url_rule(
        '/api/check', view_func=CheckTokenView.as_view('api_check', service_factory=AuthServiceFactory)
    )
    app.add_url_rule(
        '/api/refresh', view_func=RefreshTokenView.as_view('api_refresh', service_factory=AuthServiceFactory)
    )
    create_uniform_view(app)
    create_unknown_view(app)
