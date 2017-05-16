import smtplib


file = open(".\password", 'r')
username = file.readline()
pw = file.readline()

# Create a text/plain message
msg = "Just a test"

me = 'Test@testing.ch'
you = 'becher.florian@outlook.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, pw)
server.sendmail(me, you, msg)
server.quit()
