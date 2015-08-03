from app import app
from flask import render_template, url_for

# interests = {'code': 'This is the code page', 
# 			 'text':'This is the text page',
# 			 'music': 'This is the music page'}

interests = {'code': {'about': 'This is the code page', 'image':'/static/code.png', 'color': 'red'}, 
			 'text': {'about': 'This is the text page', 'image':'/static/text.png', 'color': 'blue'},
			 'music':{'about': 'This is the music page', 'image':'/static/music.png', 'color': 'green'}
		}


@app.route('/')
def index():
	return render_template('index.html', interests=interests)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', interests=interests)