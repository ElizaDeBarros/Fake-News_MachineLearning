import psycopg2
import sys
from flask import Flask,render_template, request
from flask import jsonify


app = Flask(__name__, template_folder='templates')

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

class Prediction(db.Model):
    __tablename__ = 'prediction_data'

    index = db.Column(db.BigInteger, primary_key=True)
    Body = db.Column(db.Text)
    Logistic_Regression = db.Column(db.Text)
    Naive_Bayes = db.Column(db.Text)
    Decision_Tree = db.Column(db.Text)
    Passive_Aggressive_Classifier = db.Column(db.Text)

    def __repr__(self):
        return '<Prediction %r>' % (self.Body)

###
### Method to load in model once there is a saved model ###
###
#import joblib
#filename = "Data_Gathering/Resources/test_model_save.sav"
#loaded_model = joblib.load(filename)

#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/", methods={'GET', 'POST'})
def home():
    #if request.method == 'GET':
    #    return (render_template("index.html"))
    
    #if request.method == 'POST':
    #    news = request.form['form']

    #    input_variables = pd.DataFrame([[news]], columns= ['text'], dtype=float)
    #    prediction = loaded_model.predict(input_variables)[0]

    #    return (render_template("index.html", original_input={
    #        'Text': news
    #        },
    #        result=prediction
    #        ))

    if request.method == 'POST':
        text = request.form['text']
        return text
    else:
        return render_template('index.html')

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

@app.route("/data/predictions")
def return_json():
    results = db.session.query(Prediction.index, Prediction.Body, Prediction.Logistic_Regression, Prediction.Naive_Bayes, Prediction.Decision_Tree, Prediction.Passive_Aggressive_Classifier).all()

    prediction_list = []

    for result in results:

        data_prediction = {
            "index": result[0],
            "Body": result[1],
            "Logistic_Regression": result[2],
            "Naive_Bayes": result[3],
            "Decision_Tree": result[4],
            "Passive_Aggressive_Classifier": result[5]
        }
        training_list.append(data_prediction)

    return jsonify(prediction_list)

if __name__ == "__main__":
    app.run(debug=True)