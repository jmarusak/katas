import imaplib
import email

# Connect to Yahoo Mail
mail = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
mail.login("<email>", "<app password>")

# Select inbox
mail.select("agents")

# Search all emails
status, messages = mail.search(None, "ALL")

for num in messages[0].split():
    status, data = mail.fetch(num, "(RFC822)")
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Get email content
    subject = msg["subject"]
    from_ = msg["from"]

    print(from_)
