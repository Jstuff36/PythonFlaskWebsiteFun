from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Kreterade'}
	posts = [
		{
			'author': {'nickname': 'Sammykins'},
			'body': 'Beautiful day in Paradise!'
		},
		{
			'author': {'nickname': 'Samuél'},
			'body': {'I wanna be like Deadpool!'}
		}
	]
	return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/Sam')
def Sam():
	return "Hello Sam!"