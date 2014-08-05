from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.socketio import SocketIO

app = Flask(__name__)
app.config.from_object('endgame.config')
socketio = SocketIO(app)

db = SQLAlchemy(app)

import endgame.views
from endgame.dbmodel import *

