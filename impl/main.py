from data_backups import csv_reader
from datetime import datetime
from pprint import pprint
import math
import numpy as np
import itertools as it

titles = {
    'SE Intern': 0.1,
    'Associate SE': 0.2,
    'SE': 0.3,
    'SSE': 0.4,
    'Associate Tech Lead': 0.5,
    'Tech Lead': 0.6,
    'Associate SA': 0.7,
    'SA': 0.8,
    'Project Manager': 0.9
}

degrees = {
    'Bachelor\'s Degree': 0.8,
    'Master\'s Degree': 0.9,
    'Ph.D': 1
}

university_rank ={
    'University of Moratuwa': 2000,
    'University of Colombo': 2100
}

language_score ={
    'English': 10,
    'Sinhala': 9,
    'Tamil': 9
}

proficiency_score ={
    'Elementary proficiency': 0.2,
    'Limited working proficiency': 0.4,
    'Professional working proficiency': 0.6,
    'Full professional working proficiency': 0.8,
    'Native or bilingual proficiency': 1
}

'''
    m : evaluation indices
    n : objects to evaluate
'''


def main():

    reader = csv_reader.DataReader()

    allInfo = reader.read_all_folders_as_list('verified_data')

    summary = []
    names = []
    for key, personInfo in allInfo.items():
        try:
            profile = personInfo['Profile']
            names.append(profile[0]['First Name'])
           # print( key +' ' + profile[0]['First Name'])
            positions = personInfo.get('Positions') or {}
            education_dicts = personInfo.get('Education') or {}
            language_dicts = personInfo.get('Languages') or {}

            # calculate duration of the job in days
            # update position dictionary with calculated value
            ajv = 0;
            for position in positions:
                try:
                    position['Duration'] = calculate_duration(position).days/30 # days converted to months
                except ValueError:
                    print('Date format error in file ' + personInfo['Profile'][0]['First Name'])

                # calculate sigma value
                tit =0;
                dur = position['Duration'] or 0
                if position['Title'] in titles:
                    tit = titles[position['Title']]

                ajv += tit*dur
            # print('AJV ='+str(ajv))

            # calculate es education score
            es = 0
            for education_dict in education_dicts:
                degree_name = education_dict['Degree Name']
                school_name = education_dict['School Name']
                deg = degrees.get(degree_name) or 0
                uos = university_rank.get(school_name) or float('inf')
                es += deg*(1.0/uos)
           ## print('ES =' + str(es))

            # Calclulate LP Language proficiency
            lp = 0
            for language_dict in language_dicts:
                language = language_dict['Name']
                proficiency = language_dict['Proficiency']
                lp += (language_score.get(language) or 0)*(proficiency_score.get(proficiency) or 0)

            ## print('LP =' + str(lp))

            summary.append([ajv, es, lp])

        except KeyError as e:
            try:
                pass
                # print('key error ' + str(e) + str(personInfo['Profile'][0]['First Name']))
            except Exception as e:
                # pprint(e)
                pass
    print('work exp, education, language profic')
    pprint(summary)
    print('weights')
    final_scores = calculate_r(summary)
    displayDict = {}
    for i in range(0, len(final_scores)):
        displayDict[names[i]] = str(final_scores[i])

    pprint(displayDict)

def try_parsing_date(text):
    formats = [
        "%Y",
        "%b %Y",
        "%d %b %Y",
        "%b-%y",
        '%Y-%m-%d',
        '%d.%m.%Y',
        '%d/%m/%Y']
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')


def calculate_duration(position):
    start = position['Started On']
    end = position['Finished On']

    if start == '':
        start_date = datetime.today()
    else:
        start_date = try_parsing_date(start)

    if end == '':
        end_date = datetime.today()
    else:
        end_date = try_parsing_date(end)

    duration = end_date - start_date
    return duration


def calculate_r(summary):

    # normalize
    values = np.array(summary)
    # pprint(summary)
    max_values = values.max(axis=0)
    min_values = values.min(axis=0)

    for i, j in it.product(range(len(values)), range(len(values[0]))):
        values[i][j] = (values[i][j] - min_values[j]) / (max_values[j] - min_values[j])

    # calculate entropy value
    k = 1 / math.log(len(values))

    sum_r = values.sum(axis=0)

    for i, j in it.product(range(len(values)), range(len(values[0]))):
            values[i][j] = (values[i][j])/sum_r[j]

    h = []

    for j in range(len(values[0])):
        h_sum = 0
        for i in range(len(values)):
            h_sum += values[i][j]*(math.log(values[i][j]) if values[i][j] != 0 else 0)
        h.append(h_sum*-k)

    # calculate weights
    h = np.array(h)
    w = []
    sum_h = h.sum()
    for h1 in h:
        w.append((1-h1)/(len(h) - sum_h))
    print(w)

    # apply weights
    final = []
    for row in summary:
        e_sum = 0
        for idx, col in enumerate(row):
            e_sum += (w[idx]*col)
        final.append(e_sum)
    return final


if __name__ == '__main__':
    main()


