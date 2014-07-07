import os
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def showHome():
    return render_template('home.html')
