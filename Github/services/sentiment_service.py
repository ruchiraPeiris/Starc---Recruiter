from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.Retrieve_commits import commitList

users = ['mhkarunarathne@gmail.com']


for user in users:
    list = []
    list = commitList(user)
    score = 0
    for commit in list:
        score+=calEmotionalLevel(commit.lower())
    print 'Score of '+user+": "+score.__str__()


