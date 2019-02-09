import csv
import math

from Github.Github_Api.retrieve_readme import words_list

with open('../../Github_repos_SSE.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for raw in csv_reader:
        fs, tot_words = words_list(raw[2])
        if not tot_words:
            print('Normalized spelling score of '+raw[0]+': 5')
            continue
        incorrect_words = raw[4]
        try:
            answer = (1 - (float(incorrect_words)/float(tot_words)))*10
            print('Normalized spelling score of '+raw[0]+': '+str(round(answer,2)))
        except Exception as e:
            print(raw[0]+': '+str(e))

