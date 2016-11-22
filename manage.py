#!/usr/bin/env python
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.script import Server
from flask.ext.script import Shell

from __init__ import create_app, db
import os

from models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))


@manager.command
def new_user():
    u = User(email='xxx', username='kimxu',
             password='xxx', confirmed=True)
    db.session.add(u)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
