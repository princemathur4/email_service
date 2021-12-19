from abc import ABCMeta, abstractmethod


class BaseMailServiceProvider(metaclass=ABCMeta):
    """
    Abstract class for mail service providers
    """

    @classmethod
    def get_all_subclasses(cls):
        from modules.mail_service.providers.mail_gun import MailGunMailService
        from modules.mail_service.providers.flask_mail import FlaskMailService
        return cls.__subclasses__()

    @property
    @abstractmethod
    def __provider_name__(self,):
        """
        (Abstract method)
        Identifier for each subclass to denote the name of the service provider
        """
        pass

    @abstractmethod
    def send_mail(self, *args, **kwargs):
        """
        (Abstract method)
        Logic for Sending mail or raising necessary errors goes in this function
        """
        pass
