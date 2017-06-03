from flask import Flask
import config

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


@app.route("/client_token", methods=["GET"])
def client_token():
    return braintree.ClientToken.generate()
