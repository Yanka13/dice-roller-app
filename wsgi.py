# wsgi.py
# API code
import random
from flask import Flask, jsonify
import os

app = Flask(__name__)
sentry_dsn = os.getenv('SENTRY_DSN', None)

if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration
    sentry_sdk.init(
        sentry_dsn,
        integrations=[FlaskIntegration()]
    )
@app.route('/')
def home():
    return jsonify({'roll': random.randint(1,6)})


@app.route('/error')
def error():
    return {1/0}
