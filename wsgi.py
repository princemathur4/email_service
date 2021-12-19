from app import create_app, PROD, LOCAL

env = PROD
app = create_app(env)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="5000")