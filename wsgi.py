from app import create_app, PROD, LOCAL

env = PROD
app = create_app(env)
