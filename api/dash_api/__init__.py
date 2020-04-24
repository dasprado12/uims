# Examples of valid version strings
# 'X.Y.Z.devW'
# X: major modifications
# Y: minor modifications
# Z: bug fixes
# W: developmental release (build number)


__version__ = '1.0.3'

from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load
from flask_cors import CORS
from flask import Flask, g
from pathlib import Path
import logging.config
import yaml
import os


def create_app(db_name='dash_api'):
    app = Flask(__name__, instance_relative_config=True)

    path = f'{Path(__file__).parents[1]}/logging.yaml'
    with open(path, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

    CORS(app)

    from .app import api
    app.register_blueprint(api)

    from .mongo import InitializeDb
    @app.before_request
    def connect_db():
        g.db = InitializeDb(db_name)

    from .errors import error_handler
    app.register_blueprint(error_handler)

    return app
