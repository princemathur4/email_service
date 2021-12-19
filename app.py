import os
from flask import Flask
from modules.exceptions import InvalidInputParameter


LOCAL = "LOCAL"
PROD = "PROD"
ENVIRONMENTS = [LOCAL, PROD]


def load_config(app: Flask, env):
    app.config["ENVIRONMENT"] = env
    global_config_path = os.path.join(app.root_path, "config/default.py")
    app.config.from_pyfile(global_config_path)

    env_config_path = os.path.join(app.root_path, f"config/{env.lower()}.py")
    app.config.from_pyfile(env_config_path)


def create_app(env: str) -> Flask:
    if env not in ENVIRONMENTS:
        raise InvalidInputParameter(f"Invalid value for env={env}")

    app = Flask(__name__)
    load_config(app, env)
    register_blueprints(app)
    os.environ["PROJECT_PATH"] = os.path.dirname(app.instance_path)
    print("#" * 50, f"{' ' * 10} * Environment: {env}", "#" * 50, sep='\n')
    return app


def register_blueprints(app: Flask):
    from modules.interface.views import interface_bp
    app.register_blueprint(interface_bp)
    from modules.common.blueprints.base import base_bp
    app.register_blueprint(base_bp)


if __name__ == "__main__":
    app = create_app(LOCAL)
    app.run(host="127.0.0.1", port=5000)
