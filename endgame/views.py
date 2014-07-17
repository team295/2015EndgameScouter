from endgame import app
from flask import render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from endgame.dbmodel import  User,db
from sqlalchemy import exc
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def _login():
	return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def _register():
	message = None
	if request.method == 'POST':
           try:
                u = request.form['username']
                p = request.form['password']
                n = request.form['name']
                newUser = User(n,u,p)
                db.session.add(newUser)
                db.session.commit()
                return redirect(url_for('/'))
           except exc.SQLAlchemyError:
                message = 'Something went wrong'
	return render_template('register.html', message=message)

