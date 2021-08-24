import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify


app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
#    return ( "Welcome to the homepage"
    return(
        "/data will take you to the json information"
    )

@app.route('/data')
def send_data():
    con = psycopg2.connect("host='finalprojgroup4.c26jlhodxytp.us-east-2.rds.amazonaws.com' dbname='FinalProjGroup4' user='postgres' password='group4winners'")  
    cur = con.cursor()
    cur.execute("""select * from  training_data""")
    data = [col for col in cur]
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)