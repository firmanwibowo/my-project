from __future__ import unicode_literals

from flask_runner import Manager
from ksl.database import init_db
from ksl import app

app = Manager(app)



@app.command
def create_db():
    init_db('sqlite:///ksl/ksl.db')


if __name__ == '__main__':

    app.run()
