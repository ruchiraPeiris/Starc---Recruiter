from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.Retrieve_commits import commitList

users = ["ruchirapeiris7@gmail.com","madushajg@gmail.com"]
score =0;

for user in users:
    list = []
    list = commitList(user)
    for commit in list:
        score+=calEmotionalLevel(commit.lower())


print score