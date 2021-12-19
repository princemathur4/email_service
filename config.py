import os
from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv

load_dotenv()

LOCAL = "LOCAL"
PROD = "PROD"
ENVIRONMENTS = [LOCAL, PROD]


class Config(metaclass=ABCMeta):
    """
    Acts as abstract class for env specific configs
    Also acts as a base class which contains variables that are common among different environments
    """
    
    @property
    @abstractmethod
    def __env_name__(self,):
        pass

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = "princemathur.mathur4@gmail.com"
    MAIL_USERNAME = "princemathur.mathur4@gmail.com"
    MAILGUN_SERVICE_API_BASE_URL = "https://api.mailgun.net/v3"
    MAILGUN_SERVICE_DOMAIN_NAME = "sandbox6e1626c40d924137a0559db81d68bf17.mailgun.org"
    MAILGUN_SERVICE_API_KEY = os.getenv("MAILGUN_SERVICE_API_KEY")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class DevelopmentConfig(Config):
    __env_name__ = LOCAL

    DEBUG = True


class ProductionConfig(Config):
    __env_name__ = PROD

    DEBUG = False
