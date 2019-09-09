from twilio.rest import Client
import datetime
import random

account_sid = "AC9cfa721d5f001a66ee604825d6150775"
auth_token = "6c16a26b9957ad54d4d6b0da0f422728"
client = Client(account_sid, auth_token)

d = datetime.datetime.now()

text = ['Hey Bella, it\'s time to drink some water now', 'test']

if d.isoweekday() in range(1, 6):
    if d.hour in range(10, 18):
        message = client.messages.create(
            body=random.choice(text),
            to="+447393216558",
            from_="+441613751662"
        )
        print (message.account_sid)
    else:
        print('Not in time range')
else:
    print ('Not a weekday')