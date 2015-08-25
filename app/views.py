from app import app, db
from flask import render_template, url_for

interests = {1 : {'area': 'Venice', 'about': 'My original home', 'image': True, 'FKUserId': 1}, 
			 2 : {'area': 'Constantinople', 'about': 'A peace time cultural ambassador', 'image': True, 'FKUserId': 1},
			 3 : {'area': 'Greece', 'about': 'Time in Greece', 'image': True, 'FKUserId': 1}
		}

user = {1: {'name': 'Moon Flask', 'password': 'default'}}

# The FK_InterestIds should be changed to numbers, they match areas for now
posts = {1: {'title': 'The Doge', 'text': 'Aliquam ac mauris ante. Suspendisse \
			non tempor lectus, a dignissim felis. Nunc posuere, purus et \
			feugiat accumsan, lorem leo auctor turpis, quis vestibulum metus \
			magna id neque. Ut ac blandit odio. Praesent at elit vestibulum, \
			cursus erat luctus, aliquam eros. Mauris maximus dolor sed lorem \
			rhoncus, vel fringilla mi sagittis. Suspendisse faucibus nunc eu \
			enim pharetra, id lacinia elit venenatis. Integer interdum tellus \
			aliquam ipsum semper consequat. ', 'image': False, 'FK_InterestId': 'Venice'},
		 2: {'title': 'Miracle of the Cross', 'text': 'This is built on Flask', 'image': True, 'FK_InterestId': 'Venice'},
		 3: {'title': 'Blogging', 'text': 'I write blogposts', 'image': False, 'FK_InterestId': 'Constantinople'},
		 4: {'title': 'Cello', 'text': 'I play the Cello', 'image': False, 'FK_InterestId': 'Greece'},
		 5: {'title': 'Audio Production', 'text': 'I produce my own music', 'image': False, 'FK_InterestId': 'Greece'}
	}


# Models
# Model names vary from list above. Need to translate to templates.
# todo: create FK reference between user and post
#		fix image so it actually deafults to False
class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	# password
	pages = db.relationship('Page', backref='user')

	def __repr__(self):
		return '<User %r>' % self.username

class Page(db.Model):
	__tablename__ = "pages"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, index=True)
	description = db.Column(db.String(140))
	image = db.Column(db.Boolean, default=False)
	posts = db.relationship('Post', backref='page')
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return '<Page %r>' % self.name

class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True)
	body = db.Column(db.String(500))	# Long enough? Use db.Text?
	image = db.Column(db.Boolean, default=False)
	page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))

	def __repr__(self):
		return '<Post %r>' % self.title


@app.route('/')
def index():
	return render_template('index.html', user=user, interests=interests)

# Change interest to page for this route
@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', user=user, interests=interests, area=area, posts=posts)