from endgame import app
from flask import render_template, request

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
		u = request.form['username']
		p = request.form['password']
		return redirect(url_for('_login'))
	else:
		message = 'dickbutt error'
	return render_template('register.html', message=message)

