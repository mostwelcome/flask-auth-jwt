from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# to generate public id
import uuid
from database.db import db


app = Flask(__name__)

app.config.from_pyfile('config/settings.staging.cfg')
db.init_app(app)


@app.route('/')
def home():
    return 'Its working'


if __name__ == '__main__':
    app.run()
