from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    # def __repr__(self):
    #     """Define a base way to print models"""
    #     return '%s(%s)' % (self.__class__.__name__, {
    #         column: value
    #         for column, value in self._to_dict().items()
    #     })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class UserLogin(BaseModel, db.Model):
    """Model for the mst_logn table"""
    __tablename__ = 'mst_login'

    nu_user_id = db.Column("nu_user_id",db.Integer,primary_key = True)
    vc_user_name = db.Column(db.String)
    vc_pass_word = db.Column(db.String)
    vc_user_email = db.Column(db.String)
    vc_user_type = db.Column(db.String)
    def __init__(self,nu_user_id,vc_user_name,vc_pass_word,vc_user_email,vc_user_type):
        self.nu_user_id=nu_user_id
        self.vc_user_name=vc_user_name
        self.vc_pass_word=vc_pass_word
        self.vc_user_email=vc_user_email
        self.vc_user_type=vc_user_type

class DbBarrier(BaseModel, db.Model):
    """Model for the dt_barrier table"""
    __tablename__ = 'dt_barrier'

    nu_trans_id = db.Column(db.Integer, primary_key = True)
    dt_trans_date = db.Column(db.DateTime)
    nu_phone_no = db.Column(db.Integer)
    vc_remind =db.column(db.String)
    tm_realtime=db.column(db.DateTime)
    def __init__(self,dt_trans_date,nu_phone_no,vc_remind,tm_realtime):
        self.dt_trans_date=dt_trans_date
        self.nu_phone_no=nu_phone_no
        self.vc_remind=vc_remind
        self.tm_realtime=tm_realtime





	



