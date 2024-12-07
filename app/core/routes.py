from flask import render_template
from flask_login import login_required

from . import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('base.html')


@bp.route('/faq')
def faq():
    return 'faq'


@bp.route('/files', methods=['GET', 'POST'])
@login_required
def files():
    return 'some_files'
