'''
[Google Mail Api]
https://cloud.google.com/appengine/docs/python/mail/sendingmail

 - what is different ?
   :To show that you don't need to use google user authentication to send email.
 - Local google app engine browser won't work, however, once you deploy, it will work fine :)
'''

from flask import Flask
from google.appengine.api import mail

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = str(uuid.uuid4())

@app.route('/')
def SendMail():
	message = mail.EmailMessage()
	message.sender = '___@xxx'
	message.to = '___@xxx'
	message.body = 'Hello ! I hope you receive my email :)'
	message.send()
	
	return ''
