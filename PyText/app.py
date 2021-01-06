from twilio.rest import Client

accout_sid = ""
auth_token = ""

client = Client(accout_sid, auth_token)

call = client.messages.create(
    to="",
    from="",
    body="This is our first message"
)
