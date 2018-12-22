import requests
import json

from Github.Github_Api.commit_count import findmax

max_commit_repo = findmax()
# send api request
response = requests.get('https://api.github.com/repos/milankarunarathne/'+max_commit_repo+'/commits?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')

print response.headers['content-type']
# load response as a json object
data = json.loads(response.content)
# decode data using base64
# decoded_content = base64.b64decode(data["commit"])

def commitList(user):
    commList = []
    for x in data:
        if x['commit']['author']['email'] == user:
            commList.append(x['commit']['message'])
    print commList
    return commList

