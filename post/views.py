# -*- coding:utf-8 -*-
from flask import render_template
from flask import request, jsonify

from generate import generate
from utils.helper import IndexData
from . import post
# 把项目放到heroku之后，总会一段之后 out文件夹就不见了,暂不知道为什么，
# 这里的做法就是捕获异常，如果不见了，就重新生成一遍

@post.route('/')
def page_articles():
    return render_template('posts/articles.html')


@post.route("/json/")
def get_all_article_index():
    """获取所有文章索引信息
    """
    try:
        return jsonify(IndexData.get_index_data().get("article_index"))
    except Exception as error:
        print("出错了，重新加载..." + str(error))
        generate()
        return jsonify(IndexData.get_index_data().get("article_index"))


@post.route("/inv_tag/")
def get_tag_index():
    """获取标签的倒排索引
    """
    return jsonify(IndexData.get_index_data().get("tag_inverted_index"))


@post.route("/tag/<tag>/")
def get_article_by_tag(tag):
    """获取指定标签的索引信息
    """
    try:
        pager = int(request.args['pager'])
    except:
        pager = 0
    try:
        aids = IndexData.get_index_data().get("tag_inverted_index").get(tag)
    except Exception as error:
        print("出错了，重新加载..." + str(error))
        generate()
        aids = IndexData.get_index_data().get("tag_inverted_index").get(tag)
    # 这里是预防传入的pager大于存在的篇幅数
    if aids is None:
        return jsonify(noDatas=True)
    if pager * 10 >= len(aids):
        articles = {i: IndexData.get_index_data().get("article_index")[i] for i in aids}
        return jsonify(nextPagerDatas=True)
    if len(aids) > (pager + 1) * 10:
        aids = aids[pager * 10:(pager + 1) * 10]
        has_pager = True
    else:
        aids = aids[pager * 10:len(aids)]
        has_pager = False
    articles = {i: IndexData.get_index_data().get("article_index")[i] for i in aids}

    return jsonify(articles=articles, hasPager=has_pager, nextPagerDatas=False)


@post.route("/categories/<category>/")
def get_article_by_category(category):
    """获取指定目录的索引信息
    """
    try:
        pager = int(request.args['pager'])
    except:
        pager = 0
    try:
        aids = IndexData.get_index_data().get("category_index").get(category)
    except Exception as error:
        print("出错了，重新加载..."+str(error))
        generate()
        aids = IndexData.get_index_data().get("category_index").get(category)
    # 这里是预防传入的pager大于存在的篇幅数
    if aids is None:
        return jsonify(noDatas=True)
    if pager * 10 >= len(aids):
        articles = {i: IndexData.get_index_data().get("article_index")[i] for i in aids}
        return jsonify(nextPagerDatas=True)
    if len(aids) > (pager + 1) * 10:
        aids = aids[pager * 10:(pager + 1) * 10]
        has_pager = True
    else:
        aids = aids[pager * 10:len(aids)]
        has_pager = False
    articles = {i: IndexData.get_index_data().get("article_index")[i] for i in aids}

    return jsonify(articles=articles, hasPager=has_pager, nextPagerDatas=False)


@post.route("/<aid>/")
def page_article(aid):
    from manage import app
    """页面-获取指定id的文章
    """
    return app.send_static_file("out/{}.html".format(aid))
