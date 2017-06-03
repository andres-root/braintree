from flask import Flask
import core

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/client_token", methods=["GET"])
def client_token():
    return core.braintree.ClientToken.generate()


if __name__ == "__main__":
    app.run()
