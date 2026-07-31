import smtplib


class EmailAlert:

    def send(self, sender, receiver, message):

        print("Email Alert Sent")

        print("From:", sender)

        print("To:", receiver)

        print("Message:", message)
