import requests
from http import HTTPStatus
from flask import current_app
from requests import RequestException
from urllib3.exceptions import HTTPError
from modules.exceptions import EmailNotSent
from modules.mail_service.providers import BaseMailServiceProvider


class MailGunMailService(BaseMailServiceProvider):
    __provider_name__ = "Mail Gun"

    def send_mail(self, subject, body, recipient_email):
        url = f'{current_app.config["MAILGUN_SERVICE_API_BASE_URL"]}/{current_app.config["MAILGUN_SERVICE_DOMAIN_NAME"]}/messages'
        try:
            response = requests.post(
                url=url,
                auth=("api", current_app.config["MAILGUN_SERVICE_API_KEY"]),
                data={
                    "from": current_app.config["MAIL_DEFAULT_SENDER"],
                    "to": [recipient_email],
                    "subject": subject,
                    "text": body
                }
            )
            if response.status_code >= 300:
                print(f"Error in {self.__provider_name__}: {response.text}")
                raise EmailNotSent(
                    internal_err_message=f"Error occurred while sending mail using {self.__provider_name__}"
                )
        except (HTTPError, RequestException) as e:
            print(f"Error in {self.__provider_name__}: {e}")
            raise EmailNotSent(
                internal_err_message=f"Error occurred while sending mail using {self.__provider_name__}: {e}"
            )
