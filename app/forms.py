from flask.ext.wtf import Form
# Is HiddenField needed for CSRF hidden tag?
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Email

# from app.models import

class ContactForm(Form):
	name = StringField('Name', validators=[Required()])
	# Make sure both validators work for email
	email = StringField('Email', validators=[Required(),Email()])
	message = TextAreaField('Leave your message here:')
	submit = SubmitField('Submit')

