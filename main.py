from twilio.rest import Client
from os import system
from time import strftime, localtime

account_sid = 'AC9b73a2d76141d0d5c162b35d5c3c1b74'
auth_token = 'ca39cf9641b9f5d75795183d91cdcc41'
client = Client(account_sid, auth_token)
curr_time = strftime("%H:%M:%S", localtime())
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"{system('whoami')} Logged In at {curr_time}",
    to='whatsapp:+918446998284'
)
