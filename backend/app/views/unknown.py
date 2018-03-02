from flask import render_template


def create_unknown_view(app):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def unknown(path):
        return render_template("index.html")
