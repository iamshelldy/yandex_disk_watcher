from . import bp


@bp.route('/')
@bp.route('/index')
def index():
    return 'index'
