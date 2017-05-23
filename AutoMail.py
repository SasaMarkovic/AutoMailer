import win32com.client
from win32com.client import Dispatch
import smtplib
import schedule
import time

def sendMail(body):
    file = open(".\password", 'r')
    username = file.readline()
    pw = file.readline()

    # Create a text/plain message
    msg = "Sorry but the User 'Florian Becher' is not available" + body

    me = 'FastResponde@me.com'
    you = 'becher.florian@outlook.com'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, pw)
    server.sendmail(me, you, msg)
    server.quit()


def checkMail():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                        # the inbox. You can change that number to reference
                                        # any other folder
    messages = inbox.Items
    message = messages.GetLast()
    sender = message.SenderEmailAddress
    body_content = message.body # BODY INHALT USW.

    print(sender)

    if sender == "becher.florian97@gmail.com":
        print("It's from me!")
        sendMail(body_content)
    else:
        print("Its all okay!")


def test():
    print("HI")




#MAINNNNNNNNNNNNN
while True:
    checkMail()
    test()
    time.sleep(300)
