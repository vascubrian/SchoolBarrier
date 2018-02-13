from flask import Flask
from models import db,UserLogin
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)


app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://barrier_db:123@localhost:5432/barrier_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Log me out</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    #checking whether user exists................................
    my_user=db.session.query(UserLogin).filter_by(vc_user_name=request.form['username'],vc_pass_word=request.form['password']).first()
    if my_user is not None:
        #success login.................
        session['logged_in'] = True
        session['user_name'] =my_user.vc_user_name
    else:
        #invalid login.................
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    #logout user
    session['logged_in'] = False
    return home() 
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
