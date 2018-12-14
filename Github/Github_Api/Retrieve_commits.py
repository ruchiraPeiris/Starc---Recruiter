import requests
import json
import base64


# send api request
response = requests.get('https://api.github.com/repos/ruchirapeiris/ontology/commits')

print response.headers['content-type']
# load response as a json object
data = json.loads(response.content)
 #decode data using base64
# decoded_content = base64.b64decode(data["commit"])

print data[7]['commit']['message']

for x in data:
    print x['commit']['message']
