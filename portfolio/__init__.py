import os

from flask import Flask
from . import db
from . import auth
from . import blog

def create_app(test_config=None):
    """Application factory function."""
    # Create application (instance of the Flask class).
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'portfolio.sqlite'),
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

    # Routing
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    db.init_app(app)

    # Authentication blueprint registration.
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

