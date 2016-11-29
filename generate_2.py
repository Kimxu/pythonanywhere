#!/usr/bin/python
# -*- coding:utf-8 -*-


import os


class Generate_2():
    # 静态文件路径，默认为`/static/`
    # 表示使用flask发布网站时的`http://ip:port/static/`目录
    STATIC_ROOT = "/static/"
    # Markdown文件读取目录
    INPUT_CONTENT = os.path.abspath('.') + "/in/"
    # 索引文件
    INDEX_DAT = os.path.abspath('.') + "/static/out/index.dat"
    # html生成输出目录
    OUTPUT_CONTENT = os.path.abspath('.') + "/static/out/"

    _current_file_index = None
    _pinyin_names = set()

    TAG_HTML_TEMPLATE = u" <a href='/tags/{tag}/' class='tag-index'>{tag}&nbsp</a> "
    AUTHOR_HTML_TEMPLATE = u"<a href='/about/' class='tag-index'> {author} </a>"
    TITLE_HTML_TEMPLATE = u"<div class='sidebar-module-inset'><h3 class='sidebar-title fa fa-angle-down' style='color:#dddddd;font-size: 16px'>    标题</h3><p>{title_str}</p></div>"

