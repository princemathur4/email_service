import re
from modules.mail_service.controller import MailServiceController


class MailServiceUtils:

    @staticmethod
    def send_email(user_name, recipient_email):
        message = f"Hi {user_name},\n" \
                  f"Here is your requested content.\n\n" \
                  f"--------- <content> ---------\n\n" \
                  f"Hope you enjoy your day!\n" \
                  f"Your friendly neighbourhood,\n" \
                  f"Mail-Man"
        MailServiceController().send_mail(subject="Test Email", recipient_email=recipient_email, content=message)

    @staticmethod
    def check_email(email: str) -> bool:
        """
        Checks if a string is a valid email or not
        :param email: str
        :return: bool
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return True
        return False
