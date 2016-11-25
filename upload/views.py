# -*- coding:utf-8 -*-

import os

from flask import render_template, jsonify
from flask import request, redirect
from flask import url_for
from flask.ext.login import login_required
from werkzeug.utils import secure_filename

from utils.helper import IndexData
from . import upload


@upload.route('/')
@login_required
def upload_article():
    return render_template('upload/upload.html')


@upload.route('/file', methods=["POST"])
@login_required
def upload():
    from generate import INPUT_CONTENT, generate
    """上传文件
      1. 保存至本地
      2. md转换为html
      3. 重新加载索引信息
      """
    try:
        f = request.files["file_data"]
        f_name = secure_filename(f.filename)
        print('1'+os.path.abspath('.'))
        print('2'+INPUT_CONTENT+f_name)
        print('3'+os.path.abspath(__file__))
        f.save(INPUT_CONTENT+f_name)
        generate()
        IndexData.reload_index_data()
    except Exception as error:
        print(error)
        return jsonify({'status': '上传失败'})

    return jsonify({'status': '上传成功'})
