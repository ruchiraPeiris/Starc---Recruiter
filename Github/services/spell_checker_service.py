import csv

from Github.Github_Api.retrieve_readme import words_list

with open('../../Github_repos.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for raw in csv_reader:
        fs, tot_words = words_list(raw[2])
        incorrect_words = raw[4]
        try:
            print 'Normalized spelling score of(correctness per word) '+raw[0]+': '+str(1 - float(incorrect_words)/float(tot_words))
        except Exception, e:
            print raw[0]+': '+str(e)

