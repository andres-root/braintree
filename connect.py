from flask import Flask, request
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
    nonce_from_the_client = request.form['payment_method_nonce']
    amount = request.form['amount']
    print(amount)
    result = core.braintree.Transaction.sale({
        'amount': amount,
        # 'payment_method_nonce': 'fake-valid-nonce',
        'payment_method_nonce': nonce_from_the_client,
        'options': {
            'submit_for_settlement': True
        }
    })
    # import ipdb; ipdb.set_trace()
    return result.transaction.Status.Authorized


if __name__ == "__main__":
    app.run(host='0.0.0.0')
