import requests
import csv
import json
import base64
import nltk
from nltk.tokenize import word_tokenize

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def words_list(userName):

    repo_name = ''
    with open('../../Github_repos.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for raw in csv_reader:
            if raw[2] == userName:
                repo_name = raw[3]
                print repo_name
    response = requests.get('https://api.github.com/repos/'+userName+'/'+repo_name+'/readme')
    data = json.loads(response.content)
    decoded_content = base64.b64decode(data["content"])
    words = decoded_content.decode('utf-8')
    word_tokens = word_tokenize(words)

    filtered_sentence = []
    for w in word_tokens:

        filtered_sentence.append(remove_punctuations(w))


    return filtered_sentence


def remove_punctuations(str):
    no_punct = ""
    for char in str:
        if char not in punctuations:
            no_punct = no_punct + char

    return no_punct