from twilio.rest import Client
import datetime
import random

account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

d = datetime.datetime.now()

text = ['Hey Bella, it\'s time to drink some water now', 'test']

if d.isoweekday() in range(1, 6):
    if d.hour in range(10, 18):
        message = client.messages.create(
            body=random.choice(text),
            to="your_phone_number",
            from_="your_twilio_number"
        )
        print (message.account_sid)
    else:
        print('Not in time range')
else:
    print ('Not a weekday')