from __future__ import unicode_literals

from flask import Blueprint
from ksl import app

from .controller import ArticlesPage

blueprint = Blueprint('show_articles', __name__, url_prefix='')

app.add_url_rule('/articles', view_func=ArticlesPage.as_view('show_articles'))

