from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def data():
    
    if request.method == 'POST':
        text = request.form['text']
        return text
    else:
        return render_template('index.html')

if __name__=='__main__':
   app.run()