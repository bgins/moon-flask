from flask import render_template
from flask.ext.mail import Message

from app import mail
from config import MAIL_USERNAME, MOON_MAIL_SUBJECT_PREFIX

def send_email(to, subject, template, **kwargs):
	msg = Message(MOON_MAIL_SUBJECT_PREFIX + subject,
				  sender=MAIL_USERNAME, recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)