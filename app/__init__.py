"""App initialization."""
from flask import Flask
from instance.config import CONFIG

def create_app(configuration):
    """
    Initialize api
    args:
        configuration(str): instance specific configuration
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(CONFIG[configuration])
    return app