from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

	def __repr__(self): #repr is for debugging. Tells Python how to print object to screen
		return '<User %r>' % (self.nickname)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
	#ForeignKey tells Flask-SQLAlchemy that field will link to a user

	def __repr__(self):
		return '<User %r>' % (self.body)