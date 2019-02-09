from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.retrieve_commits import commit_list
import csv
from collections import OrderedDict
import operator





def individual_score():
    dict_normalized_score = OrderedDict()
    with open('../../Github_repos.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for user2 in csv_reader:

            try:
                list2 = []
                list2 = commit_list(user2[1], user2[2], user2[3])
                statement = ''
                score = 0
                for commit2 in list2:
                    statement += commit2
                #if len(list2) >= 5:
                score = calEmotionalLevel(statement)
                dict_normalized_score.update({user2[0]: score})

                #print('Value of ' + user2[0] + ' : ' + str(score))
            except Exception as ex:
                print(ex)


    normalize(dict_normalized_score)



def normalize(dict_name_score):

    #print(dict_name_score)

    maximum = max(dict_name_score, key=dict_name_score.get)
    minimum = min(dict_name_score, key=dict_name_score.get)

    print(maximum + ',' + str(dict_name_score[maximum]))
    print(minimum + ',' + str(dict_name_score[minimum]))
    print('////////////////////////////////////')
    print('Normalized Scores')
    for key,val in dict_name_score.items():
        final_score = 1 + float((val - dict_name_score[minimum])*9)/float(dict_name_score[maximum]-dict_name_score[minimum])
        print(key+', '+str(round(final_score,3)))



individual_score()