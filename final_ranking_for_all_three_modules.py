import operator
import csv

from final_ranking import get_features, get_features_github
from github_final_ranking import se_list_github, sse_list_github
se_list = []
sse_list = []

se_list = se_list_github()
sse_list = sse_list_github()


# get overall ranking for SE
def final_rank_SE(list):
    max = int(len(get_features())) + 1
    dict_name_score = {}
    sorted_list = []
    print(max)
    try:
        with open('for_correlation_se.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = 0
                D = 0
                for x in range(1,15):
                    N = N + (max - int(list[x-1]))*float(raw[x])
                    D = D + (max - int(list[x-1]))
                final_score = float(N)/float(D)
                # print(final_score)
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, t[str(raw[0]).capitalize()]]
                dict_name_score.update({raw[0]: tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

           # print('Software Engineers: ' + str(sorted_list))
            #return sorted_list
    except Exception as ex:
        print('Error occured: ' + str(ex))
    return sorted_list

# get overall ranking for SSE
def final_rank_SSE(list):
    max = int(len(get_features())) + 1
    dict_name_score = {}
    sorted_list = []

    try:
        with open('for_correlation_sse.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = 0
                D = 0
                for x in range(1, 15):
                    N = N + (max - int(list[x-1])) * float(raw[x])
                    D = D + (max - int(list[x-1]))
                final_score = float(N) / float(D)
                t = sse_list_github()
                # print t[raw[0]]
                l = [final_score, str(t[raw[0]]).upper()]
                dict_name_score.update({raw[0]: tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

        # print('Software Engineers: ' + str(sorted_list))
        # return sorted_list
    except Exception as ex:
        print('Error occured: ' + str(ex))
    return sorted_list



def github_rank_SE(list):
    max = int(len(get_features_github()))
    dict_name_score = {}
    sorted_list = []
    print(max)
    try:
        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = 0
                D = 0
                for x in range(1, 6):
                    N = N + (max - int(list[x - 1])) * float(raw[x])
                    D = D + (max - int(list[x - 1]))
                final_score = float(N) / float(D)
                t = se_list_github()
                # print t[raw[0]]
                l = [final_score, str(t[raw[0]]).upper()]
                dict_name_score.update({raw[0]: tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

        # print('Software Engineers: ' + str(sorted_list))
        # return sorted_list
    except Exception as ex:
        print('Error occured: ' + str(ex))
    return sorted_list

def github_rank_SSE(list):
    max = int(len(get_features_github())) + 1
    dict_name_score = {}
    sorted_list = []

    try:
        with open('features_SSE.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                N = 0
                D = 0
                for x in range(1, 7):
                    N = N + (max - int(list[x - 1])) * float(raw[x])
                    D = D + (max - int(list[x - 1]))
                final_score = float(N) / float(D)
                t = sse_list_github()
                # print t[raw[0]]
                l = [final_score, str(t[raw[0]]).upper()]
                dict_name_score.update({raw[0]: tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

        # print('Software Engineers: ' + str(sorted_list))
        # return sorted_list
    except Exception as ex:
        print('Error occured: ' + str(ex))
    return sorted_list