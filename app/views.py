from app import app
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

@app.route('/')
def index():
	return render_template('index.html', user=user, interests=interests)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', user=user, interests=interests, area=area, posts=posts)