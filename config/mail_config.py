import os
MAIL_SERVER='smtp.mailgun.org'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER='flask@example.com'