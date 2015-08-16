from app import app
from flask import render_template, url_for

interests = {1 : {'area':'Venice', 'about': 'My original home', 'color': '#936FB2', 'FKUserId': 1}, 
			 2 : {'area':'Constantinople', 'about': 'A peace time cultural ambassador', 'color': '#AF4415', 'FKUserId': 1},
			 3 : {'area':'Greece', 'about': 'Time in Greece', 'color': '#5487B2', 'FKUserId': 1}
		}

user = {1: {'name': 'Moon Flask','password': 'default', 'color': '#111111'}}

posts = {1: {'title': 'Python', 'text': 'I like Python', 'FK_IntrestId': 1},
		 2: {'title': 'Flask', 'text': 'This is built on Flask', 'FK_IntrestId': 1},
		 3: {'title': 'Blogging', 'text': 'I write blogposts', 'FK_IntrestId': 2},
		 1: {'title': 'Cello', 'text': 'I play the Cello', 'FK_IntrestId': 3},
		 1: {'title': 'Audio Production', 'text': 'I produce my own music', 'FK_IntrestId': 3}
	}

@app.route('/')
def index():
	return render_template('index.html', user=user, interests=interests)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', user=user, interests=interests, area=area)