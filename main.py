from twilio.rest import Client
from os import getlogin


account_sid = 'MY_AUTH'
auth_token = 'MY_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f""" "{getlogin()}" Logged In into your Linux""",
    to='whatsapp:+918446998284'
)
