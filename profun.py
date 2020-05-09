import imaplib
import email
from email.parser import Parser
from twilio.rest import Client
import time

def msg(data):
	result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID 
	raw_email = data[0][1]
	headers = Parser().parsestr(raw_email)
	print 'To: %s' % headers['to']
	print 'From: %s' % headers['from']
	print 'Subject: %s' % headers['subject']
	# Your Account Sid and Auth Token from twilio.com/console
	account_sid = 'AC839821af00843ef0386180fcdd51ef84'
	auth_token = '005e30fc72e7f9253db1193741a4a066'
	client = Client(account_sid, auth_token)
	message = client.messages \
	    .create(
	         body='From: %s' % headers['from']+'Subject: %s' % headers['subject'],
	         from_='+13862226833',
	         to='+917997623352'
	     )
	print(message.sid)
	



mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('nuvvularakeshchowdary@gmail.com','rakesh07')
mail.list()
mail.select('inbox')
result, data = mail.search(None,'ALL')
#retrieves the latest (newest) email by sequential ID
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]
msg(data)

while True:
	time.sleep(01)
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('nuvvularakeshchowdary@gmail.com','rakesh07')
	mail.list()
	mail.select('inbox')
	#retrieves the latest (newest) email by sequential ID
	result, data1 = mail.search(None,'ALL')
	ids1 = data1[0]
	id_list = ids1.split()
	latest_email_id = id_list[-1]
	if(ids!=ids1):
		msg(data1)
		ids=ids1
		

