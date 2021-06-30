# has functions that relate to sending whatsapp message
# import modules
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# function to send message using Twilio API
def send_message(message, number):
    account_sid = os.environ["ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    number = str(number)
    try:
        message = client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+'+number
        )
    except TwilioRestException as e:
        print(e)
        return False
    else:
        print(message.sid)
        return True
