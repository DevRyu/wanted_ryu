from settings import DockerConfig
from application import create_app

if __name__ == "__main__":
    app = create_app(config=DockerConfig)
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
