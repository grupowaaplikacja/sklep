from flask import *
from werkzeug import *
from flask_sqlalchemy import SQLAlchemy
from  model.user import User
import os

app = Flask(__name__)
app.secret_key ='bardzosekretnyklucz'
project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir,"model/database.db"))
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '44444', ssl_context=('ssl/cert.pem', 'ssl/key.pem'))


#admin = User(email='fsdfsd', password='gag',first_name='gfdgdsf',last_name='gfdgsf', phone='53243',role=1)
#db.session.add(admin)
#db.session.commit()

#User.query.all()
