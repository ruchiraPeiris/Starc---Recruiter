import csv
import numpy as np
import operator



weights_per_feature = {
'code_comment_percentage': 2,
'code_quality': 2,
'comment_sentiment': 5,
'spelling': 4,
'popularity': 6,
'useof_popular_technologies': 3,
}


def se_list_github():
    se_list = {}
    try:
        with open('Github_repos.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for raw in csv_reader:
                se_list.update({raw[0]: raw[8]})

    except Exception as ex:
        print(str(ex))
    return se_list

#print(se_list_github())

def sse_list_github():
    sse_list = {}
    try:
        with open('Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for raw in csv_reader:
                sse_list.update({raw[0]:raw[8]})

    except Exception as ex:
        print(str(ex))
    return sse_list
def se_rank_github():
    dict_name_score = {}

    attributes_per_user = []
    rank_list_SE = (())
    all_features = ['code_comment_percentage','code_quality','comment_sentiment','spelling','popularity','useof_popular_technologies']
    code_comment_weight = weights_per_feature[all_features[0]]
    code_quality_weight = weights_per_feature[all_features[1]]
    comment_sentiment_weight = weights_per_feature[all_features[2]]
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = weights_per_feature[all_features[4]]
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('features.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight*float(raw[2])+comment_sentiment_weight*float(raw[3])+spelling_weight*float(raw[4])+popularity_weight*float(raw[5])+useof_popular_technologies_weight*float(raw[6])
                D = code_comment_weight + code_quality_weight+comment_sentiment_weight+spelling_weight+popularity_weight+useof_popular_technologies_weight
                final_score = round(float(N)/float(D),3)
                #print(raw[0]+', '+str(final_score))
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, t[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})

            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1),reverse=True)



            print('Software Engineers: '+str(sorted_list))
            return sorted_list,dict_name_score
    except Exception as ex:
        print(str(ex))


def sse_rank_github():
    dict_name_score = {}
    list_key_value = [[]]
    dictlist = []

    all_features = ['code_comment_percentage','code_quality','comment_sentiment','spelling','popularity','useof_popular_technologies']
    code_comment_weight = weights_per_feature[all_features[0]]
    code_quality_weight = weights_per_feature[all_features[1]]
    comment_sentiment_weight = weights_per_feature[all_features[2]]
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = weights_per_feature[all_features[4]]
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('features_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight*float(raw[2])+comment_sentiment_weight*float(raw[3])+spelling_weight*float(raw[4])+popularity_weight*float(raw[5])+useof_popular_technologies_weight*float(raw[6])
                D = code_comment_weight+code_quality_weight+comment_sentiment_weight+spelling_weight+popularity_weight+useof_popular_technologies_weight
                final_score = round(float(N)/float(D),3)
                #print(raw[0]+', '+str(final_score))
                t = sse_list_github()
               # print t[raw[0]]
                l = [final_score,t[raw[0]]]
                dict_name_score.update({raw[0]:tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1),reverse=True)

            print('\n')
            print('Senior Software Engineers: '+str(sorted_list))
            return sorted_list
    except Exception as ex:
        print('sse_rank_github: '+str(ex))

def se_rank_github_without_sentiment():
    dict_name_score = {}

    attributes_per_user = []
    rank_list_SE = (())
    all_features = ['code_comment_percentage', 'code_quality', 'comment_sentiment', 'spelling', 'popularity',
                    'useof_popular_technologies']
    code_comment_weight = weights_per_feature[all_features[0]]
    code_quality_weight = weights_per_feature[all_features[1]]
    comment_sentiment_weight = 0
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = weights_per_feature[all_features[4]]
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight * float(raw[2]) + comment_sentiment_weight * float(raw[3]) + spelling_weight * float(raw[4]) + popularity_weight * float(raw[5]) + useof_popular_technologies_weight * float(raw[6])
                D = code_comment_weight + code_quality_weight + comment_sentiment_weight + spelling_weight + popularity_weight + useof_popular_technologies_weight
                final_score = round(float(N) / float(D), 3)
                # print(raw[0]+', '+str(final_score))
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, t[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})

            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

            print('Software Engineers rank without sentiment score: ' + str(sorted_list))
            #return dict_name_score
    except Exception as ex:
        print(str(ex))

