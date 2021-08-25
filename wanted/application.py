from flask import Flask
from models.company_model import db
from settings import LocalConfig


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    from blue_prints.company_view import api

    app.register_blueprint(api)
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app(config=LocalConfig)
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
