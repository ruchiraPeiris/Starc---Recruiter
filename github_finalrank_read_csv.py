from github_final_ranking import se_list_github, sse_list_github
import csv
import operator

se_list = se_list_github()
sse_list = sse_list_github()

def se_sorted_list():
    dict_name_score = {}
    try:
        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                l = [raw[7],se_list[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

            print('Software Engineers: ' + str(sorted_list))
            return sorted_list
    except Exception as ex:
        print('Error occured: '+str(ex))

def sse_sorted_list():
    dict_name_score = {}
    try:
        with open('features_SSE.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:
                l = [raw[7],sse_list[raw[0]]]
                dict_name_score.update({raw[0]: tuple(l)})
            sorted_list = sorted(dict_name_score.items(), key=operator.itemgetter(1), reverse=True)

            print('Senior Software Engineers: ' + str(sorted_list))
            return sorted_list
    except Exception as ex:
        print('Error occured: '+str(ex))

