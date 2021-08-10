from flask import Flask

def create_app(**config_overrides):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)

    from wanted.views import api

    app.register_blueprint(api)

    return app

