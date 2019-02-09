import requests
import json
import csv


def get_followers_per_user(user_name):


    try:
        # send api request
        response = requests.get(
            'https://api.github.com/users/' + user_name + '/followers?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')

        # load response as a json object
        data = json.loads(response.content)


        count = len(data)
        # print count
    except Exception as ex:
        print(ex)
    return count


def get_max_follwers():
    max_followers = 0
    try:
        with open('../../Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                if raw:
                    #print raw[0]
                    x = get_followers_per_user(raw[2])
                    if x > max_followers:
                        max_followers = x
                else: break

    except Exception as e:
            print('Error occurred: ' + str(e))
    return max_followers

def avg_score():
    min_val = 0
    dict_follow_count = {}
    try:
        with open('../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            max = get_max_follwers()
            #print max

            for user in csv_reader:
                if user:
                    #print user[0]
                    followers = get_followers_per_user(user[2])
                    #result = (float(followers) / float(max)) * 10
                    dict_follow_count.update({user[0]:followers})
                    print('followers of'+user[0]+': '+str(followers))
                else:
                    break
            normalize(dict_follow_count)
        #print dict_follow_count
        for key, val in sorted(iter(dict_follow_count.items()), key=lambda k_v: (k_v[1],k_v[0])):
                if val>0:
                    min_val = val
                    break
        print('min value: ' + str(min_val))
    except Exception as e:
            print('Error occurred: ' + str(e))


def normalize(dict_name_score):

    #print(dict_name_score)

    maximum = max(dict_name_score, key=dict_name_score.get)
    minimum = min(dict_name_score, key=dict_name_score.get)

    print(maximum + ',' + str(dict_name_score[maximum]))
    print(minimum + ',' + str(dict_name_score[minimum]))
    print('////////////////////////////////////')
    print('Normalized scores')
    for key,val in dict_name_score.items():
        final_score = 1 + float((val - dict_name_score[minimum])*9)/float(dict_name_score[maximum]-dict_name_score[minimum])
        print(key+', '+str(round(final_score,3)))


avg_score()