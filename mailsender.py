import smtplib

def sendMail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    password =input("Please type in the password:")
    server.login("timo.schessl@gmail.com",password)

    subject="Python Test Mail"
    body = "This is a python test email from me."

    message= f"Subject: {subject}\n\n{body}"

    server.sendmail(
      "timo.schessl@gmail.com",
      "timo.schessl@gmail.com",
       message)


sendMail()
print("Email sent successfully!")