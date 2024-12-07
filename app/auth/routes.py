from . import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'


@bp.route('/logout')
def logout():
    return 'logout'
