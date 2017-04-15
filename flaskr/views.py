from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@main.errorhandler(500)
def internal_error(error):
    return render_template('500.html')