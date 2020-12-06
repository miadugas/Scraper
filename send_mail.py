import smtplib
# bring in the by fault email module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
 
# turned into a function to import into scrape.py
# put your own values in the from & to email fields
def send(filename):
    from_add = "from_email@gmail.com"
    to_add = "to_email@gmail.com"
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg["From"] = from_add
    msg["To"] = to_add
    msg["Subject"] = subject

    body = "<b>Today's Report Attached</b>"
    msg.attach(MIMEText(body, "html"))

    my_file = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= " + filename)
    msg.attach(part)

    message = msg.as_string()

# start a mail server
    server = smtplib.SMTP("smtp.gmail.com", 587)
# make the server secure
    server.starttls()
# login info & from , could use a .env file but trying to keep lines of code at minimum
# instead used gmail to simply generate a custom password for this app
# add your own server login password 
    server.login(from_add, "server_password_here")

    server.sendmail(from_add, to_add, message)

# quit the server once sent
    server.quit()