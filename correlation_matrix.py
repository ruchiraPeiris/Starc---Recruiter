from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
X_train = pd.DataFrame.from_csv('test.csv')

corr_df=X_train.corr()
f, ax = plt.subplots(figsize=(12, 15))
hm = sns.heatmap(corr_df, annot=True, ax=ax, cmap="coolwarm",fmt='.2f',linewidths=.6)
f.subplots_adjust(right=1.00)
f.subplots_adjust(left=0.80)
f.subplots_adjust(top=0.94)
f.subplots_adjust(bottom=0.40)
t= f.suptitle('Github features correlation', fontsize=12)
plt.show()