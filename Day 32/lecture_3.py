"""
REVISION NOTES: SENDING EMAIL WITH PYTHON
=========================================

1. How email works
------------------
- Your program sends a message to your email provider's mail server.
- That server passes the message to the recipient's mail server.
- The recipient reads the message from their provider.
- SMTP (Simple Mail Transfer Protocol) is the standard used to send email.

Think of SMTP as the postal system that moves a letter between post offices.

2. The smtplib module
---------------------
Python's built-in ``smtplib`` module connects to an SMTP server and sends mail.
Common SMTP server addresses include:

- Gmail: ``smtp.gmail.com``
- Yahoo: ``smtp.mail.yahoo.com``

The usual port for SMTP with STARTTLS is 587. Provider settings can change, so
check your email provider's current instructions when setting up an account.

3. The main steps
-----------------
1. Create an SMTP connection.
2. Call ``starttls()`` to encrypt the connection.
3. Log in with the sender's email address and an app password.
4. Send the message.
5. Close the connection.

Using ``with`` closes the connection automatically, even if an error occurs.

4. Subject and body
-------------------
An email needs a blank line between its headers and its body:

    Subject: A simple subject\n\nThis is the email body.

The ``EmailMessage`` class used below builds this structure for us and helps
avoid formatting mistakes.

5. Security and beginner tips
-----------------------------
- Never put your normal password or app password directly in Python code.
- Store secrets in environment variables and do not commit them to Git.
- Gmail and Yahoo normally require two-step verification and an app password.
- Use a separate test account while learning.
- Check the spam folder if a test message does not appear in the inbox.
- Check the server address, port, email addresses, and password for typos.
- A successful Python run means the server accepted the message; delivery may
  still be delayed or filtered as spam.

6. Running this example in PowerShell
-------------------------------------
Set the three environment variables, then run this file:

    $env:EMAIL_ADDRESS = "your_test_account@gmail.com"
    $env:EMAIL_APP_PASSWORD = "your_app_password"
    $env:EMAIL_RECIPIENT = "recipient@example.com"
    python main.py

These values last only for the current PowerShell session. Do not replace the
placeholders in this file with real login details.
"""

import os
import smtplib
from email.message import EmailMessage


# Change these values if you use another email provider.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email() -> None:
    """Send one test email using details stored in environment variables."""
    # Read private values without writing them directly in this file.
    sender = os.environ.get("EMAIL_ADDRESS")
    app_password = os.environ.get("EMAIL_APP_PASSWORD")
    recipient = os.environ.get("EMAIL_RECIPIENT")

    # Give a clear error instead of trying to log in with missing values.
    if not all((sender, app_password, recipient)):
        raise RuntimeError(
            "Set EMAIL_ADDRESS, EMAIL_APP_PASSWORD, and EMAIL_RECIPIENT first."
        )

    # EmailMessage safely creates the Subject, From, To, and body sections.
    message = EmailMessage()
    message["Subject"] = "Hello from Python"
    message["From"] = sender
    message["To"] = recipient
    message.set_content("This is the body of my email.")

    # The connection closes automatically when the with block finishes.
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()  # Encrypt communication with the mail server.
        connection.login(user=sender, password=app_password)
        connection.send_message(message)


if __name__ == "__main__":
    # Running this file sends the email after the environment variables are set.
    send_email()
