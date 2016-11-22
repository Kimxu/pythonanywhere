# -*- coding:utf-8 -*-
from flask import flash
from flask import redirect
from flask import render_template
from flask import request, jsonify
from flask import url_for
from flask.ext.login import login_user

from models import User
from user.forms import LoginForm
from . import user


@user.route('/login', methods=['GET', 'POST'])
def get_posts():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('请输入正确的账号和密码')
    return render_template('users/login.html', form=form)


@user.route('/author')
def author():
    m_author = request.args['author']
    return m_author
