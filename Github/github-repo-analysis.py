import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from ggplot import *
plt.style.use('default')

git_df = pd.read_csv("TopStaredRepositories.csv", parse_dates=['Last Update Date'], dayfirst=True)
git_df.head()

git_df.info()

git_df_max = git_df['Number of Stars'].str.contains('k').all()
print(git_df_max)

git_df['Number of Stars']=git_df['Number of Stars'].str.replace('k','').astype(float)
print(git_df.head())

print(git_df['Number of Stars'].describe())

classified_repos=[]
for i in range(8,300,7):
    x = git_df[(git_df['Number of Stars'] >= i) & (git_df['Number of Stars'] <(i+7.0))]
    classified_repos.append(len(x))

indexes = []

for i in range (8000,300000, 7000):
    x = '[' + str(i) +','+ (str(i+7000)) + ')'
    indexes.append(x)

divided_repos = pd.Series(data=classified_repos, index=indexes)
#divided_repos.plot(kind='bar', figsize=(15,10), color=['red'],legend=True, label='Number of repositories')

x=git_df['Language'].value_counts()
print(x)


plt.figure()
x.plot(kind='barh',figsize=(15,10),grid=True, label='Number of repositories',legend='No of repos',title='No of repositories vs language used')
plt.show()


x[:20].plot.pie(label="Division of the top 20 languages",fontsize=10,figsize=(10,10),legend=True)

plt.show()