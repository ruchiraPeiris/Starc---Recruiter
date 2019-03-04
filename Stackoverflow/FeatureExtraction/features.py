import pandas as pd
import re
import csv
import numpy as np
from jedi.evaluate.utils import to_list

df = pd.read_csv('C:/Users/pc/Desktop/FYP data/test_results/sse_results.csv')
df=df.fillna(0)


user_data=[]
user_data.append(['UserId','name','reputation','experience','upvotes','downvotes','avg_word_count_answer_posts','avg_word_count_question_posts','avg_setence_count_answer_posts','avg_setence_count_question_posts','avg_word_count_comments','avg_setence_count_comments','code_count_in_answer_posts','tags','question_posts_similarity','answer_posts_similarity','job','avg_comment_count_answer_posts','avg_answer_count_answer_posts','avg_viewcount_count_question_posts','releventness_to_jobadd'])

for index, row in df.iterrows():
    if row['UserId'] != 0:
        reputation = (row['reputation'] - df['reputation'].min()) / (df['reputation'].max() - df['reputation'].min())
        experience = (row['experience'] - df['experience'].min()) / (df['experience'].max() - df['experience'].min())
        upvotes = (row['upvotes'] - df['upvotes'].min()) / (df['upvotes'].max() - df['upvotes'].min())
        downvotes = (row['downvotes'] - df['downvotes'].min()) / (df['downvotes'].max() - df['downvotes'].min())
        avg_word_count_answer_posts = (row['avg_word_count_answer_posts'] - df['avg_word_count_answer_posts'].min()) / (
        df['avg_word_count_answer_posts'].max() - df['avg_word_count_answer_posts'].min())
        avg_word_count_question_posts = (row['avg_word_count_question_posts'] - df[
            'avg_word_count_question_posts'].min()) / (df['avg_word_count_question_posts'].max() - df[
            'avg_word_count_question_posts'].min())
        avg_setence_count_answer_posts = (row['avg_setence_count_answer_posts'] - df[
            'avg_setence_count_answer_posts'].min()) / (df['avg_setence_count_answer_posts'].max() - df[
            'avg_setence_count_answer_posts'].min())
        avg_setence_count_question_posts = (row['avg_setence_count_question_posts'] - df[
            'avg_setence_count_question_posts'].min()) / (df['avg_setence_count_question_posts'].max() - df[
            'avg_setence_count_question_posts'].min())
        avg_word_count_comments = (row['avg_word_count_comments'] - df['avg_word_count_comments'].min()) / (
        df['avg_word_count_comments'].max() - df['avg_word_count_comments'].min())
        avg_setence_count_comments = (row['avg_setence_count_comments'] - df['avg_setence_count_comments'].min()) / (
        df['avg_setence_count_comments'].max() - df['avg_setence_count_comments'].min())
        code_count_in_answer_posts = (row['code_count_in_answer_posts'] - df['code_count_in_answer_posts'].min()) / (
        df['code_count_in_answer_posts'].max() - df['code_count_in_answer_posts'].min())
        question_posts_similarity = (row['question_posts_similarity'] - df['question_posts_similarity'].min()) / (
        df['question_posts_similarity'].max() - df['question_posts_similarity'].min())
        answer_posts_similarity = (row['answer_posts_similarity'] - df['answer_posts_similarity'].min()) / (
        df['answer_posts_similarity'].max() - df['answer_posts_similarity'].min())
        avg_comment_count_answer_posts = (row['avg_comment_count_answer_posts'] - df[
            'avg_comment_count_answer_posts'].min()) / (df['avg_comment_count_answer_posts'].max() - df[
            'avg_comment_count_answer_posts'].min())
        avg_answer_count_answer_posts = (row['avg_answer_count_answer_posts'] - df[
            'avg_answer_count_answer_posts'].min()) / (df['avg_answer_count_answer_posts'].max() - df[
            'avg_answer_count_answer_posts'].min())
        avg_viewcount_count_question_posts = (row['avg_viewcount_count_question_posts'] - df[
            'avg_viewcount_count_question_posts'].min()) / (df['avg_viewcount_count_question_posts'].max() - df[
            'avg_viewcount_count_question_posts'].min())
        releventness_to_jobadd = (row['releventness_to_jobadd'] - df['releventness_to_jobadd'].min()) / (
        df['releventness_to_jobadd'].max() - df['releventness_to_jobadd'].min())


    # tags=0
    # # UserId											tags			job
    if row['tags']!=0:

        tagsset = row['tags']
        tagset = re.sub('\[', '', tagsset)
        tagset = re.sub('\]', '', tagset)
        tagset = re.sub('\'', '', tagset)
        # print(tagset)
        tagset = tagset.split(',')
        a = list(tagset)
        tags=len(a)
        # print(a,'====',len(a))


    if row['UserId'] != 0:
        user_data.append([row['UserId'],row['name'],reputation,experience,upvotes,downvotes,avg_word_count_answer_posts,avg_word_count_question_posts,avg_setence_count_answer_posts,avg_setence_count_question_posts,avg_word_count_comments,avg_setence_count_comments,code_count_in_answer_posts,tags,question_posts_similarity,answer_posts_similarity,row['job'],avg_comment_count_answer_posts,avg_viewcount_count_question_posts,avg_answer_count_answer_posts,releventness_to_jobadd])


with open('C:/Users/pc/Desktop/FYP data/test_results/sse_results_temp.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    for row in user_data:
        writer.writerow(row)
    csvFile.close()

newdtf=pd.read_csv('C:/Users/pc/Desktop/FYP data/test_results/sse_results_temp.csv')
newdtf=newdtf.fillna(0)

newuser=[]
newuser.append(['UserId','name','Technical_skills','Communication_skills','experience_on_stackoverflow_profile_usage','Popularity_among_the_other_users','releventness_to_jobadd','job'])
for index1, row1 in newdtf.iterrows():

    if row1['UserId'] != 0:
        tags = (row1['tags'] - newdtf['tags'].min()) / (newdtf['tags'].max() - newdtf['tags'].min())

        Technical_skills = (row1['code_count_in_answer_posts'] + tags -row1['question_posts_similarity']-row1['answer_posts_similarity'] + row1['upvotes'] + row1['downvotes']) / 6
        Communication_skills=(row1['avg_word_count_answer_posts']+    row1['avg_word_count_question_posts']+    row1['avg_setence_count_answer_posts']+    row1['avg_setence_count_question_posts']+    row1['avg_word_count_comments']+    row1['avg_setence_count_comments'])/6
        experience_on_stackoverflow_profile_usage=(row1['experience']+ row1['reputation'])/2
        Popularity_among_the_other_users=    (row1['avg_comment_count_answer_posts']+row1['avg_viewcount_count_question_posts'])/2
    if row1['UserId'] != 0:
        newuser.append([row1['UserId'],row1['name'],Technical_skills,Communication_skills,experience_on_stackoverflow_profile_usage,Popularity_among_the_other_users,row1['releventness_to_jobadd'],row1['job']])

with open('C:/Users/pc/Desktop/FYP data/test_results/sse_results_new.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    for row in newuser:
        writer.writerow(row)
    csvFile.close()





















