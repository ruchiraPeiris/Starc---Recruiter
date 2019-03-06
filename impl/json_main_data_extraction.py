from datetime import datetime
from datetime import timedelta

from pprint import pprint
import json
import csv
import math
import numpy as np
import itertools as it
import pickle
import networkx as nx
import sentiment.sentiment as sentiment

#  load weights from files
weights_jobs = json.load(open('weights/jobs.json'))
titles = dict(weights_jobs['short_list'])

weights_edu = json.load(open('weights/education.json'))
degrees = weights_edu['degree_name']
it_degrees = weights_edu['degree_spec']
university_rank = weights_edu['university_rank']

# load skills graph to find skill match

skill_graph = nx.DiGraph(pickle.load(open('graph_generation/saved_objects/combined_graph.p', 'rb')))

print_dict = {}

language_score = {
    'English': 10,
    'Sinhala': 9,
    'Tamil': 9
}

proficiency_score = {
    'Elementary proficiency': 0.2,
    'Limited working proficiency': 0.4,
    'Professional working proficiency': 0.6,
    'Full professional working proficiency': 0.8,
    'Native or bilingual proficiency': 1
}

current_profile = {}
priorities_list = [

    "experience",
    "skills",
    "education",
    "ad_match",
    "sentiment"
]
employer_priorities = {
    "experience": 1,
    "skills": 1,
    "education": 1,
    "sentiment": 1
}


columns = ['name', 'no_skills', 'no_langs',
           'no_companies', 'no_positions', 'total_dur',
           'highest_edu','edu_duration', 'no_courses', 'last_job']

csv_file = open('linkedin_csv_data.csv', mode='w')
writer = csv.DictWriter(csv_file, fieldnames=columns)
writer.writeheader()


def main(filename):

    all_info = json.load(open(filename, 'rb'))


    # TODO : Load from file
    required_skills = ['java', 'python', 'html', 'css', 'angular']
    ad_text = "competent communicator energetic passionate positive attitude"

    # load all endorsements for later calculations
    max_endorsements = find_max_endorsements(all_info)

    summary = []
    names = []
    degree_set = set()
    global current_profile
    global print_dict
    global writer

    summary_dicts = []

    for person in all_info:
        try:

            summary_dict = dict()
            print_dict = {}
            current_profile = person['general']
            names.append(current_profile['firstName'])
            positions = person['jobs']
            education = person['schools']
            skill_endorsements = person['skills']
            # recommendation = person['recommendations']
            all_skills = list(map(str.strip, map(str.lower, person['allSkills'].split(','))))

            print(current_profile['fullName'])

            print('Position: ' + person.get('headline', ''))
            print('No of skills: ' + str(len(all_skills)))
            languages = person.get('languages', [1, 2])
            print('No of languages: ' + str(len(languages)))

            print_dict['name'] = current_profile['fullName']
            print_dict['no_skills'] = len(all_skills)
            print_dict['no_langs'] = len(languages)

            # update position dictionary with calculated value
            experience_score = calc_experience(positions)
            summary_dict['experience'] = experience_score

            # calculate es education score
            education_score = calc_education(education)
            summary_dict['education'] = education_score

            # calculate skill score
            skill_score = calculate_skill_match(required_skills, all_skills, skill_endorsements, max_endorsements)
            summary_dict['skills'] = skill_score

            # calculate sentiment score of about me
            sentiment_score = sentiment.calc_emotional_level(current_profile['description'])
            sentiment_score = sentiment_score[1]
            summary_dict['sentiment'] = sentiment_score

            writer.writerow(print_dict)
            print('row written to file')
            # # Calclulate LP Language proficiency
            # lp = 0
            # for language_dict in language_dicts:
            #     language = language_dict['Name']
            #     proficiency = language_dict['Proficiency']
            #     lp += (language_score.get(language) or 0)*(proficiency_score.get(proficiency) or 0)
            #
            # ## print('LP =' + str(lp))

            # candidate_text = recommendation[1]['description'] if len(recommendation) == 2 else ''
            # candidate_text = candidate_text + ' ' + current_profile['description']

            # ad_match_score = sentiment.match_from_stem(ad_text.split(' '), candidate_text.split(' '))
            # summary_dict['ad_match_score'] = ad_match_score

            summary_dicts.append([person, summary_dict])

            summary.append([
                experience_score,
                education_score,
                skill_score,
                sentiment_score,
                # ad_match_score
            ])

        except Exception as e:
            try:
                pass
                print('key error ' + str(e) + str(current_profile['firstName']))
            except Exception as e:
                pprint(e)
                pass
    # print('work exp, education, language profile')
    # pprint(summary)

    # final_scores = calculate_r(summary)
    # display_dict = {}
    # for i in range(0, len(final_scores)):
    #     display_dict[names[i]] = str(final_scores[i])
    #
    # # print('Entropy\n')
    # # pprint(sorted(display_dict.items(), key=lambda kv: kv[1], reverse=True))
    #
    # # experience_score,
    # # education_score,
    # # skill_score,
    # # sentiment_score,
    # # ad_match_score
    #
    # normalized = normalize(summary)
    # priority_weights = [
    #     len(priorities_list) - priorities_list.index("experience"),
    #     len(priorities_list) - priorities_list.index("education"),
    #     len(priorities_list) - priorities_list.index("skills"),
    #     len(priorities_list) - priorities_list.index("sentiment"),
    #     len(priorities_list) - priorities_list.index("ad_match")
    # ]
    #
    # normalized = np.array(normalized)
    #
    # weighted_score = []
    # for r in range(len(normalized)):
    #     for c in range(len(priorities_list)):
    #         normalized[r][c] = normalized[r][c]*priority_weights[c]
    #     weighted_score.append(sum(normalized[r])/sum(priority_weights))
    #
    # display_dict2 = {}
    # for i in range(0, len(final_scores)):
    #     display_dict2[names[i]] = str(weighted_score[i])

    # csv_file.close()
    print()
    print()
    # print('Weights')
    # pprint(sorted(display_dict2.items(), key=lambda kv: kv[1], reverse=True))


