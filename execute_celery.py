from flask import Flask
from celery_copy import make_celery
from os import path, environ
from models import db,DbBarrier
import datetime
import schedule
import time

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_BACKEND'] = 'postgresql://barrier_db:123@localhost:5432/barrier_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://barrier_db:123@localhost:5432/barrier_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

celery = make_celery(app)

@app.route('/')
def process():
	
	sendSms.delay()

	return "Sendings sms in progress"

@celery.task(name="send_sms_flag")
def sendSms():

	#getting db_flag...................................................

	barrier_data=db.session.query(DbBarrier).filter_by(dt_trans_date=str(datetime.date.today()),vc_remind='N').first()
	if barrier_data is not None:
	   	try:
	   		#send sms_function

	   		#update flag
            dt_update=db.session.query(DbBarrier).filter_by(nu_trans_id =barrier_data.nu_trans_id).first()
            dt_update.vc_remind = 'Y'
            db.session.commit()

	   		return "SMS is sent successfully !!"

    	except:
    		return "Failed to send sms"

    else:
    	pass




if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)