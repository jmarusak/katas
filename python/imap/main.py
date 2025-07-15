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
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdisposition = str(part.get("Content-Disposition"))
            # Look for text/plain parts that are not attachments
            if ctype == "text/plain" and "attachment" not in cdisposition:
                body = part.get_payload(decode=True).decode(errors='ignore')
                break # Found the plain text body, exit loop
            # Optionally, handle HTML as a fallback if plain text is not found
            elif ctype == "text/html" and "attachment" not in cdisposition:
                # If no plain text body has been found yet, use HTML
                if not body:
                    body = part.get_payload(decode=True).decode(errors='ignore')
    else:
        # Not multipart, assume it's the main body content
        if msg.get_content_maintype() == 'text':
            body = msg.get_payload(decode=True).decode(errors='ignore')
        # Else, if it's not text (e.g., image), body will remain an empty string

    print(from_)
