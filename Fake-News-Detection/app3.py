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

training_list = []

for result in data:

    data_training = {
        "index": result[0],
        "URLs": result[1],
        "Headline": result[2],
        "Body": result[3],
        "Label": result[4]
    }
    training_list.append(data_training)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return(
        #"/data will take you to the json information"
        render_template("index.html")
    )

@app.route('/data/api')
def return_json():

    return jsonify(training_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)