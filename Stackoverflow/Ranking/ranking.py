import pandas as pd
import re
import csv
import numpy as np
from jedi.evaluate.utils import to_list


def get_rank(p1,p2,p3,p4,filename):
    newdtf = pd.read_csv('C:/Users/pc/Desktop/FYP data/test_results/sse_results_new.csv')
    newdtf = newdtf.fillna(0)
    w_Technical_skills = p1
    w_Communication_skills = p2
    w_experience_on_stackoverflow_profile_usage = p3
    w_Popularity_among_the_other_users = p4
    w_releventness_to_jobadd = 0.25
    newuser = []
    newuser.append(['UserId', 'name', 'Technical_skills_socre', 'Communication_skills_socre',
                    'experience_on_stackoverflow_profile_usage_socre', 'Popularity_among_the_other_users_socre','releventness_to_jobadd',
                    'final_score', 'job'])
    count = 0
    for index1, row1 in newdtf.iterrows():
        print('=========11')
        # if count==0:
        #     count += 1
        #     break

        print('=========')
        count += 1
        Technical_skills_socre = row1['Technical_skills'] * w_Technical_skills
        Communication_skills_socre = row1['Communication_skills'] * w_Communication_skills
        experience_on_stackoverflow_profile_usage_socre = row1[
                                                              'Popularity_among_the_other_users'] * w_Popularity_among_the_other_users
        Popularity_among_the_other_users_socre = row1['Popularity_among_the_other_users'] * w_releventness_to_jobadd
        # releventness_to_jobadd_score = w_releventness_to_jobadd * row1['releventness_to_jobadd']

        total_w = (
        w_Technical_skills + w_Communication_skills + w_experience_on_stackoverflow_profile_usage + w_Popularity_among_the_other_users + w_releventness_to_jobadd)
        total_score = (
        Technical_skills_socre + Communication_skills_socre + experience_on_stackoverflow_profile_usage_socre + Popularity_among_the_other_users_socre)

        final_score = (((total_score / total_w))+row1['releventness_to_jobadd'])/2

        newuser.append([row1['UserId'], row1['name'], Technical_skills_socre, Communication_skills_socre,
                        experience_on_stackoverflow_profile_usage_socre, Popularity_among_the_other_users_socre,
                        row1['releventness_to_jobadd'],final_score, row1['job']])
    print(newuser)
    filepath='C:/Users/pc/Desktop/FYP data/test_results/'+filename+'.csv'
    with open(filepath, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in newuser:
            writer.writerow(row)
        csvFile.close()

experts=[
    [3,2,4,4],
    [1,3,2,4],
    [1,3,4,2],
    [3,1,4,2],
    [2,1,3,4],
    [1,3,4,2],
    [1,3,4,2],
    [2,3,4,1]
]
count=0
for e in experts:
    w_Technical_skills_val = e[0]
    w_Communication_skills_val = e[1]
    w_experience_on_stackoverflow_profile_usage_val = e[2]
    w_Popularity_among_the_other_users_val = e[3]
    filename = 'sse_user_rank_'+str(count)
    get_rank(w_Technical_skills_val, w_Communication_skills_val, w_experience_on_stackoverflow_profile_usage_val,
             w_Popularity_among_the_other_users_val, filename)
    count+=1

def get_rank_gui(list):
    newdtf = pd.read_csv('C:/Users/pc/Desktop/FYP data/test_results/sse_results_new.csv')
    newdtf = newdtf.fillna(0)
    w_Technical_skills = p1
    w_Communication_skills = p2
    w_experience_on_stackoverflow_profile_usage = p3
    w_Popularity_among_the_other_users = p4
    w_releventness_to_jobadd = 0.25
    newuser = []
    newuser.append(['UserId', 'name', 'Technical_skills_socre', 'Communication_skills_socre',
                    'experience_on_stackoverflow_profile_usage_socre', 'Popularity_among_the_other_users_socre','releventness_to_jobadd',
                    'final_score', 'job'])
    count = 0
    for index1, row1 in newdtf.iterrows():
        print('=========11')
        # if count==0:
        #     count += 1
        #     break

        print('=========')
        count += 1
        Technical_skills_socre = row1['Technical_skills'] * w_Technical_skills
        Communication_skills_socre = row1['Communication_skills'] * w_Communication_skills
        experience_on_stackoverflow_profile_usage_socre = row1[
                                                              'Popularity_among_the_other_users'] * w_Popularity_among_the_other_users
        Popularity_among_the_other_users_socre = row1['Popularity_among_the_other_users'] * w_releventness_to_jobadd
        # releventness_to_jobadd_score = w_releventness_to_jobadd * row1['releventness_to_jobadd']

        total_w = (
        w_Technical_skills + w_Communication_skills + w_experience_on_stackoverflow_profile_usage + w_Popularity_among_the_other_users + w_releventness_to_jobadd)
        total_score = (
        Technical_skills_socre + Communication_skills_socre + experience_on_stackoverflow_profile_usage_socre + Popularity_among_the_other_users_socre)

        final_score = (((total_score / total_w))+row1['releventness_to_jobadd'])/2

        newuser.append([row1['UserId'], row1['name'], Technical_skills_socre, Communication_skills_socre,
                        experience_on_stackoverflow_profile_usage_socre, Popularity_among_the_other_users_socre,
                        row1['releventness_to_jobadd'],final_score, row1['job']])
    print(newuser)
    filepath='C:/Users/pc/Desktop/FYP data/test_results/'+filename+'.csv'
    with open(filepath, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in newuser:
            writer.writerow(row)
        csvFile.close()

