from flask import Flask
from models import db

senti = Flask(__name__)

# load config from the config file we created earlier
senti.config.from_object('config')

# initialize and create the database
db.init_app(senti)
db.create_all(app=senti)

@senti.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    senti.run()
