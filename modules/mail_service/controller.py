from modules.exceptions import InvalidInputParameter, EmailNotSent
from modules.mail_service.providers import BaseMailServiceProvider


class MailServiceController:
    """
    Controls the flow of sending an email using all the service providers available
    """

    provider_priority = [
        "Flask Mail Service",
        "Mail Gun"
    ]

    def send_mail(self, recipient_email, subject, content):
        """
        Accepts necessary info and sends email using the all service providers available
        :param recipient_email: str
        :param subject: str
        :param content: str
        """
        for provider_name in self.provider_priority:
            provider_cls = self.get_provider(provider_name=provider_name)
            try:
                obj = provider_cls()
                obj.send_mail(recipient_email=recipient_email, subject=subject, body=content)
                return
            except EmailNotSent:
                pass
        raise EmailNotSent(internal_err_message="All providers failed to send the mail to the recipient")

    @staticmethod
    def get_provider(provider_name: str):
        """
        Returns the provider class corresponding to a given provider_name (if exists)
        :param provider_name: str
        """
        providers = BaseMailServiceProvider.get_all_subclasses()
        for provider in providers:
            if provider.__provider_name__ == provider_name:
                return provider
        raise InvalidInputParameter(internal_err_message="Invalid value for 'provider_name'")
