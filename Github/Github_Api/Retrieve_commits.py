import requests
import json



# send api request
response = requests.get('https://api.github.com/repos/ruchirapeiris/ontology/commits')

print response.headers['content-type']
# load response as a json object
data = json.loads(response.content)
 #decode data using base64
# decoded_content = base64.b64decode(data["commit"])

def commitList(user):
    commList= []
    for x in data:
        if x['commit']['author']['email'] == user:
            commList.append(x['commit']['message'])

    return commList

