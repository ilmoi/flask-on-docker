import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from get_secrets import retrieve_secret


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def hello():
    return 'Version 12'


@app.route('/env')
def env():
    return f"{os.environ.get('USER')}, {os.environ.get('PASSWD')}"


@app.route('/secret')
def test_secret():
    load_dotenv()
    secret = retrieve_secret("SATOSHI")
    return jsonify(secret)


if __name__ == "__main__":
    print('main')
    # we could specify a port below with port="123"
    app.run(debug=True, host='0.0.0.0')
