from flask import Flask, render_template
from flask_pymongo import PyMongo
from load_images import load

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'starc_db'
app.config['MONGO_URI'] = 'mongodb://ruchira:welcome123@ds161804.mlab.com:61804/starc_db'

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add')
def  add():
    return render_template('index.html')


@app.route('/codeQuality', methods=['GET'])
def code_quality():

    return render_template('code_quality_view.html')

if __name__ == '__main__':
    app.run()
