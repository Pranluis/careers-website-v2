import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def send_mail(recmail, recname, jobname):
    # Email credentials
    sender_email = "pranluis20@gmail.com"
    sender_password = "bzjm gido muxz uyvx"

    # Recipient email
    recipient_email = recmail

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Confirmation of Job Application Submission"

    # Email body
    body = '''Dear Applicant

I hope this email finds you well. I am writing to confirm that we have received your application 
for the XXX position at Luidlink.

We appreciate the time and effort you invested in preparing and submitting your application. 
Your resume and cover letter have been successfully received, and we are currently reviewing them.

Our hiring team will carefully assess your qualifications and experience to determine if they align 
with our requirements for the position. We will contact you directly if we require any further information or to 
schedule an interview.

In the meantime, please feel free to reach out if you have any questions or require additional information 
regarding your application.

Thank you once again for your interest for applying at Luidlink

Best regards

Priyanshu Raj
HR
Luidlink
pranluis20@gmail.com

'''
    body = body.replace("Applicant", recname)
    body = body.replace("XXX", jobname)
    
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your Gmail account
    server.login(sender_email, sender_password)

    # Send email
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)

    # Close connection
    server.quit()

    print("Email sent successfully!")


