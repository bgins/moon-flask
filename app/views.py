from app import app, db
from flask import render_template, url_for

from app.models import User, Page, Post, SocialIcon


@app.route('/')
def index():
	user = User.query.first()
	pages = Page.query.all()
	return render_template('index.html', user=user, pages=pages)


@app.route('/page/<name>')
def page(name):
	pages = Page.query.all()
	posts = Post.query.all()
	social_icons = SocialIcon.query.all()
	return render_template('page.html', name=name, pages=pages, posts=posts, social_icons=social_icons)


@app.route('/contact')
def contact():
	pages = Page.query.all()
	return render_template('contact.html', pages=pages)