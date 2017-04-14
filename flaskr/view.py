# coding=utf-8
from flask import Blueprint, jsonify, redirect, url_for, request, render_template
from flask_login import current_user

from flaskr.form import LoginForm
from utils.views import json_abort

auth = Blueprint('blog', __name__)


@auth.route('/')
def index():
    if current_user.is_authenticated():
        return jsonify(current_user)
    else:
        return redirect(url_for('.login'))


@auth.route('/login')
def login():
    if request.method == 'POST':
        params = request.get_json()
        try:
            username = params['username']
            password = params['password']
            
        except KeyError as e:
            error = '缺少%s参数' % e
            json_abort(401, error)
    elif request.method == 'GET':
        form = LoginForm()
        return render_template("login.html", form=form)
