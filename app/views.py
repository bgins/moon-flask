from app import app, db
from flask import render_template, url_for

from app.models import User, Page, Post, SocialIcon
from app.forms import ContactForm



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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	pages = Page.query.all()
	form = ContactForm()
	return render_template('contact.html', form=form, pages=pages)