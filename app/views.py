from app import app, db
from flask import render_template, url_for

interests = {1 : {'area': 'Dragons', 'about': 'St. George in his famed battle \
				  against the Dragon.', 'image': True, 'FKUserId': 1}, 
			 2 : {'area': 'Hermits', 'about': 'Early Renaissance monastic life.',
			  	  'image': True, 'FKUserId': 1},
			 3 : {'area': 'Polyhedra', 'about': 'My stellated dodecahedron and more.',
			 	  'image': True, 'FKUserId': 1}
		}

user = {1: {'name': 'Moon Flask', 'password': 'default', 'about': 'Moon Flask is \
			a simple content management system built on Flask. You can use it to \
			build a portfolio or personal website. Paolo Uccello serves as the \
			user for the sample app. Take a look at his interests below.'}}

# The FK_InterestIds should be changed to numbers, they match areas for now
posts = {1: {'title': 'Dragons in our Times.', 'text': 'Aliquam ac mauris ante. Suspendisse \
			non tempor lectus, a dignissim felis. Nunc posuere, purus et \
			feugiat accumsan, lorem leo auctor turpis, quis vestibulum metus \
			magna id neque. Ut ac blandit odio. Praesent at elit vestibulum, \
			cursus erat luctus, aliquam eros. Mauris maximus dolor sed lorem \
			rhoncus, vel fringilla mi sagittis. Suspendisse faucibus nunc eu \
			enim pharetra, id lacinia elit venenatis. Integer interdum tellus \
			aliquam ipsum semper consequat. ', 'image': False, 'FK_InterestId': 'Dragons'},
		 2: {'title': 'St. George and the Dragon', 'text': 'Brave St.George.', 'image': True, 'FK_InterestId': 'Dragons'},
		 3: {'title': 'Episodes of the Hermit Life', 'text': 'Hermits and their role in monsatic life.', 'image': True, 'FK_InterestId': 'Hermits'},
		 4: {'title': 'Perspective Study of Mazzocchio', 'text': 'My famous sketch.', 'image': True, 'FK_InterestId': 'Polyhedra'},
		 5: {'title': 'More Shapes', 'text': 'Undiscovered polyhedra.', 'image': False, 'FK_InterestId': 'Polyhedra'}
	}


# Models
# Model names vary from list above. Need to translate to templates.
# todo: create FK reference between user and post
class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	# password
	about = db.Column(db.Text)
	pages = db.relationship('Page', backref='author')
	posts = db.relationship('Post', backref='author')

	def __repr__(self):
		return '<User %r>' % self.username

class Page(db.Model):
	__tablename__ = "pages"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, index=True)
	description = db.Column(db.Text)
	image = db.Column(db.Boolean, default=False)
	posts = db.relationship('Post', backref='page')
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return '<Page %r>' % self.name

class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True)
	body = db.Column(db.Text)	# Long enough? Use db.Text?
	image = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
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