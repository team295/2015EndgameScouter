from endgame import app
from flask import render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from endgame.dbmodel import *
from sqlalchemy import exc

@app.route('/')
def _home():
	return render_template('home.html')

@app.route('/login')
def _login():
	return render_template('login.html')

@app.route('/admin')
def _admin():
	users = [] 
	message = None
	try:
		users = list(User.query.all())
	except exc.SQLAlchemyError:
		message = 'There was a problem reading the users from the database.'
	return render_template('admin.html', users=users, message=message)

@app.route('/register', methods=['GET', 'POST'])
def _register():
	message = None
	if request.method == 'POST':
		try:
			n = request.form['name']
			u = request.form['username']
			p = request.form['password']
			db.session.add(User(n, u, p))
			db.session.commit()
			return redirect(url_for('_home'))
		except exc.SQLAlchemyError:
			message = 'There was a problem adding a user to the database.'
	return render_template('register.html', message=message)

