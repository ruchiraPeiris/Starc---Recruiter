import csv
from math import *
from sklearn.metrics import jaccard_similarity_score

from Stackoverflow.FeatureExtraction import tec_skills as sa


def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)


# t1=['revision','language','source','nothing','character','would','keyword','change','final','however']
# t2=['return','regex','output','delta','think','update','string','every','server']
# t3=['small','query','title','candidate','ballot','small_re','words','first','database','single']
# t4=['rewrite','really','anything','request','lt;/rule&gt','lt;action','lt;match','type="redirect']
# t=['java','c#','administrator','communication']
# print(jaccard_similarity(t1,t2))
# print(jaccard_similarity_score(t1,t2))

file_path_for_answer_posts='D:/Desktop data/FYP/data/User_Data.csv'
column_name_for_user_id='Id'


# rows = sa.get_user_years_stovfl(file_path_for_answer_posts,column_name_for_user_id)
#
# for row in rows:
#      print(row[0])
# with open('C:D:/Desktop data/FYP/User_Data.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     for row in rows:
#         writer.writerow(row)
#
# csvFile.close()
#
# with open('C:/Users/pc/Desktop/FYP/User_Data.csv', 'r') as csvFile:
#      reader = csv.reader(csvFile)
#      for row in reader:
#          print(row)
#
# csvFile.close()