def se_rank_github_without_codecomment():
    dict_name_score = {}

    attributes_per_user = []
    rank_list_SE = (())
    all_features = ['code_comment_percentage', 'code_quality', 'comment_sentiment', 'spelling', 'popularity',
                    'useof_popular_technologies']
    code_comment_weight = 0
    code_quality_weight = weights_per_feature[all_features[1]]
    comment_sentiment_weight = weights_per_feature[all_features[2]]
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = weights_per_feature[all_features[4]]
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight * float(raw[2]) + comment_sentiment_weight * float(raw[3]) + spelling_weight * float(raw[4]) + popularity_weight * float(raw[5]) + useof_popular_technologies_weight * float(raw[6])
                D = code_comment_weight + code_quality_weight + comment_sentiment_weight + spelling_weight + popularity_weight + useof_popular_technologies_weight
                final_score = round(float(N) / float(D), 3)
                # print(raw[0]+', '+str(final_score))
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, t[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})

            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

            print('Software Engineers rank without sentiment score: ' + str(sorted_list))
            #return dict_name_score
    except Exception as ex:
        print(str(ex))

def se_rank_github_without_codequality():
    dict_name_score = {}

    attributes_per_user = []
    rank_list_SE = (())
    all_features = ['code_comment_percentage', 'code_quality', 'comment_sentiment', 'spelling', 'popularity',
                    'useof_popular_technologies']

    code_comment_weight = weights_per_feature[all_features[0]]
    code_quality_weight = 0
    comment_sentiment_weight = weights_per_feature[all_features[2]]
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = weights_per_feature[all_features[4]]
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight * float(raw[2]) + comment_sentiment_weight * float(raw[3]) + spelling_weight * float(raw[4]) + popularity_weight * float(raw[5]) + useof_popular_technologies_weight * float(raw[6])
                D = code_comment_weight + code_quality_weight + comment_sentiment_weight + spelling_weight + popularity_weight + useof_popular_technologies_weight
                final_score = round(float(N) / float(D), 3)
                # print(raw[0]+', '+str(final_score))
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, t[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})

            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

            print('Software Engineers rank without sentiment score: ' + str(sorted_list))
            #return dict_name_score
    except Exception as ex:
        print(str(ex))

def se_rank_github_without_popularity():
    dict_name_score = {}

    attributes_per_user = []
    rank_list_SE = (())
    all_features = ['code_comment_percentage', 'code_quality', 'comment_sentiment', 'spelling', 'popularity',
                    'useof_popular_technologies']

    code_comment_weight = weights_per_feature[all_features[0]]
    code_quality_weight = weights_per_feature[all_features[1]]
    comment_sentiment_weight = weights_per_feature[all_features[2]]
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = 0
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight * float(raw[2]) + comment_sentiment_weight * float(raw[3]) + spelling_weight * float(raw[4]) + popularity_weight * float(raw[5]) + useof_popular_technologies_weight * float(raw[6])
                D = code_comment_weight + code_quality_weight + comment_sentiment_weight + spelling_weight + popularity_weight + useof_popular_technologies_weight
                final_score = round(float(N) / float(D), 3)
                # print(raw[0]+', '+str(final_score))
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, t[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})

            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

            print('Software Engineers rank without sentiment score: ' + str(sorted_list))
            #return dict_name_score
    except Exception as ex:
        print(str(ex))





se_rank_github()
#sse_rank_github()
#se_rank_github_without_sentiment()
#se_rank_github_without_codecomment()

#se_rank_github_without_codequality()
#sse_rank_github()
#print(se_rank_github())