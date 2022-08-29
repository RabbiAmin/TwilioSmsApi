from http import client
from twilio.rest import Client

client = Client(
    "ACe8b86e623f4ba50e61c777b753fef010",
    "00c35652ccd342bd53c417fe6f4709be"
)

# for msg in client.messages.list():
#     print(msg.body)

msg = client.messages.create(
    to = "+8801813124824",
    from_ = "+18623198103",
    body = "R koto game khelbi vudai",
)

print(f"Created a new sms from vs code:{msg.sid}")