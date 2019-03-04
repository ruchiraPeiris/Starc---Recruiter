from Stackoverflow import SentimentAnalysis as sa
import pandas as pd
import csv
from datetime import date,datetime


#   Id	Reputation	CreationDate	DisplayName	LastAccessDate	WebsiteUrl	Location	AboutMe	Views	UpVotes	DownVotes	ProfileImageUrl	EmailHash	AccountId

def get_user_deatils(file_path, column_name_for_user_id):
    df = pd.read_csv(file_path)

    df = df.sort_values(column_name_for_user_id)

    user_data = []
    user_data.append(['UserId','name', 'reputation', 'experience', 'upvotes', 'downvotes'])
    today = datetime.today()

    for index, row in df.iterrows():
        reputation = row['Reputation']

        datetime_object = datetime.strptime(row['CreationDate'], '%y-%m-%d %H:%M')
        experience=(today-datetime_object).days

        upvotes = row['UpVotes']
        downvotes = row['DownVotes']

        user_data.append([row['Id'],row['DisplayName'],reputation,experience,upvotes,downvotes])

    with open('C:/Users/pc/Desktop/FYP data/test_results/sse_results.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in user_data:
            writer.writerow(row)
    csvFile.close()

    # return user_data


# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP/data/user_data.csv'
# column_name_for_user_id='Id'
# get_user_years_stovfl(file_path_for_answer_posts,column_name_for_user_id)

# ============================ common method for counting average word counts post,comments user wise =====================================

def get_tags_user_wise(file_path, column_name_for_user_id,text_column_name):
    df = pd.read_csv(file_path)
    df = df.sort_values(column_name_for_user_id)
    user_data = []
    user_data.append(['UserId','tags'])
    tags=[]
    tag_count=0
    count = 0
    df_line = 0
    for index, row in df.iterrows():
        text =row[text_column_name]
        text = ((((text.replace('<', ' ')).replace('>', '')).lstrip()).rstrip()).split(' ')
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]
            if previous_user == '' or previous_user == current_user:
                count += 1
                df_line += 1
                for tag in text:
                    if tag not in tags:
                        tags.append(tag)
                        tag_count+=1
            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                user_data.append([previous_user, tags])
                count = 1
                df_line += 1
                tags=[]
                tag_count=0
                for tag in text:
                    tags.append(tag)
                    tag_count += 1

            previous_user = current_user
    return user_data