def find_max_endorsements(all_info):
    endorsement_summary = {}
    for info in all_info:
        for skill in info['skills']:
            name = str(skill['name']).lower().strip()
            endorsements = (skill['endorsements'])
            endorsements = endorsements if '+' not in endorsements else endorsements[:-1]
            endorsement_summary[name] = max(endorsement_summary.get(name, 0), int(endorsements))

    return endorsement_summary


def calc_experience(positions):
    global current_profile
    global print_dict
    ajv = 0
    p = []
    org = set()
    pos = set()
    for position in positions:
        try:
            position['duration'] = calculate_duration(position).days / 30  # days converted to months
        except ValueError:
            print('Date format error in file ' + current_profile.get('fullName', '1'))

        # calculate sigma value
        dur = position['duration'] or 0
        # tit = titles[position['Title']] if position['jobTitle'] in titles else 0
        tit = get_job_title_score(position['jobTitle'])

        if tit != 0:
            p.append(position)

        ajv += tit * dur

    print('Jobs')
    total_dur = 0
    for pp in p:
        org.add(pp['companyName'])
        pos.add(pp['jobTitle'])
        duration = calculate_duration(pp).days / 365
        total_dur += duration
        print(
            pp['companyName'] + '-->' +
            pp['jobTitle'] + '-->' +
            str(pp['dateRange']) + '-->' +
            str(duration)
        )
    print_dict['no_companies'] = len(org)
    print_dict['no_positions'] = len(pos)
    print_dict['total_dur'] = total_dur

    print('No companies: ' + str(len(org)))
    print('No positions: ' + str(len(pos)))
    print_dict['last_job'] = calculate_duration(positions[0]).days/365 if len(positions) > 0 else 0

    print()

    return ajv


