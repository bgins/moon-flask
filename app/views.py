from app import app
from flask import render_template, url_for

interests = {1 : {'area':'code', 'about': 'This is the code page', 'color': '#936FB2', 'FKUserId': 1}, 
			 2 : {'area':'text', 'about': 'This is the text page', 'color': '#AF4415', 'FKUserId': 1},
			 3 : {'area':'music', 'about': 'This is the music page', 'color': '#5487B2', 'FKUserId': 1}
		}

user = {1: {'name': 'Gentile Bellini','password': 'default'}}

posts = {1: {'title': 'Python', 'text': 'I like Python', 'FK_IntrestId': 1},
		 2: {'title': 'Flask', 'text': 'This is built on Flask', 'FK_IntrestId': 1},
		 3: {'title': 'Blogging', 'text': 'I write blogposts', 'FK_IntrestId': 2},
		 1: {'title': 'Cello', 'text': 'I play the Cello', 'FK_IntrestId': 3},
		 1: {'title': 'Audio Production', 'text': 'I produce my own music', 'FK_IntrestId': 3}
	}

@app.route('/')
def index():
	link_width = calculate_width();
	return render_template('index.html', interests=interests, user=user, link_width=link_width)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', interests=interests)

def calculate_width():
	link_width = int(12 / len(interests))
	# Convert number to word for skeleton.css class - five links won't center properly!
	numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
	return numbers[link_width]