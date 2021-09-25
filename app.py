from flask import Flask, redirect, url_for

from blueprints.users import USERS_BLUEPRINT
# to generate public id
from database.db import db

app = Flask(__name__)
app.register_blueprint(USERS_BLUEPRINT, url_prefix='/user')


@app.before_first_request
def create_tables():
    db.create_all()


app.config.from_pyfile('config/settings.staging.cfg')
db.init_app(app)


@app.route('/')
def home():
    return redirect(url_for('user.get_all_user'))


if __name__ == '__main__':
    app.run()
