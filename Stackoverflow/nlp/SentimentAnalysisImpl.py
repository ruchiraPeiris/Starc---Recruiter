import csv
import pandas as pd

from Stackoverflow import SentimentAnalysis as sa
from Stackoverflow import test1 as test1
from Stackoverflow.FeatureExtraction import tec_skills as sk


# =======================================================================================================================


def cluster_data(tag_value, data):
    df = pd.read_csv('C:/Users/pc/Desktop/FYP data/test_results/se_results_new.csv')
    df = df.sort_values('UserId')
    df=df.drop(tag_value, axis=1)
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
    with open('C:/Users/pc/Desktop/FYP data/test_results/se_results_new.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in user_data:
            writer.writerow(row)
    csvFile.close()


# ============================ common method for counting average word counts post,comments user wise =====================================

def get_avg_word_count_user_wise(file_path, column_name_for_user_id, count_type, text_column_name):
    df = pd.read_csv(file_path)

    df = df.sort_values(column_name_for_user_id)

    user_data = []
    user_data.append(['UserId', 'count'])
    word_count = 0
    count = 0
    df_line = 0

    for index, row in df.iterrows():

        text = sa.remove_stopwords(sa.remove_tags(row[text_column_name]))
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]

            if previous_user == '' or previous_user == current_user:
                count += 1
                df_line += 1
                word_count += sa.word_count(text)

            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                average_word_count = word_count / count
                word_count = 0
                word_count += sa.word_count(text)
                user_data.append([previous_user, average_word_count])
                print('user = ', previous_user, ' => count type = ', count_type, ' => count  = ', average_word_count)
                count = 1
                df_line += 1

            previous_user = current_user

    return user_data


# =================== Answer post Average word counts user wise ==================================================================================



# print('=================== Answer post counts user wise ==================================================================================')
# file_path_for_answer_posts='D:/Desktop data/FYP/data/uer_answer_posts_latest.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# data=get_avg_word_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# cluster_data('avg_word_count_posts',data)
# print('**********************************   END   *******************************************')

# print('=================== Answer post counts user wise ==================================================================================')
# file_path_for_answer_posts='D:/Desktop data/FYP/data/Comments.csv'
# column_name_for_user_id='UserId'
# count_type='comments'
# text_column_name='Text'
# data=get_avg_word_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
#
# cluster_data('avg_word_count_comments',data)

# ============================ common method for counting average sentences counts post,comments user wise =====================================

def get_avg_sentences_count_user_wise(file_path, column_name_for_user_id, count_type, text_column_name):
    df = pd.read_csv(file_path)

    df = df.sort_values(column_name_for_user_id)

    user_data = []
    user_data.append(['UserId', 'count'])
    sentence_count = 0
    count = 0
    df_line = 0

    for index, row in df.iterrows():

        text = sa.remove_stopwords(sa.remove_tags(row[text_column_name]))
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]

            if previous_user == '' or previous_user == current_user:
                count += 1
                df_line += 1
                sentence_count += sa.sentence_count(text)

            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                average_sentence_count = sentence_count / count
                sentence_count = 0
                sentence_count += sa.sentence_count(text)
                user_data.append([previous_user, average_sentence_count])
                print('user = ', previous_user, ' => count type = ', count_type, ' => count  = ',
                      average_sentence_count)
                count = 1
                df_line += 1

            previous_user = current_user

    print(len(df.index))
    print(user_data)
    return user_data


# =================== Answer post Average sentence counts user wise ====================================================
# print('=================== Answer post counts user wise ==================================================================================')
# file_path_for_answer_posts='D:/Desktop data/FYP/data/Comments.csv'
# column_name_for_user_id='UserId'
# count_type='answer_posts'
# text_column_name='Text'
# data2=get_avg_sentences_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
#
# cluster_data('avg_setence_count_comments',data2)


# ============================ method for counting code counts answer posts user wise ==================================

def get_include_code_count_user_wise(file_path, column_name_for_user_id, text_column_name):
    df = pd.read_csv(file_path)
    df = df.sort_values(column_name_for_user_id)
    user_data = []
    user_data.append(['UserId', 'count'])
    code_count = 0
    df_line = 0

    for index, row in df.iterrows():
        text = row[text_column_name]
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]
            if previous_user == '' or previous_user == current_user:
                if '<code>' in text:
                    code_count += 1
                    print('line => ', df_line, 'text =>  ', text)
                df_line += 1
            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):

                user_data.append([previous_user, code_count])
                print('user = ', previous_user, ' => code count  = ', code_count)
                if '<code>' in text:
                    code_count += 1
                    print('line => ', df_line, 'text =>  ', text)
                else:
                    code_count = 0
                df_line += 1
            previous_user = current_user
    return user_data


# ======================================================================================================================

# file_path_for_answer_posts='D:/Desktop data/FYP/data/post_answers_u100.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# data4=get_include_code_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,text_column_name)
#
# cluster_data('code_count_posts',data4)

# ======================================================================================================================
import numpy as np
from sklearn.metrics import jaccard_similarity_score
from Stackoverflow import test2 as t2


def post_similarity(file_path, column_name_for_user_id):
    df_posts = pd.read_csv(file_path)
    user_df = pd.read_csv('D:/Desktop data/FYP/users_latest.csv')
    user_df = user_df.sort_values('UserId')
    user_data = []
    user_data.append(['UserId', 'post_similarity'])
    for index, row in user_df.iterrows():
        df = df_posts.loc[df_posts['OwnerUserId'] == row['UserId']]
        df = df.sort_values('Id')
        count = 0
        score = 0
        for index1, row1 in df.iterrows():

            for index2, row2 in df.iterrows():
                if row1['Id'] < row2['Id']:
                    text1 = sa.word_tokenize(sa.remove_stopwords(sa.remove_tags(row1['Body'])))
                    text2 = sa.word_tokenize(sa.remove_stopwords(sa.remove_tags(row2['Body'])))
                    score += t2.jaccard_similarity(text1, text2)
                    count += 1
                if count==10000:
                     break
            if count == 10000:
                break
        if count == 0:
            user_data.append([row['UserId'], count])
        else:
            user_data.append([row['UserId'], score / count])
    return user_data


# file_path_for_answer_posts = 'D:/Desktop data/FYP/data/user_question_posts_latest.csv'
# column_name_for_user_id = 'OwnerUserId'
# post_similarity(file_path_for_answer_posts, column_name_for_user_id)


# ============================ common method for counting average counts post,comments user wise =======================

def get_avg_score_user_wise(file_path, column_name_for_user_id, count_type,column_name):
    df = pd.read_csv(file_path)

    df = df.sort_values(column_name_for_user_id)

    user_data = []
    user_data.append(['UserId', 'score'])
    tatal_score = 0
    count = 0
    df_line = 0

    for index, row in df.iterrows():

        score = row[column_name]
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]

            if previous_user == '' or previous_user == current_user:
                count += 1
                df_line += 1
                tatal_score+=score


            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                average_score = tatal_score / count
                tatal_score = 0

                user_data.append([previous_user, average_score])
                print('user = ', previous_user, ' => count type = ', count_type, ' => count  = ', average_score)
                count = 1
                df_line += 1
                tatal_score += score

            previous_user = current_user

    return user_data