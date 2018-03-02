from flask import Response

from settings import UNIFORM_BASE_URL


def create_uniform_view(app):
    @app.route('/uniform_base_url')
    def uniform():
        response = Response(UNIFORM_BASE_URL, status=200)
        return response
