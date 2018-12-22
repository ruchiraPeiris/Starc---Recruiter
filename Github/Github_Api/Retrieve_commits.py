import requests
import json


def commitList(email, userName,max_commit_repo):
    # send api request
    response = requests.get(
        'https://api.github.com/repos/'+userName+'/'+ max_commit_repo + '/commits?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')

    # load response as a json object
    data = json.loads(response.content)
    commList = []
    for x in data:
        if x['commit']['author']['email'] == email:
            commList.append(x['commit']['message'])

    return commList

