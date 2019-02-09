import language_check
import csv
import os

from Github.Github_Api.retrieve_commits import commit_list


def load_users():
    x =0
    paragraph = ''
    try:
        with open('../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                list2 = []
                list2 = commit_list(raw[1], raw[2], raw[3])
                while x<5:
                    for commit2 in list2:
                        paragraph += commit2
                        x =+1
                print(raw[0]+': '+check(paragraph))
    except Exception as ex:
        print(str(ex))


def check(data):

    tool = language_check.LanguageTool('en-GB')
    matches = tool.check(data)
    print(matches)
    print(language_check.correct(data, matches))
    return len(matches)

load_users()