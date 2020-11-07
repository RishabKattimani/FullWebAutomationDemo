import smtplib, ssl

port = 465  # For SSL
def send_email(receiver_email, message):
    smtp_server = "smtp.gmail.com"
    sender_email = ""  # Enter your address
    password = (Enter_Your_Password_Here)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return
