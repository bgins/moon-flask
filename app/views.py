from app import app, db
from flask import render_template, url_for, session, redirect, flash, abort

from app.models import User, Page, Post, SocialIcon
from app.forms import ContactForm
from app.email import send_email
from config import MAIL_USERNAME


@app.route('/')
def index():
    user = User.query.first()
    pages = Page.query.all()
    return render_template('index.html', user=user, pages=pages)


@app.route('/page/<name>')
def page(name):
    if not Page.query.filter_by(name=name).first():
        abort(404)
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
        name = form.name.data
        email = form.email.data
        message = form.message.data
        send_email(MAIL_USERNAME, 'Contact', 'mail/contact',
                   name=name, email=email, message=message)
        flash('Your message has been sent!')
        return redirect(url_for('contact'))
    return render_template('contact.html', 
                            form=form, 
                            pages=pages, 
                            social_icons=social_icons)


@app.errorhandler(404)
def not_found_error(error):
    pages = Page.query.all()
    return render_template('404.html', pages=pages), 404


@app.errorhandler(500)
def internal_error(error):
    app.logger.error(error)
    pages = Page.query.all()
    return render_template('500.html', pages=pages), 500
