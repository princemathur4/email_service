from app import create_app, PROD, LOCAL

env = PROD
app = create_app(env)

app.run(host="0.0.0.0", port="80")