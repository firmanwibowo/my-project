from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from ksl import app, db
from ksl.database import db_session

from .model import Articles


class ArticlesPage(MethodView):

    def get(self):
        session = db.session()
        articles = session.query(Articles).all()

        return render_template('articles/articles.html', articles=articles)

    def post(self):
        session = db.session()
        i_title = request.form['title']
        i_article = request.form['article']
        i_date = request.form['tanggal']
        i_authorid = request.form['id']

        data = Articles(title=i_title, article=i_article, datepost=i_date, author_id=i_authorid)

        try:
            session.add(data)
            session.commit()
            flash('save succes')
        except:
            session.rollback()
            flash('save vailed')
        #return redirect(url_for('show_users'))




@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
