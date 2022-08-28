import os
from twilio.rest import Client



account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='whatsapp:+15005550006',
         body='Hi, Joe! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234',
         to='whatsapp:+14155238886'
     )

print(message.sid)
