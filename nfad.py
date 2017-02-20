import requests

class Email(object):

    sender_email = None
    sender_name = None
    recipient_email = None
    recipient_name = None
    message = None




    def __init__(self, color, taste):
        self.color = color
        self.taste = taste


def send_simple_message():
    return requests.post(
    "https://api.mailgun.net/v3/sandbox60e49936b0774a678eb3e70fc7a43dca.mailgun.org/messages",
    auth=("api", "key-0479604fc81406050eafa1f16dc1e738"),
    data={"from": "Mailgun Sandbox <postmaster@sandbox60e49936b0774a678eb3e70fc7a43dca.mailgun.org>",
    "to": "Gabriela <gabriela.l.bazan@gmail.com>",
    "subject": "Hello Gabriela",
    "text": "Congratulations Gabriela, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})


print send_simple_message()

























