import csv
import pandas as pd
from datetime import date, datetime

from Stackoverflow.FeatureExtraction import tec_skills as sa
from Stackoverflow.nlp import SentimentAnalysisImpl as sai


# listone=['asds',12,'hello']
#
# if 13 in listone:
#     print('hello is there')
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP/data/post_answers_u100.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# sai.get_include_code_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,text_column_name)



# file_path_for_answer_posts='D:/Desktop data/FYP/data/users_latest.csv'
# column_name_for_user_id='Id'
#
#
# rows = sa.get_user_years_stovfl(file_path_for_answer_posts,column_name_for_user_id)
#
# for row in rows:
#     print(row[0])
# with open('D:/Desktop data/FYP/users_latest_dataset.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     for row in rows:
#         writer.writerow(row)
#
# csvFile.close()

# with open('D:/Desktop data/FYP/users_latest_dataset.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         print(row)
#
# csvFile.close()




def cluster_data(tag_value,data):
    df = pd.read_csv('D:/Desktop data/FYP/users_latest.csv')
    df = df.sort_values('UserId')
    val = list(df.columns.values)
    val.append(tag_value)
    print(val)
    user_data = []
    user_data.append(val)
    for index, row in df.iterrows():
        user = list(row)
        print(user)
        for d in data:
            if d[0] == row['UserId']:
                user.append(d[1])

        user_data.append(user)
    for w in user_data:
        print(w)
    with open('D:/Desktop data/FYP/users_latest.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in user_data:
            writer.writerow(row)
    csvFile.close()


def get_tag_data(tags):
    df = pd.read_csv('D:/Desktop data/FYP/users_latest.csv')
    df = df.sort_values('UserId')
    val = list(df.columns.values)
    val.append('tags')
    print(val)
    user_data = []
    user_data.append(val)
    for index, row in df.iterrows():
        user = list(row)
        print(user)
        for tag in tags:
            if tag[0] == row['UserId']:
                user.append(tag[1])

        user_data.append(user)
    # for w in user_data:
    #     print(w)
    with open('D:/Desktop data/FYP/users_latest.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        count = 0
        for row in user_data:
            count += 1
            writer.writerow(row)
        # print('count  =  > ', count)
    csvFile.close()



