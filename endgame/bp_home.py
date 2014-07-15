from flask import Blueprint, render_template, abort, url_for, request, redirect
from jinja2 import TemplateNotFound

bp_home = Blueprint('bp_home', __name__, template_folder='templates')

@bp_home.route('/login')
def _login():
	return render_template('login.html')

@bp_home.route('/register', methods=['GET', 'POST'])
def _register():
	message = None
	if request.method == 'POST':
		u = request.form['username']
		p = request.form['password']
		return redirect(url_for('_login'))
	else:
		message = 'dickbutt error'
	return render_template('register.html', message=message)

