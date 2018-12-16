import requests
import json


users = ['ruchirapeiris']

request_url = "https://api.github.com/users/"+users[0]+"/repos"

result = requests.get(request_url)
repo_data = json.loads(result.content)
max_commits = 0

def count(repo):

    comm_result = requests.get('https://api.github.com/repos/'+users[0]+'/'+repo+'/commits')
    comm_data = json.loads(comm_result.content)
    count = 0
    for value in comm_data:
        if value['commit']['author']['email'] == 'ruchirapeiris7@gmail.com':
            count+=1

    return count

def findmax():

    max_commits = 0
    for item in repo_data:
        count2 = count(item['name'])
        if count2 > max_commits:
            max_commits = count2
            max_repo = item['name']



    return max_repo

print findmax()