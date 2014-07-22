from endgame import app
from flask import render_template, request, redirect, url_for, session, flash, jsonify
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
	if request.method == 'POST':
		approved = [int(i.split('_')[1]) for (i, a) in request.form.items() if 'approved' in i]
		admin = [int(i.split('_')[1]) for (i, a) in request.form.items() if 'admin' in i]
		for u in User.query.all():
			u.approved = u.id in approved
			u.admin = u.id in admin
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

@app.route('/scout/lobby')
def _lobby():
	if not session.get('logged_in'):
		flash('Please log in to access this page.')
		return redirect(url_for('_login'))
	return render_template('lobby.html')

@app.route('/handshake')
def _handshake():
	handshake = request.args.get('handshake', -1, type=int)
	return jsonify(response=handshake + 1)

