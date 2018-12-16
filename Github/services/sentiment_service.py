from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.Retrieve_commits import commitList

users = ["mohomedarshad1@gmail.com","ruchirapeiris7@gmail.com"]


for user in users:
    list = []
    list = commitList(user)
    for commit in list:
        score = 0
        score+=calEmotionalLevel(commit.lower())
    print user+": "+score.__str__()


