import pandas as pd

#   Id	PostId	Score	Text	CreationDate	UserDisplayName	UserId
#comments=pd.read_csv('C:/Users/pc/Desktop/FYP/data/Comments.csv', delimiter = ',',names=['Id','PostId','Score','Text','CreationDate','UserDisplayName','UserId'])

# ============================ common method for counting post,comments user wise =====================================

def get_count_user_wise(file_path, column_name_for_user_id,count_type):
    df = pd.read_csv(file_path)

    df = df.sort_values(column_name_for_user_id)

    user_data = []
    count = 0
    df_line = 0

    for index, row in df.iterrows():
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]

            if previous_user == '' or previous_user == current_user:
                count += 1
                df_line += 1

            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                user_data.append([previous_user, count])
                print('user = ', current_user,count_type,' = ', count)
                count = 1
                df_line += 1

        previous_user = row[column_name_for_user_id]

    print(len(df.index))
    print(user_data)
    print(len(user_data))

# =============================== getting counts ===============================================================================

# =================== comment counts user wise ==================================================================================
print('=================== comment counts user wise ==================================================================================')
file_path_for_comments='C:/Users/pc/Desktop/FYP/data/Comments.csv'
column_name_for_user_id='UserId'
count_type='comment'

get_count_user_wise(file_path_for_comments, column_name_for_user_id,count_type)

# =================== Answer post counts user wise ==================================================================================
print('=================== Answer post counts user wise ==================================================================================')
file_path_for_answer_posts='C:/Users/pc/Desktop/FYP/data/post_answers_u100.csv'
column_name_for_user_id='OwnerUserId'
count_type='answer_posts'
get_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type)

# =================== Question post counts user wise ==================================================================================
print('=================== Question post counts user wise ==================================================================================')
file_path_for_question_posts='C:/Users/pc/Desktop/FYP/data/post_question_u100.csv'
column_name_for_user_id='OwnerUserId'
count_type='question_posts'
get_count_user_wise(file_path_for_question_posts, column_name_for_user_id,count_type)