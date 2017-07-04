import smtplib
import getpass

username= input("Enter your email: ")
password= getpass.getpass("Enter your passwd: ")

recipient = input("Enter email to person you are emailing: ")
msg= input("Enter your messenger: ")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(username, recipient, msg)
print("Message sent!")
server.quit()
print()
