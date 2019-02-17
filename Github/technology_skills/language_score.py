import csv
from collections import OrderedDict
import json
import requests



dict_user_lang = OrderedDict()

dict_lang_popularity = {
    'JavaScript': 338,
    'Java': 67,
    'Python':63,
    'Ruby':44,
    'Objective-C':43,
    'Go':39,
    'HTML':34,
    'CSS':30,
    'C++':28,
    'Swift':28,
    'C':26,
    'PHP':23,
    'Shell':20,
    'TypeScript':15,
    'C#':9,
    'Scala':5,
    'Kotlin':1,
    'pare':2
}

result = OrderedDict()

def normalize_and_store(dict):
        # print(dict_name_score)

        maximum = max(dict, key=dict.get)
        minimum = min(dict, key=dict.get)

        print(maximum + ',' + str(dict[maximum]))
        print(minimum + ',' + str(dict[minimum]))
        max_val = dict[maximum]
        min_val = dict[minimum]

        for key, val in dict.items():
            final_score = 0 + float((val - min_val)*1)/ float(max_val - min_val)
            #print(key+', '+str(final_score))
            dict[key] = final_score


        return dict

print(normalize_and_store(dict_lang_popularity))

def get_lang(user_name,repo):
    max = 0
    lang = ''
    try:
        url = 'https://api.github.com/repos/'+user_name+'/'+repo+'/languages?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34'
        response2 = requests.get(url)
        lang_data = json.loads(response2.content)
        for key,val in list(lang_data.items()):
            if val > max:
                lang = key
                max = val



    except Exception as ex:
        print('error occurred while finding repo language: '+str(ex))

    return lang


with open('../../Github_repos_SSE.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for raw in csv_reader:
        repo_lang = get_lang(raw[2],raw[3])
        dict_user_lang.update({raw[0]:repo_lang})
    print(dict_user_lang)

def final_result():
    for key, val in dict_user_lang.items():
        try:
            if dict_lang_popularity[val]:
                score = dict_lang_popularity.get(val)
            else:
                score = 0
        except Exception as ex:
            print('error occurred: '+str(ex))
            score = 0
        print(key+', '+str(round(score,4)))

final_result()