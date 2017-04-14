from flask import Blueprint, jsonify, redirect, url_for, request
from flask_login import current_user

from utils.views import json_abort

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    if current_user.is_authenticated():
        return jsonify(current_user)
    else:
        return redirect(url_for('.login'))


@bp.route('/login')
def login():
    if request.method == 'POST':
        params = request.get_json()
        try:
            username = params['username']
            password = params['password']
        except KeyError as e:
            error = '缺少%s参数' % e
            json_abort(401, error)
