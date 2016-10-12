from flask.ext.wtf import Form 
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form): #LoginForm is a subclass of Form. Osea LoginForm inherits from From
	openid = StringField('openid', validators = [DataRequired()]) 
	
	'''The DataRequired import is a validator, a function that can be attached to a field 
	to perform validation on the data submitted by the user. The DataRequired validator 
	simply checks that the field is not submitted empty. There are many more validators 
	included with Flask-WTF, we will use some more in the future.'''
	
	remember_me = BooleanField('remember_me', default = False)
