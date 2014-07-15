from endgame import app
from flask import render_template, request

from endgame.bp_home import bp_home

app.register_blueprint(bp_home)

@app.route('/')
def home():
    return render_template('home.html')

