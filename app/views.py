from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm 

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID = "%s", remember_me = %s' % (form.openid.data, str(form.remember_me.data)))
		#flush function shows data on the next page. Good for debugging
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form = form)


@app.route('/Sam')
def Sam():
	return "Hello Sam!"