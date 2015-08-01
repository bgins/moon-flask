from app import app
from flask import render_template, url_for

interests = {'code':'This is the code page', 
			 'writing':'A page on writing',
			 'music':'A page on music'}


@app.route('/')
def index():
	return render_template('index.html', interests=interests)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', interests=interests)