import win32com.client
from win32com.client import Dispatch
import smtplib
import schedule
import time

#sendMail is the function to send a explicite mail
def sendMail(body):
    file = open(".\password", 'r')
    username = file.readline()
    pw = file.readline()

    # Create a text/plain message
    msg = "Sorry but the User 'Florian Becher' is not available\n\n\n" + body

    #Mail from who? -me (Fastresponde@me.com)
    me = 'FastResponde@me.com'
    #Mail to who? -you
    you = 'becher.florian@outlook.com'

    #Open GMAIL server for Mail activities
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, pw)
    server.sendmail(me, you, msg)
    server.quit()

    print("EMAIL SEND!")

#Looks if a mail is in the inbox and checks sender of it
#If is is from YOU it send answer
def checkMail():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                        # the inbox. You can change that number to reference
                                        # any other folder

                                        #3 Deleted
    messages = inbox.Items
    message = messages.GetLast()
    sender = message.SenderEmailAddress
    body_content = message.body # BODY INHALT USW.
    body = "Hello and so on"
    name = sender.rpartition('@')[0]
    firstname = name.split('.')[0]
    secondname = name.rpartition('.')[2]

    print(sender, firstname, secondname)

    if sender == "becher.florian97@gmail.com":
        print("Email sender will be activated!")
        sendMail(body)
    else:
        print("Not the Email to respond!")

#Loop for Mail
while True:
    checkMail()
    time.sleep(10)
