import os

from flask import Flask
from . import db
from . import auth
from . import blog
from . import resume

import logging


def create_app(test_config=None):
    """Application factory function."""
    # Create application (instance of the Flask class).
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'portfolio.sqlite'),
        UA_ID = 'UA-119542722-2',
    )

    if test_config is None:
        # Load the instance config when not testing.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in.
        app.config.from_mapping(test_config)

    # Ensure that the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # Authentication blueprint registration.
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(resume.bp)
    app.add_url_rule('/', endpoint='index')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
