from flask import *
from werkzeug import *

#jakies fajne zmienne nie wiem ocb
app = Flask(__name__)
app.secret_key ='bardzosekretnyklucz'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '44444', ssl_context=('ssl/cert.pem', 'ssl/key.pem'))


