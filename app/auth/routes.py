from urllib.parse import urlsplit

from flask import redirect, url_for, render_template, request, flash
from flask_login import current_user, login_user, logout_user, login_required

from . import bp
from .forms import LoginForm, RegistrationForm
from .models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)

        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember.data)

        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('core.index')
        return redirect(next_page)

    return render_template('login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create(form.email.data, form.password.data)

        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
