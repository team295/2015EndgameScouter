from flask import Flask
from  flask.ext.sqlalchemy import SQLAlchemy
#from dbmodel import User
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.create_all()


