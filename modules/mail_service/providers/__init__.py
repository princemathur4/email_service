from abc import ABCMeta, abstractmethod


class BaseMailServiceProvider(metaclass=ABCMeta):

    @classmethod
    def get_all_subclasses(cls):
        from modules.mail_service.providers.mail_gun import MailGunMailService
        from modules.mail_service.providers.flask_mail import FlaskMailService
        return cls.__subclasses__()

    @property
    @abstractmethod
    def __provider_name__(self,):
        pass

    @abstractmethod
    def send_mail(self, *args, **kwargs):
        pass
