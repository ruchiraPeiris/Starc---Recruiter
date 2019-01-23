from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.retrieve_commits import commit_list
import csv



with open('../../Github_repos.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for user in csv_reader:
        list = []
        list = commit_list(user[1],user[2],user[3])
        score = 0
        for commit in list:
            if len(list) >= 5:
                score += calEmotionalLevel(commit.lower())
        try:
            test = float(score)/float(len(list))
        except:
            print 'no commits in the repository'
        print 'Score of ' + user[0] + ": " + str(test)



