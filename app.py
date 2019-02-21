from flask import Flask, render_template
from pymongo import MongoClient

from final_ranking_for_all_three_modules import final_rank_SE, final_rank_SSE, github_rank_SE, github_rank_SSE
from github_final_ranking import*
from final_ranking import get_features, get_features_github
from github_finalrank_read_csv import*
from stack_finalrank_csv import se_sorted_list_stack, sse_sorted_list_stack

app = Flask(__name__)


@app.route('/')
def hello_world():
    list = get_features()
    return render_template('index.html',feature_list = list)


@app.route('/GithubRank', methods=['GET'])
def code_quality():
    try:
        users_se = se_sorted_list()
        users_sse = sse_sorted_list()
        return render_template('code_quality_view.html',se_list = users_se, sse_list = users_sse)
    except Exception as ex:
        print ('error occured: '+str(ex))
        return render_template('index.html')

@app.route('/stackRank', methods=['GET'])
def stack_rank():
    try:
        users_se = se_sorted_list_stack()
        users_sse = sse_sorted_list_stack()
        return render_template('code_quality_view.html',se_list = users_se, sse_list = users_sse)
    except Exception as ex:
        print ('error occured: '+str(ex))
        return render_template('index.html')



@app.route('/test_chart', methods=['GET'])
def display_chart():
    return render_template('chart.html')

@app.route('/github_priority', methods=['GET'])
def set_priority_github():
    list = get_features_github()
    return render_template('index2.html',feature_list=list)

@app.route('/change_priority_github', methods=['POST'])
def change_priority_github():
    sorted_list_SE = []
    sorted_list_SSE = []
    try:
        list_of_priorities =  request.form.getlist('values')
        print(list_of_priorities)
        sorted_list_SE = github_rank_SE(list_of_priorities)
        sorted_list_SSE = github_rank_SSE(list_of_priorities)
        print(sorted_list_SE)
        print(sorted_list_SSE)
    except Exception as ex:
        print('Error occurred: '+str(ex))
    return render_template('code_quality_view.html', se_list = sorted_list_SE,sse_list=sorted_list_SSE)


@app.route('/change_priority', methods=['POST'])
def change_priority():
    sorted_list_SE = []
    sorted_list_SSE = []
    try:
        list_of_priorities =  request.form.getlist('values')
        print(list_of_priorities)
        sorted_list_SE=final_rank_SE(list_of_priorities)
        sorted_list_SSE=final_rank_SSE(list_of_priorities)
        print(sorted_list_SE)
        print(sorted_list_SSE)
    except Exception as ex:
        print('Error occurred: '+str(ex))
    return render_template('code_quality_view.html', se_list = sorted_list_SE,sse_list=sorted_list_SSE)

from flask import request





if __name__ == '__main__':
    app.run()
