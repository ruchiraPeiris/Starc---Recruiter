import csv
import numpy as np
import operator

weights_per_feature = {
'code_comment_percentage': 2,
'code_quality': 2,
'comment_sentiment': 4,
'spelling': 3,
'popularity': 5,
'useof_popular_technologies': 1,
}



def se_list_github():
    se_list = (())
    try:
        with open('Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)

            se_list = np.asarray(list(map(tuple,csv_reader)))
    except Exception as ex:
        print(str(ex))

    filtered_list = list(())

    for item in se_list:
        filtered_list.append((item[0], item[8]))

    return filtered_list

#print(se_list_github())

def sse_list_github():
    sse_list = (())
    try:
        with open('Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)

            sse_list = np.asarray(list(map(tuple,csv_reader)))

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
        with open('../features.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight*float(raw[2])+comment_sentiment_weight*float(raw[3])+spelling_weight*float(raw[4])+popularity_weight*float(raw[5])+useof_popular_technologies_weight*float(raw[6])
                D = code_comment_weight+code_quality_weight+comment_sentiment_weight+spelling_weight+popularity_weight+useof_popular_technologies_weight
                final_score = round(float(N)/float(D),3)
                #print(raw[0]+', '+str(final_score))
                dict_name_score.update({raw[0]:final_score})
            sorted_dict = sorted(dict_name_score.items(), key=operator.itemgetter(1),reverse=True)
            print('Software Engineers: '+str(sorted_dict))

    except Exception as ex:
        print(str(ex))

def sse_rank_github():
    dict_name_score = {}

    all_features = ['code_comment_percentage','code_quality','comment_sentiment','spelling','popularity','useof_popular_technologies']
    code_comment_weight = weights_per_feature[all_features[0]]
    code_quality_weight = weights_per_feature[all_features[1]]
    comment_sentiment_weight = weights_per_feature[all_features[2]]
    spelling_weight = weights_per_feature[all_features[3]]
    popularity_weight = weights_per_feature[all_features[4]]
    useof_popular_technologies_weight = weights_per_feature[all_features[5]]

    try:
        with open('../features_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = code_comment_weight*float(raw[1])+code_quality_weight*float(raw[2])+comment_sentiment_weight*float(raw[3])+spelling_weight*float(raw[4])+popularity_weight*float(raw[5])+useof_popular_technologies_weight*float(raw[6])
                D = code_comment_weight+code_quality_weight+comment_sentiment_weight+spelling_weight+popularity_weight+useof_popular_technologies_weight
                final_score = round(float(N)/float(D),3)
                #print(raw[0]+', '+str(final_score))
                dict_name_score.update({raw[0]:final_score})
            sorted_dict = sorted(dict_name_score.items(), key=operator.itemgetter(1),reverse=True)
            print()
            print('Senior Software Engineers: '+str(sorted_dict))

    except Exception as ex:
        print('sse_rank_github: '+str(ex))


se_rank_github()
sse_rank_github()
#print(se_rank_github())