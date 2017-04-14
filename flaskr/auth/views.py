# coding=utf-8
from flask import Blueprint, redirect, url_for, request, render_template
from flask_login import login_user, logout_user

from flaskr.auth.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            user = form.get_user()
            login_user(user)
    elif request.method == 'GET':
        return render_template("auth/login.html", form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('main.index'))
    return render_template('auth/register.html')
