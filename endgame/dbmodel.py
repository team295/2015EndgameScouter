from endgame import db
from flask.ext.sqlalchemy import SQLAlchemy

class User(db.Model):
	id       = db.Column(db.Integer,    primary_key=True)
	name     = db.Column(db.String(40), unique=True)
	admin    = db.Column(db.Boolean,    default=False)
	approved = db.Column(db.Boolean,    default=False)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, name, username, password):
		self.username = username
		self.password = password
		self.name = name
	
	def __repr__(self):
		return '<USER {!r}>'.format(self.username)

