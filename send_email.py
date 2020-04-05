import smtplib
import os
from  email.message import EmailMessage
import imghdr


# Basic Form

EMAIL_ADDRESS = "******@gmail.com"
PASSWORD = "******"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() # identify yourself to server
    smtp.starttls() # encrypt the transaction
    smtp.ehlo() # re-identify yourself after encryption
    smtp.login(EMAIL_ADDRESS, PASSWORD)

    subject = 'Grab dinner this weekend'
    body = 'how about dinner at 6pm this saturday'
    msg = f'Subject: {subject}\n\n{body}' # f-string
    smtp.sendmail(EMAIL_ADDRESS, 'targetMail@gmail.com', msg)


# ========================================
# sending attachments

msg_1 = EmailMessage()
msg_1['Subject'] = 'my puppies image'
msg_1['From'] = EMAIL_ADDRESS
msg_1['To'] = 'targetMail@gmail.com'
msg_1.set_content('Image attached')

# attach several files to the email
files = ['1.png', '2.jpg']

for file in files:
    with open("./Files/"+file, 'rb') as f:
        file_date = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg_1.add_attachment(file_date, maintype='image', subtype=file_type, filename= file_name)


# using SSL connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    smtp.send_message(msg_1)


# ========================================
# sending to several emails

contacts = ['targetMail_1@gmail.com', 'targetMail_2@example.com']

msg_2 = EmailMessage()
msg_2['Subject'] = 'my puppies msg'
msg_2['From'] = EMAIL_ADDRESS
msg_2['To'] = ', '.join(contacts)
msg_2.set_content('random spam!')

# using SSL connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    smtp.send_message(msg_2)


#========================================
# sending with html

msg_3 = EmailMessage()
msg_3['Subject'] = 'my puppies again'
msg_3['From'] = EMAIL_ADDRESS
msg_3['To'] = 'targetMail_1@gmail.com'
msg_3.set_content('random spam!')

msg_3.add_alternative('''\
    <html><body><h1>this is an HTML email!</h1></body></html>
    ''', subtype='html')

# using SSL connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    smtp.send_message(msg_3)