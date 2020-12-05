import smtplib
# bring in the by fault email module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
 
# turned into a function to import into scrape.py
def send():
    from_add = "skoden0909@gmail.com"
    to_add = "msmiadugas@gmail.com"
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg["From"] = from_add
    msg["To"] = to_add
    msg["Subject"] = subject

    body = "<b>Heya! Sending mail throigh Python!</b>"
    msg.attach(MIMEText(body, "html"))

    my_file = open("scrape.csv", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + "scrape.csv")
    msg.attach(part)

    message = msg.as_string()

# start a mail server
    server = smtplib.SMTP("smtp.gmail.com", 587)
# make the server secure
    server.starttls()
# login info & from , could use a .env file but trying to keep lines of code at minimum
# instead used gmail to simply generate a custom password for this app
    server.login(from_add, "wwxhzvenaqpljcic")

    server.sendmail(from_add, to_add, message)

# quit the server once sent
    server.quit()