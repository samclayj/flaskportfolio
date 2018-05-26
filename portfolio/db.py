import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    """Register the close_db and init_db functions with the Flask application context."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    """Initialize the database."""
    db = get_db()
    with current_app.open_resource('schema.sql') as db_file:
        db.executescript(db_file.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables.

    @click.command() defines a command line command called init-db.
    """
    init_db()
    click.echo('Initialized the database.')


def get_db():
    """Return the database.

    Variables:
    g -- a special object unique for each request. Used to store data that
      might be accessed by multiple functions during the request.
    current_app -- another special object that points to the Flask app
      handling the request.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES,
        )

        # Tells the connection to return ros that behave like dicts (access
        # columns by name).
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Close the DB connection if it was set."""
    db = g.pop('db', None)
    # TODO(sjentsch): remove this if statement.
    if db:
        db.close()
