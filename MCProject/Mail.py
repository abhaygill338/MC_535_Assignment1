import smtplib
import ssl


def send_mail(user_email, message):
    port = 465  # For SSL
    system_email = "mc.project.23.xyz@gmail.com"
    password = "asdf1@34"

    # user_email = "mayur.padaval@gmail.com"
    # message = "Hi there, \n Please buy groceries for this week!"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("mc.project.23.xyz@gmail.com", password)
        server.sendmail(system_email, user_email, message)
