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

con = psycopg2.connect(conn)  
cur = con.cursor()
cur.execute("""select * from  training_data""")
data = [col for col in cur]

index = [result[0] for result in data]
url = [result[1] for result in data]
headline = [result[2] for result in data]
body = [result[3] for result in data]
label = [result[4] for result in data]

data_training = [{
    "index": index,
    "URLs": url,
    "Headline": headline,
    "Body": body,
    "Label": label
}]

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
#    return ( "Welcome to the homepage"
    return(
        #"/data will take you to the json information"
        render_template("index.html")
    )
@app.route('/return')
def return_info():
    

    index = [result[0] for result in data]
    url = [result[1] for result in data]
    headline = [result[2] for result in data]
    body = [result[3] for result in data]
    label = [result[4] for result in data]

    data_training = [{
        "index": index,
        "URLs": url,
        "Headline": headline,
        "Body": body,
        "Label": label
    }]

    return jsonify(data_training)

@app.route('/data/api')
def send_data():

    return jsonify(data_training)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)