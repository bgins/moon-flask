from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(Form):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    message = TextAreaField('Message')
    submit = SubmitField('Submit')
