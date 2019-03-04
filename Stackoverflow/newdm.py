import pandas as pd
import numpy as np
df = pd.read_csv('D:/Desktop data/FYP/for_correlation_se_dummy.csv')
import pandas as pd
import matplotlib.pyplot as plt
users = df

import seaborn as sns
# sns.countplot(users['position'],label="Count")
# plt.show()

# users.drop('UserId', axis=1).plot(kind='box', subplots=False, layout=(10,10), sharex=False, sharey=True, figsize=(9,9),title='Box Plot for each input variable')
# plt.savefig('users_box')
# plt.show()

import pylab as pl
# users.drop('UserId' ,axis=1).hist(bins=50, figsize=(15,15))
# pl.suptitle("Histogram for each numeric input variable")
# plt.savefig('users_hist')
# plt.show()

job_mapping={'SE':0,'SSE':1}
users['position']=users['position'].map(job_mapping)

# print(users)
from pandas.plotting import scatter_matrix
from matplotlib import cm
feature_names = list(df.columns.values)
feature_names.remove('position')
# print('feature_names==============',feature_names)
X = users[feature_names]
y = users['position']


X_train=users[feature_names]
X_test=users[feature_names]
y_train = users['position']
y_test  = users['position']

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(copy=True, feature_range=(0, 1)).fit(X)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(logreg.score(X_test, y_test)))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))
pred1=knn.predict(X_test)
print(confusion_matrix(y_test, pred1))

from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_train, y_train)
print('Accuracy of DecisionTree classifier on training set: {:.2f}'
     .format(dt.score(X_train, y_train)))
print('Accuracy of DecisionTree classifier on test set: {:.2f}'
     .format(dt.score(X_test, y_test)))
pred3=dt.predict(X_test)
print(confusion_matrix(y_test, pred3))

pred = svm.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
