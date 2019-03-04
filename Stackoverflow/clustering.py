import pandas as pd
import matplotlib.pyplot as plt
users = pd.read_csv('D:/Desktop data/FYP/user_data_all_new.csv')
print(users)
print(users.shape)
print(users.groupby('job').size())

import seaborn as sns
sns.countplot(users['job'],label="Count")
# plt.show()

users.drop('UserId', axis=1).plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, figsize=(9,9),
                                        title='Box Plot for each input variable')
plt.savefig('users_box')
# plt.show()

import pylab as pl
users.drop('UserId' ,axis=1).hist(bins=30, figsize=(9,9))
pl.suptitle("Histogram for each numeric input variable")
plt.savefig('users_hist')
# plt.show()

job_mapping={'SE':0,'SSE':1}
users['job']=users['job'].map(job_mapping)

print(users)
from pandas.plotting import scatter_matrix
from matplotlib import cm
feature_names = ['reputation','experience','upvotes','downvotes']
X = users[feature_names]
y = users['job']



# pd.scatter_matrix(users, alpha=0.2, figsize=(10, 10))
# # plt.show()
# # cmap = cm.get_cmap('gnuplot')
# # scatter = scatter_matrix(X, c = y, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap = cmap)
#
# plt.suptitle('Scatter-matrix for each input variable')
# plt.savefig('fruits_scatter_matrix')
#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)
#
# from sklearn.linear_model import LogisticRegression
# logreg = LogisticRegression()
# logreg.fit(X_train, y_train)
# print('Accuracy of Logistic regression classifier on training set: {:.2f}'
#      .format(logreg.score(X_train, y_train)))
# print('Accuracy of Logistic regression classifier on test set: {:.2f}'
#      .format(logreg.score(X_test, y_test)))
#
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier()
# knn.fit(X_train, y_train)
# print('Accuracy of K-NN classifier on training set: {:.2f}'
#      .format(knn.score(X_train, y_train)))
# print('Accuracy of K-NN classifier on test set: {:.2f}'
#      .format(knn.score(X_test, y_test)))
#
# from sklearn.svm import SVC
# svm = SVC()
# svm.fit(X_train, y_train)
# print('Accuracy of SVM classifier on training set: {:.2f}'
#      .format(svm.score(X_train, y_train)))
# print('Accuracy of SVM classifier on test set: {:.2f}'
#      .format(svm.score(X_test, y_test)))
#
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# pred = svm.predict(X_test)
# print(confusion_matrix(y_test, pred))
# print(classification_report(y_test, pred))