##Email word counter

from decimal import Subnormal
import smtplib
import getpass
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)

username = getpass.getpass('Please enter your username: ')
password = getpass.getpass('Please enter your gmail password: ')

print(smtp_obj.ehlo())
print(smtp_obj.starttls())

smtp_obj.login(username,password)

from_address = username
to_address = input('Send email to? (@gmail.com): ')

subject = input('Subject?: ')
message = input('Message?: ')

msg = "Subject: " + subject + '\n' + message


smtp_obj.sendmail(from_address,to_address,msg)

print('Message sent! ')
mes = message.split()
sub = subject.split()

print(f'The ammount of words in the message is {len(mes)}')
print(f'The ammount of words in the subject is {len(sub)}')




