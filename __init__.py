from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
import sys
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    print(sys.executable)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 附加路由和自定义的错误页面 return app
    from post import post as post_blueprint
    app.register_blueprint(post_blueprint, url_prefix='/posts')
    from user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')
    from upload import upload as upload_blueprint
    app.register_blueprint(upload_blueprint, url_prefix='/uploads')
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
