import sqlite3
import click
from flask import current_app, g


# function to intiate the database for a request handling.
def get_db():
    """Intiate Database function."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# function to close the database connection
def close_db(e=None):
    """Close database connection."""
    db = g.pop('db', None)

    if db is not None:
        db.close()


# intializing databse
def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode('utf-8'))


# adding it as a command
@click.command('init-db')
def init_db_command():
    """clear the existing data and create new tables."""

    try:
        click.echo("initialializing database...")
        init_db()
        click.echo("database initialized successfully.")
    except Exception as e:
        click.echo("there is an issue with initialization.")
        raise
        




# registering with the app
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)