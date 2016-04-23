from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView

from ksl import app, db
from ksl.database import db_session

from .model import Users


class UsersPage(MethodView):

    def get(self):
        session = db.session()
        users = session.query(Users).all()

        return render_template('user/users.html', users=users, nama=users)


    def post(self):
        session = db.session()
        i_nama = request.form['name']
        i_email = request.form['email']


        data = Users(name=i_nama,email=i_email)

        try:
            session.add(data)
            session.commit()
            flash('save succes')
        except:
            session.rollback()
            flash('user name sudah dignakan')

        return redirect(url_for('show_users'))
        #session = db.session()
        #users = session.query(Users).all()
        #flask('')
        #return render_template('user/users.html', users=users)


class UsersLogin(MethodView):

    def get(self):

        return render_template('user/login.html')


    def post(self):
        session = db.session()
        users_name = session.query(Users.name).all()
        users_email = session.query(Users.email).all()
        nama = users_name[0]
        email = users_email[0]
        i_nama = request.form['name']
        i_email = request.form['email']


        if i_nama == 'firman' and i_email ==  'firmanwibowo77@gmail.com':
            session = db.session()
            users = session.query(Users).all()

            return render_template('articles/dashboard.html', users=users)
        else:
            return "LOGIN VAILED CAN YOU TRY AGAIN"


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
