from flask import Flask
import core

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/client_token", methods=["GET"])
def client_token():
    return core.braintree.ClientToken.generate()


@app.route("/checkout", methods=["POST"])
def create_purchase():
    # nonce_from_the_client = request.form["payment_method_nonce"]
    result = core.braintree.Transaction.sale({
        'amount': '10.00',
        'payment_method_nonce': 'fake-valid-nonce',
        'options': {
            'submit_for_settlement': True
        }
    })
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0')
