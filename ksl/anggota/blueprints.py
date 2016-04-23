from __future__ import unicode_literals

from flask import Blueprint
from ksl import app

from .controller import UsersPage, UsersLogin



blueprint = Blueprint('show_users', __name__, url_prefix='')

app.add_url_rule('/users', view_func=UsersPage.as_view('show_users'))
app.add_url_rule('/login', view_func=UsersLogin.as_view('login_users'))
