from app import app
from flask import render_template, url_for


interests = {'code': {'about': 'This is the code page', 'image': 'code', 'color': 'red'}, 
			 'text': {'about': 'This is the text page', 'image': 'text', 'color': 'blue'},
			 'music':{'about': 'This is the music page', 'image': 'music', 'color': 'green'}
		}


@app.route('/')
def index():
	return render_template('index.html', interests=interests)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', interests=interests)