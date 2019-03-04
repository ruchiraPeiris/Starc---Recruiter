import pandas as pd
from  nltk.tokenize import word_tokenize, sent_tokenize
from spellchecker import SpellChecker

from Stackoverflow.nlp import SentimentAnalysis as sa

spell = SpellChecker()

def get_incorrect_word_count_user_wise(file_path, column_name_for_user_id,count_type,text_column_name):
    df = pd.read_csv(file_path)

    df = df.sort_values(column_name_for_user_id)

    user_data = []
    user_data.append(['UserId', 'count_of_incorrct_words'])
    word_count=0
    count = 0
    df_line = 0

    for index, row in df.iterrows():

        text =sa.remove_stopwords(sa.remove_tags(row[text_column_name]))


        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            word_tokens = word_tokenize(text)
            for word in word_tokens:
                current_user = row[column_name_for_user_id]
                if spell.correction(word):
                    if (previous_user == '' or previous_user == current_user) :
                        count += 1
                        df_line += 1
                        word_count+=sa.word_count(text)

                    if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):

                        user_data.append([previous_user, count])
                        print('user = ', current_user,' => count type = ',count_type,' => count  = ', count)
                        count = 1
                        df_line += 1


        previous_user = row[column_name_for_user_id]

    return user_data

print('=================== get_incorrect_word_count_user_wise ==================================================================================')
file_path_for_answer_posts='D:/Desktop data/FYP/data/question_poat_data_all.csv'
column_name_for_user_id='OwnerUserId'
count_type='incorrect words'
text_column_name='Body'
data=get_incorrect_word_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
print(data)