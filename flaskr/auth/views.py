# coding=utf-8
from flask import Blueprint, redirect, url_for, request, render_template
from flask_login import login_user, logout_user

from flaskr.auth.forms import LoginForm, RegisterForm
from flaskr.auth.services import user_service

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            user = form.get_user()
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template("auth/login.html", form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate():
            user = user_service.new_user(form.username.data, form.password.data, form.email.data, form.description.data)
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)
