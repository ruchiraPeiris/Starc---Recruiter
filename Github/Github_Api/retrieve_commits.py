import json
import requests
import csv



def commit_list(email, user_name, max_commit_repo):


    # send api request
    response = requests.get(
        'https://api.github.com/repos/'+user_name+'/'+ max_commit_repo + '/commits?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')

    # load response as a json object
    data = json.loads(response.content)
    comm_list = []
    for x in data:
        try:
            if x['commit']['author']['email'] == email:
                comm_list.append(x['commit']['message'])
        except:
            continue

    return comm_list





def load_users():
    x =0
    paragraph = ''
    try:
        with open('../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                list2 = []
                list2 = commit_list(raw[1], raw[2], raw[3])

                for x in range(0,5):
                    paragraph+=' '+list2[x]


                print(raw[0]+': '+paragraph)
    except Exception as ex:
        print('Error: '+str(ex))


#load_users()
#print commit_list('nsaumini@gmail.com','nsaumini','nova-field-count')