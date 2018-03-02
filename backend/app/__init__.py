import os
from flask import Flask

from .settings import APP_DIR
from .urls import init_urls


def create_app():
    app = Flask(__name__, static_folder=os.path.join(APP_DIR, 'static'), static_url_path='/static/')
    app.config.from_pyfile('config.py')

    init_urls(app)
    return app
