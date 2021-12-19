import os
from flask import Flask
from config import ENVIRONMENTS, Config, LOCAL, PROD
from modules.exceptions import InvalidInputParameter


def load_config(app: Flask, env):
    app.config["ENVIRONMENT"] = env
    config_classes = Config.__subclasses__()
    for config_cls in config_classes:
        if config_cls.__env_name__ == env:
            app.config.from_object(config_cls)
            return
    raise InvalidInputParameter(f"Invalid value for env={env}")


def create_app(env: str) -> Flask:
    if env not in ENVIRONMENTS:
        raise InvalidInputParameter(f"Invalid value for env={env}")

    app = Flask(__name__)
    load_config(app, env)
    from modules.mail_service.providers.flask_mail import mail
    mail.init_app(app)
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
