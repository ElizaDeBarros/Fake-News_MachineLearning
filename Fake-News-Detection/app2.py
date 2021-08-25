import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify


app = Flask(__name__)

#################################################
# Database Setup
#################################################

from config import username, password, server, database

conn = f"host='{server}' dbname='{database}' user='{username}' password='{password}'"

from flask_sqlalchemy import SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conn
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Training(db.Model):
    __tablename__ = 'training_data'

    index = db.Column(db.Integer, primary_key=True)
    urls = db.Column(db.String)
    headline = db.Column(db.String)
    body = db.Column(db.String)
    label = db.Column(db.Integer)

    def __repr__(self):
        return '<training_data %r>' % (self.name)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
#    return ( "Welcome to the homepage"
    return(
        "/data will take you to the json information"
        #render_template("index.html")
    )
@app.route('/return')
def return_info():
    results = db.session.query(Training.urls).all()
    
    index = [result[0] for result in results]
    url = [result[1] for result in results]
    headline = [result[2] for result in results]
    body = [result[3] for result in results]
    label = [result[4] for result in results]

    data_training = [{
        "index": index,
        "URLs": url,
        "Headline": headline,
        "Body": body,
        "Label": label
    }]

    return jsonify(data_training[0:2])

@app.route('/data')
def send_data():
    con = psycopg2.connect(conn)  
    cur = con.cursor()
    cur.execute("""select * from  training_data""")
    data = [col for col in cur]
    cur.close()
    return jsonify(data[0]])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)