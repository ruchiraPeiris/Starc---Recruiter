from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.Retrieve_commits import commitList
import csv



with open('../../Github_repos.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for user in csv_reader:
        list = []
        list = commitList(user[0],user[1],user[2])
        score = 0
        for commit in list:
            score += calEmotionalLevel(commit.lower())
        print 'Score of ' + user[1] + ": " + score.__str__()



