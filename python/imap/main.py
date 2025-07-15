import os
import imaplib
import email

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# Connect to Yahoo Mail
mail = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Select inbox
mail.select("inbox")

# Search all emails
status, messages = mail.search(None, "ALL")

for num in messages[0].split():
    status, data = mail.fetch(num, "(RFC822)")
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Get email header 
    subject = msg["subject"]
    from_ = msg["from"]

    # Get email body
    body = ...

    print(from_)
