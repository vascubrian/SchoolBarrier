from flask import Flask
from celery_copy import make_celery
from os import path, environ
import json

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_BACKEND'] = 'postgresql://barrier_db:123@localhost:5432/barrier_db'

celery = make_celery(app)

@app.route('/process/<phone_no>')
def process(phone_no):
	sendSms.delay(phone_no)
	return "Sending sms in progess"

@celery.task(name="send_sms")
def sendSms(PhoneNo):

	return "Test Brian"

if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)