def calc_education(education):
    global print_dict

    es = 0
    h_deg = 0
    total_edu_duration = 0
    max_edu = {}
    for education_dict in education:
        degree_name = education_dict.get('degree', 'none')
        degree_spec = education_dict.get('degreeSpec', degree_name)
        school_name = education_dict.get('schoolName', 'none')

        deg = get_weight(degree_name, degrees)

        # deg = degrees.get(degree_name) or 0 if any(s in degree_spec for s in it_degrees) else 0
        uos = get_weight(school_name, university_rank) or float('inf')
        es += deg * (1.0 / uos)

        h_deg = max(deg, h_deg)
        max_edu = education_dict if h_deg == deg else max_edu
        total_edu_duration += calculate_duration(education_dict).days

    # TODO : REMOVE AFTER DATA EXTRACTION
    print('Education')
    print('Highest Education: ' + max_edu.get('degree', 'null'))
    print('Total Duration: ' + str(total_edu_duration / 365))
    print('No of courses: ' + str(len(education)))
    print('--' * 5)

    print_dict['highest_edu'] = max_edu.get('degree', 'null')
    print_dict['edu_duration'] = total_edu_duration / 365
    print_dict['no_courses'] = len(education)

    return es


def get_job_title_score(text):
    score = 0
    for s in titles.keys():
        if s.lower() in text.lower():
            score = titles[s]
    return score


def get_weight(text, dictionary):
    for item in dictionary.keys():
        if item in text:
            return dictionary[item]
    return 0


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


def calculate_duration(date_range):
    try:
        dates = list(map(str.strip, str(date_range['dateRange']).split('–')))
    except:
        return timedelta(days=0)

    start = dates[0]
    end = dates[1] if len(dates) > 1 else 'Present'

    start_date = datetime.today() if start == '' else try_parsing_date(start)
    end_date = datetime.today() if end == '' or end == 'Present' else try_parsing_date(end)

    try:
        duration = end_date - start_date
    except:
        return timedelta(days=0)
    return duration


def calculate_skill_match(required, candidate_skills, skill_endorsements, max_endorsements):
    endorsements = {}
    for skill_endorsement in skill_endorsements:
        endorsements[str(skill_endorsement['name']).lower()] = int(skill_endorsement['endorsements'])

    #     find closest item to each required
    score = 0.0
    all_nodes = list(skill_graph.nodes())
    candidate_skills = set(candidate_skills).intersection(set(all_nodes))

    for skill in required:
        #         find closest skill to skill
        if skill in candidate_skills:
            score += 1
            score += endorsements[skill] / max_endorsements[skill]
        else:
            try:
                path = nx.multi_source_dijkstra(skill_graph, candidate_skills, skill)
                length = path[0]
                closest_node = path[1][0]
                score += endorsements[closest_node] / max_endorsements[closest_node]
            except Exception:
                length = 1

            length = 1.0 if length >= 1 else float(length)
            score += (1.0 - length)

    return float(score / (2 * len(required)))


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
        values[i][j] = (values[i][j]) / sum_r[j]

    h = []

    for j in range(len(values[0])):
        h_sum = 0
        for i in range(len(values)):
            h_sum += values[i][j] * (math.log(values[i][j]) if values[i][j] != 0 else 0)
        h.append(h_sum * -k)

    # calculate weights
    h = np.array(h)
    w = []
    sum_h = h.sum()
    for h1 in h:
        w.append((1 - h1) / (len(h) - sum_h))

    # print('Entropy weights')
    # print(w)

    # apply weights
    final = []
    for row in summary:
        e_sum = 0
        for idx, col in enumerate(row):
            e_sum += (w[idx] * col)
        final.append(e_sum)
    return final


def normalize(summary):
    arr = np.array(summary)
    vmax = arr.max(axis=0)
    vmin = arr.min(axis=0)

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            arr[r][c] = (arr[r][c] - vmin[c]) / (vmax[c] - vmin[c])

    return arr


if __name__ == '__main__':
    main('final_data/data_for_extraction/part1.json')
    main('final_data/data_for_extraction/part2.json')
    main('final_data/data_for_extraction/part6.json')
    # main('final_data/final dataset/PM_12.json')
    # todo : for SSE file
