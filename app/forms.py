from flask.ext.wtf import Form
# Is HiddenField needed for CSRF hidden tag?
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# from app.models import

class ContactForm(Form):
	name = StringField('Name',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(), Email()])
	message = TextAreaField('Leave your message here:')
	submit = SubmitField('Submit')