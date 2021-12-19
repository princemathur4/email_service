from smtplib import SMTPException
from modules.exceptions import EmailNotSent
from modules.mail_service.providers import BaseMailServiceProvider
from flask_mail import Mail, Message, BadHeaderError, FlaskMailUnicodeDecodeError

mail = Mail()


class FlaskMailService(BaseMailServiceProvider):
    __provider_name__ = "Flask Mail Service"

    def send_mail(self, subject, body, recipient_email):
        try:
            msg = Message(subject=subject, body=body, recipients=[recipient_email])
            _ = mail.send(msg)
        except (ConnectionError, BadHeaderError, FlaskMailUnicodeDecodeError, SMTPException) as e:
            print(f"Error in {self.__provider_name__}: {e}")
            raise EmailNotSent(internal_err_message=f"Error occurred while sending mail using {self.__provider_name__}")
