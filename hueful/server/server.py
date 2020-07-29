from flask import Flask
from flask_cors import CORS

from hueful.server.apis import make_rest_api_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)
    api_bp = make_rest_api_blueprint()
    app.register_blueprint(api_bp)

    return app


def main():
    app = create_app()

    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
