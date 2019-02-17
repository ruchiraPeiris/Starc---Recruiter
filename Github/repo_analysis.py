import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from ggplot import *
plt.style.use('default')

git_df = pd.read_csv("../input/TopStaredRepositories.csv", parse_dates=['Last Update Date'], dayfirst=True)
print(git_df.head())

print(git_df.info())


git_df_max = git_df['Number of Stars'].str.contains('k').all()
print(git_df_max)

git_df['Number of Stars']=git_df['Number of Stars'].str.replace('k','').astype(float)
print(git_df.head())

print(git_df.tail())
git_df['Number of Stars'].describe()

popular_repos= git_df[git_df['Number of Stars'] > 13.0]
len(popular_repos)

popular_repos.head(8)
popular_repos.tail(8)

classified_repos=[]
for i in range(8,300,7):
    x = git_df[(git_df['Number of Stars'] >= i) & (git_df['Number of Stars'] <(i+7.0))]
    classified_repos.append(len(x))

indexes = []

for i in range (8000,300000, 7000):
    x = '[' + str(i) +','+ (str(i+7000)) + ')'
    indexes.append(x)
divided_repos = pd.Series(data=classified_repos, index=indexes)
divided_repos.plot(kind='bar', figsize=(15,10), color=['red'],legend=True, label='Number of repositories')


