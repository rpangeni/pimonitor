import smtplib
import getpass
import sys

gmail_user = 'rupakpangeni@gmail.com'
gmail_password = getpass.getpass('enter password for gmail account')


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    print("Connected succesfully.")    
except SMTPAuthenticationError as e:
    print ("Something went wrong: ",  sys.exec_info()[0])
    
