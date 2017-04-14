from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    user_info = jsonify(current_user)
    return render_template('index.html', user=user_info)
