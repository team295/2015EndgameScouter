from endgame import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		u = request.form['username']
		p = request.form['password']
	else:
		message = 'Something happened.'
	return render_template('register.html', message=message)

