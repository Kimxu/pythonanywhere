from flask import render_template

from main import main


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@main.app_errorhandler(403)
def page_not_found(error):
    return render_template("403.html"), 403


@main.app_errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
