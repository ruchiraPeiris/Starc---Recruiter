from flask import Flask, render_template
from pymongo import MongoClient

from Github.github_final_ranking import*

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'starc_db'
#app.config['MONGO_URI'] = 'mongodb://ruchira:welcome123@ds161804.mlab.com:61804/starc_db'

client = MongoClient("mongodb://ruchira:welcome123@ds161804.mlab.com:61804/starc_db") #host uri
db = client.starc_db #Select the database

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add')
def  add():
    name = 'sahan'
    all_users = db.users
    user = all_users.find_one({'name':name})
    if user:
        return 'existing user'
    else:
        all_users.insert({'name':name})
        return 'user added'


@app.route('/GithubRank', methods=['GET'])
def code_quality():
    try:
        users_se = se_list_github()
        users_sse = sse_list_github()
        return render_template('code_quality_view.html',se_list = users_se, sse_list = users_sse)
    except Exception as ex:
        print ('error occured: '+str(ex))
        return render_template('index.html')


@app.route('/test_chart', methods=['GET'])
def display_chart():
    return render_template('chart.html')







if __name__ == '__main__':
    app.run()
