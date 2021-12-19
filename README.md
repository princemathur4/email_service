# Email-Service
## Features
- Provides abstraction to the user between two different email service providers
- If one of the services goes down, service can quickly fail-over to a different provider without
affecting customer's user experience.
- Email Providers used: 
    - Mailgun
    - Flask Mail

## API Documentation
### Send Mail
   This API sends a dummy mail to the given user and email address.

* **URL**: /send_mail
* **Method:** `POST`
*  **Data Params**: 

   **Required:**
   `user_name=[string]` <br />
   **Required:**
   `email=[string]`

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `{"status": True, "message": "Mail sent successfully. Please check your inbox."}`
 
* **Error Response:**

  * **Code:** 400 BAD_REQUEST <br />
    **Content:** `{"status": False, "message": 'Invalid request params/payload'}`

  OR

  * **Code:** 500 INTERNAL_SERVER_ERROR <br />
    **Content:** `{"status": False, "message": 'Couldn't send email'}`

  OR

  * **Code:** 500 INTERNAL_SERVER_ERROR <br />
    **Content:** `{"status": False, "message": 'Something went wrong'}`

## Deployments
This Flask Project is deployed on heroku at url: `https://email-service-flask.herokuapp.com`

* **Sample cURL:**

  `curl --location --request POST 'https://email-service-flask.herokuapp.com/send_mail' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_name":"Bruce Wayne",
    "email": "bruce@wayne.enterprise.com"
}'` 

## To setup project on your machine
- Install python3 if not installed already
- Clone the repository using: `git clone https://github.com/princemathur4/email_service`
- cd into the project root folder
- Create a Python3 virtual env using: `python3 -m venv ./virtualenv`
- Activate the virtual env for your command line,

For Windows:
`.\virtualenv\Scripts\activate`

For Linux:
`source ./virtualenv/bin/activate`
- install packages using requirement.txt file `pip install -r requirements.txt`
 
## Run
- cd into the project root folder
- Activate virtual env like mentioned above
- Update `config.py` env specific config variables according to your requirements
- Update your credentials in the `.env` file
- Run using command:

For Windows:
`waitress-serve --host=0.0.0.0 --port=5000 --threads=4 wsgi:app`

For Linux:
`gunicorn --bind 0.0.0.0:5000 --workers=2 --threads=4 wsgi:app --access-logfile -`
