from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.retrieve_commits import commit_list
import csv



with open('../../Github_repos.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for user in csv_reader:
        list = []
        list = commit_list(user[0],user[1],user[2])
        score = 0
        for commit in list:
            if len(list) >= 5:
                score += calEmotionalLevel(commit.lower())
        test = float(score)/float(len(list))
        print 'Score of ' + user[1] + ": " + str(test)



