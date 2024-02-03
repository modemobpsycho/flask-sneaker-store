from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mrobs59fghdfg"

    return app
