# -*- coding:utf-8 -*-
from flask import render_template
from flask import request, jsonify
from flask import url_for

from . import main


@main.route('/index/')
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/tags')
def tags():
    return render_template('tags.html')


@main.route('/about/user')
def user():
    return render_template('user.html')



@main.route("/categories/<category>/")
def page_article_by_category(category):
    """页面-指定目录的文章列表
    """
    return render_template("posts/articles_by_category.html", category=category)


@main.route("/tags/<tags>/")
def page_article_by_tags(tags):
    """页面-指定标签的文章列表
    """
    return render_template("posts/articles_by_tags.html", tags=tags)
