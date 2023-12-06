''' Twilio is a Communication Platform as a Service platform that helps software developers 
create seamless customer experiences through Application Programming Interfaces '''

from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC97c94dda76c05a271bba4f94e95b5e4d"
auth_token = "fbf779ba12c6e053d5a5ca9a90489d12"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+91-8310207447",
    from_="+12622383828",
    body="Hello there!")
