from app import app, db
from flask import render_template, url_for, session, redirect

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
	return render_template('page.html', 
							name=name, 
							pages=pages, 
							posts=posts, 
							social_icons=social_icons)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	name = None
	pages = Page.query.all()
	social_icons = SocialIcon.query.all()
	form = ContactForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		session['email'] = form.email.data
		session['message'] = form.message.data
		return redirect(url_for('contact'))
	return render_template('contact.html', 
							form=form, 
							name=session.get('name'),
							email=session.get('email'), 
							message=session.get('message'), 
							pages=pages, 
							social_icons=social_icons)