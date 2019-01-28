import requests
import json
import csv



def count(repo,email,userName):

    comm_result = requests.get('https://api.github.com/repos/'+userName+'/'+repo+'/commits?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')
    comm_data = json.loads(comm_result.content)
    count = 0
    try:
        for value in comm_data:
            if value['commit']['author']['email'] == email:
                count+=1
    except Exception, e:
        print 'error occurred while finding user commits: '+str(e)
    return count

def findmax(email,userName):
    request_url = "https://api.github.com/users/" + userName + "/repos?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34"

    result = requests.get(request_url)
    repo_data = json.loads(result.content)
    max_repo = ' '
    max_commits = 0
    for item in repo_data:
        test = item['name']
        count2 = count(test,email,userName)
        if count2 > max_commits:
            max_commits = count2
            max_repo = item['name']
    print 'Maximum number of commits: '+max_commits.__str__()


    return max_repo

with open('../../Github_repos.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for raw in csv_reader:
        print 'Repository which has maximum commits for '+raw[0]+': ' + findmax(raw[1], raw[2])+'\n'


# print 'Repository which has maximum commits: '+findmax('jdeen-solutions@outlook.com','ziyan-junaideen')