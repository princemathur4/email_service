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
