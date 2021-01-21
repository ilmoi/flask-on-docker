from dotenv import load_dotenv
from flask import Flask, jsonify

from get_secrets import retrieve_secret


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def hello():
    load_dotenv()
    secret = retrieve_secret("SATOSHI")
    return jsonify(secret)


if __name__ == "__main__":
    print('main')
    # we could specify a port below with port="123"
    app.run(debug=True, host='0.0.0.0')
