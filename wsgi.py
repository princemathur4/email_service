import os
from app import create_app, LOCAL, PROD

env = PROD
app = create_app(env)

app.run(host="127.0.0.1", port="5000")