from flask import Flask
from celery_copy import make_celery
from os import path, environ
from models import db,DbBarrier
import json
import datetime


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_BACKEND'] = 'postgresql://barrier_db:123@localhost:5432/barrier_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://barrier_db:123@localhost:5432/barrier_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

celery = make_celery(app)

@app.route('/process/<phone_no>')
def process(phone_no):
	#sendSms.delay(phone_no)


	
	result=DbBarrier.query.order_by(DbBarrier.dt_trans_date.desc()).limit(1)
	if result is not None:
		for data_value in result:
			fmt = '%Y-%m-%d %H:%M:%S'
			#system time
			system_date = datetime.datetime.now()
			#db time
			check_date=data_value.tm_realtime
			print check_date 
			print "--"
			print type(check_date)
			print system_date 
			print "--"
			print type(system_date)
			#p = system_date - check_date

			print "nothing"



			return "something"
	else:
		return "Sending sms in progess2"


@celery.task(name="send_sms.sendSms")
def sendSms():
	


	return "Test Brian"


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)