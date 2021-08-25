import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify


app = Flask(__name__)

#################################################
# Database Setup
#################################################

#from config import username, password, server, database

username = "postgres"
password = "group4winners"
server = "finalprojgroup4.c26jlhodxytp.us-east-2.rds.amazonaws.com"
database = "FinalProjGroup4"

conn = f'postgresql+psycopg2://{username}:{password}@{server}/{database}'

from flask_sqlalchemy import SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conn
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Training(db.Model):
    __tablename__ = 'training_data'

    index = db.Column(db.BigInteger, primary_key=True)
    urls = db.Column(db.Text)
    headline = db.Column(db.Text)
    body = db.Column(db.Text)
    label = db.Column(db.BigInteger)

    def __repr__(self):
        return '<Training %r>' % (self.urls)

#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data/api")
def return_json():
    results = db.session.query(Training.index, Training.urls, Training.headline, Training.body, Training.label).all()

    training_list = []

    for result in results:

        data_training = {
            "index": result[0],
            "URLs": result[1],
            "Headline": result[2],
            "Body": result[3],
            "Label": result[4]
        }
        training_list.append(data_training)

    return jsonify(training_list)

if __name__ == "__main__":
    app.run(debug=True)