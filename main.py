from twilio.rest import Client
from os import getlogin


account_sid = 'AC9b73a2d76141d0d5c162b35d5c3c1b74'
auth_token = 'ca39cf9641b9f5d75795183d91cdcc41'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f""" "{getlogin()}" Logged In into your Linux""",
    to='whatsapp:+918446998284'
)
