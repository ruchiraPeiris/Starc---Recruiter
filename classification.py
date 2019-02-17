import pandas as pd
import numpy as np

try:
  df = pd.read_csv('test.csv')
except Exception as ex:
     print('Error occurred: '+str(ex))


# print(df['UserId'].describe())

# 'reputation', 'experience', 'upvotes', 'downvotes', 'avg_word_count_answer_posts', 'avg_word_count_question_posts', 'avg_setence_count_answer_posts', 'avg_setence_count_question_posts', 'avg_word_count_comments', 'avg_setence_count_comments', 'code_count_in_answer_posts', 'releventness_to_jobadd', 'question_posts_similarity', 'answer_posts_similarity', 'avg_comment_count_answer_posts', 'avg_answer_count_answer_posts', 'avg_viewcount_count_question_posts'

#df=df.fillna(df.min())


# df=df[df.reputation != 1]
# a=df.dropna(how='all')
# print(a['avg_word_count_comments'])
# print('===============================')

# b=df.fillna(df.mean())
# print(b['avg_word_count_comments'])
# c=pd.get_dummies(df.tags)
# b=df.drop('name',axis=1)
# b=b.drop('tags',axis=1)
# b=b.drop('downvotes',axis=1)
# b=b.drop('question_posts_similarity',axis=1)
# b=b.drop('avg_word_count_comments',axis=1)
# b=b.drop('downvotes',axis=1)
# b=b.drop('releventness_to_jobadd',axis=1)
# b=b.drop('question_posts_similarity',axis=1)
# s=pd.concat([b,c],axis=1)

print('=================================================================================================================')
# print('==============',s.columns)

import pandas as pd
import matplotlib.pyplot as plt
users = df
# print(users)
# print(users.shape)
# print(users.groupby('job').size())

import seaborn as sns
sns.countplot(users['job'],label="Count")
# plt.show()

# users.drop('UserId', axis=1).plot(kind='box', subplots=False, layout=(10,10), sharex=False, sharey=True, figsize=(9,9),title='Box Plot for each input variable')
# plt.savefig('users_box')
# plt.show()

import pylab as pl
# users.drop('UserId' ,axis=1).hist(bins=50, figsize=(15,15))
# pl.suptitle("Histogram for each numeric input variable")
# plt.savefig('users_hist')
# plt.show()

print()

job_mapping={'SE':0,'SSE':1}
users['job']=users['job'].map(job_mapping)

# print(users)
from pandas.plotting import scatter_matrix
from matplotlib import cm
feature_names = list(df.columns.values)
feature_names.remove('job')
print(feature_names)
# print('feature_names==============',feature_names)
X = users[feature_names]
y = users['job']


X_train=users[feature_names]
X_test=users[feature_names]
y_train = users['job']
y_test  = users['job']

# pd.scatter_matrix(users, alpha=0.2, figsize=(10, 10))
# plt.show()
# cmap = cm.get_cmap('gnuplot')
# scatter = scatter_matrix(X, c = y, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap = cmap)

# plt.suptitle('Scatter-matrix for each input variable')
# plt.savefig('fruits_scatter_matrix')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
from sklearn.preprocessing import MinMaxScaler
# scaler1 = Normalizer().fit(X)
# scaler2=StandardScaler().fit(X)
scaler = MinMaxScaler(copy=True, feature_range=(0, 1)).fit(X)




# X_train = scaler.fit_transform(X_train)
# # X_train = scaler2.fit_transform(X_train)
# X_test = scaler.fit_transform(X_test)
# # X_test = scaler2.fit_transform(X_test)

# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r

corr_df=df.corr()
f, ax = plt.subplots(figsize=(12, 15))
hm = sns.heatmap(corr_df, annot=True, ax=ax, cmap="coolwarm",fmt='.2f',linewidths=.6)
f.subplots_adjust(right=1.00)
# f.subplots_adjust(left=0.20)
# f.subplots_adjust(top=0.94)
# f.subplots_adjust(bottom=0.40)
t= f.suptitle('Github Attributes Correlation Heatmap', fontsize=12)
#plt.show()


# LogisticRegression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(logreg.score(X_test, y_test)))
predlr=logreg.predict(X_test)
print(confusion_matrix(y_test, predlr))
print(classification_report(y_test, predlr))


# KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))
predknn=knn.predict(X_test)
print(confusion_matrix(y_test, predknn))
print(classification_report(y_test, predknn))




# SVC
from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))
predsvm=svm.predict(X_test)
print(confusion_matrix(y_test, predsvm))
print(classification_report(y_test, predsvm))



# DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_train, y_train)
print('Accuracy of DecisionTree classifier on training set: {:.2f}'
     .format(dt.score(X_train, y_train)))
print('Accuracy of DecisionTree classifier on test set: {:.2f}'
     .format(dt.score(X_test, y_test)))
preddt=dt.predict(X_test)
print(confusion_matrix(y_test, preddt))
print(classification_report(y_test, preddt))






