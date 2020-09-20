from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from ..models import User
from .forms import LoginForm, RegistrationForm
from . import auth
from flask_login import login_user, logout_user, login_required
from .. import db

@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
