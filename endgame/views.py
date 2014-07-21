from endgame import app
from flask import render_template, request, redirect, url_for, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from endgame.dbmodel import *
from sqlalchemy import exc

@app.route('/')
def _home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def _login():
	if session.get('logged_in'):
		flash('You are already logged in as {}.'.format(session.get('username')))
		return redirect(url_for('_home'))
	if request.method == 'POST':
		try:
			u = request.form['username']
			p = request.form['password']
			if User.query.filter(User.username == u, User.password == p).first() != None:
				session['logged_in'] = True
				session['username'] = u
				flash('Logged in as {}.'.format(u))
				return redirect(url_for('_home'))
			else:
				flash('Incorrect username or password.')
		except exc.SQlAlchemyError:
			flash('There was a problem accessing the database.')
	return render_template('login.html')

@app.route('/logout')
def _logout():
	session.pop('logged_in', None)
	flash('Logged out.')
	return redirect(url_for('_home'))

@app.route('/admin', methods=['GET', 'POST'])
def _admin():
	if (request.method == 'POST'):
		### print request.form
		for t in request.form.items():
			if 'approved' in t[0]:
				id = int(t[0].split('_')[1])
				ac = True if t[1] == 'y' else False
				### print('{}:{}'.format(id, ac))
				User.query.filter(User.id == id).update({'approved':ac})
				db.session.commit()
	users = []
	try:
		users = list(User.query.all())
	except exc.SQLAlchemyError:
		flash('There was a problem reading the users from the database.')
	return render_template('admin.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def _register():
	if request.method == 'POST':
		try:
			n = request.form['name']
			u = request.form['username']
			p = request.form['password']
			db.session.add(User(n, u, p))
			db.session.commit()
			flash('You are now registered as {}.'.format(u))
			return redirect(url_for('_home'))
		except exc.SQLAlchemyError:
			flash('There was a problem adding a user to the database.')
	return render_template('register.html')

