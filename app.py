from flask import Flask, render_template
from pymongo import MongoClient

from final_ranking_for_all_three_modules import final_rank_linkedIn_SE, final_rank_linkedIn_SSE, final_rank_SE, \
    final_rank_SSE
from github_final_ranking import*
from final_ranking import get_features, get_integrated_features
from github_finalrank_read_csv import*


app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'starc_db'
#app.config['MONGO_URI'] = 'mongodb://ruchira:welcome123@ds161804.mlab.com:61804/starc_db'

client = MongoClient("mongodb://ruchira:welcome123@ds161804.mlab.com:61804/starc_db") #host uri
db = client.starc_db #Select the database

@app.route('/')
def hello_world():
    list = get_features()
    return render_template('index.html',feature_list = list)

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
        users_se = se_sorted_list()
        users_sse = sse_sorted_list()
        return render_template('code_quality_view.html',se_list = users_se, sse_list = users_sse)
    except Exception as ex:
        print ('error occured: '+str(ex))
        return render_template('index.html')

@app.route('/LinkedInRank', methods=['GET'])
def linkedIn_rank():
    try:
        users_se = se_sorted_list()
        users_sse = sse_sorted_list()
        return render_template('code_quality_view.html',se_list = users_se, sse_list = users_sse)
    except Exception as ex:
        print ('error occured: '+str(ex))
        return render_template('index.html')

@app.route('/finalRank', methods=['GET'])
def final_rank():
    try:
        users_se = se_sorted_list_final()
        users_sse = sse_sorted_list_final()
        return render_template('code_quality_view.html',se_list = users_se, sse_list = users_sse)
    except Exception as ex:
        print ('error occured: '+str(ex))
        return render_template('index.html')

@app.route('/test_chart', methods=['GET'])
def display_chart():
    return render_template('chart.html')

from flask import request
@app.route('/change_priority', methods=['POST'])
def change_priority():

    try:
        list_of_priorities = request.form.getlist('values')
        # print(list_of_priorities)
        sorted_list_SE=final_rank_linkedIn_SE(list_of_priorities)
        sorted_list_SSE=final_rank_linkedIn_SSE(list_of_priorities)
        # print(sorted_list_SE)
        # print(sorted_list_SSE)
    except Exception as ex:
        print('Error occurred: '+str(ex))
    return render_template('code_quality_view.html', se_list = sorted_list_SE,sse_list=sorted_list_SSE)

@app.route('/display_final_rank', methods=['POST'])
def display_final_rank():

    try:
        list_of_priorities = request.form.getlist('values')
        # print(list_of_priorities)
        sorted_list_SE = final_rank_SE(list_of_priorities)
        sorted_list_SSE = final_rank_SSE(list_of_priorities)
        # print(sorted_list_SE)
        # print(sorted_list_SSE)
    except Exception as ex:
        print('Error occurred: '+str(ex))
    return render_template('code_quality_view.html', se_list = sorted_list_SE,sse_list=sorted_list_SSE)

@app.route('/finalRankPriority', methods=['GET'])
def finalRankPriority():
    list = get_integrated_features()
    return render_template('index2.html', feature_list=list)

if __name__ == '__main__':
    app.run()
