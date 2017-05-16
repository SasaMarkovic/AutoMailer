import smtplib


file = open('C:\Daten\projects\python\AutoBot\password', 'r')
first_line = file.readline()
print(first_line)


#username = 'becher.florian97@gmail.com'

# Create a text/plain message
#msg = "Just a test"

#me = 'Test@testing.ch'
#you = 'becher.florian@outlook.com'

#server = smtplib.SMTP('smtp.gmail.com:587')
#server.starttls()
#server.login(username, pw)
#server.sendmail(me, you, msg)
#server.quit()