import csv
import os
import numpy as np
import matplotlib.pyplot as plt

dict_code_comment_per_language = {}
dict_language_files = {}

dict_code_comment_per_language_SSE = {}
dict_language_files_SSE = {}

dict_code_quality_per_language = {}
dict_language_repos = {}

dict_code_quality_per_language_SSE = {}
dict_language_repos_SSE = {}

result_dict =  {}
result_dict_SSE = {}

    #for key,value in dict_user_repo.items():
        #print key+','+value


def avg_code_comment_per_language_SE():
    extension = ''
    try:
        with open('../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for user in csv_reader:
                user_dir = '../files/code_snippets/SE/'+user[0]
                if os.path.exists(user_dir):
                    currentDir = user_dir
                    if len(os.listdir(currentDir)) == 0:
                        print (user[0])
                        continue
                    else:
                       # print '\n' + currentDir
                        for root, _, files in os.walk(currentDir):
                            for f in files:
                                fullpath = os.path.join(root, f)
                                ext = os.path.splitext(fullpath)[-1]
                                #print ext
                                if dict_code_comment_per_language:
                                        if dict_code_comment_per_language.get(ext):
                                            # print ext+', '+str(dict_code_comment_per_language[ext])
                                            dict_code_comment_per_language[ext]+=float(user[5])
                                            dict_language_files[ext]+=1
                                            # print key

                                        else:
                                            dict_code_comment_per_language.update({ext: float(user[5])})
                                            dict_language_files.update({ext: 1})
                                else:
                                    dict_code_comment_per_language.update({ext: float(user[5])})
                                    dict_language_files.update({ext:1})
                                    # print dict_code_comment_per_language.get(ext)

    except Exception as ex:
        print (ex)

    for key,val in dict_code_comment_per_language.items():
        result = float(dict_code_comment_per_language[key])/float(dict_language_files[key])
        dict_code_comment_per_language[key]=result

    for x, y in dict_code_comment_per_language.items():
        print (x+', '+str(y))

def avg_code_comment_per_language_SSE():
    try:
        with open('../../Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for user in csv_reader:
                user_dir = '../files/code_snippets/SSE/'+user[0]
                if os.path.exists(user_dir):
                    currentDir = user_dir
                    if len(os.listdir(currentDir)) == 0:
                        print (user[0])
                        continue
                    else:
                       # print '\n' + currentDir
                        for root, _, files in os.walk(currentDir):
                            for f in files:
                                fullpath = os.path.join(root, f)
                                ext = os.path.splitext(fullpath)[-1]
                                #print ext
                                if dict_code_comment_per_language_SSE:
                                        if dict_code_comment_per_language_SSE.get(ext):
                                            # print ext+', '+str(dict_code_comment_per_language[ext])
                                            dict_code_comment_per_language_SSE[ext]+=float(user[5])
                                            dict_language_files_SSE[ext]+=1
                                            # print key

                                        else:
                                            dict_code_comment_per_language_SSE.update({ext: float(user[5])})
                                            dict_language_files_SSE.update({ext: 1})
                                else:
                                    dict_code_comment_per_language_SSE.update({ext: float(user[5])})
                                    dict_language_files_SSE.update({ext:1})
                                    # print dict_code_comment_per_language.get(ext)

    except Exception as ex:
        print (ex)
    for key,val in dict_code_comment_per_language_SSE.items():
        result = float(dict_code_comment_per_language_SSE[key])/float(dict_language_files_SSE[key])
        dict_code_comment_per_language_SSE[key]=result
        #print key + ', ' + str(val)

def code_quality_per_language_SE():

    try:
        with open('../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                if dict_code_quality_per_language:
                    if dict_code_quality_per_language.get(raw[6]):
                        # print ext+', '+str(dict_code_comment_per_language[ext])
                        dict_code_quality_per_language[raw[6]] += float(raw[7])
                        dict_language_repos[raw[6]] += 1
                        # print key

                    else:
                        dict_code_quality_per_language.update({raw[6]: float(raw[7])})
                        dict_language_repos.update({raw[6]: 1})
                else:
                    dict_code_quality_per_language.update({raw[6]: float(raw[7])})
                    dict_language_repos.update({raw[6]: 1})
    except Exception as ex:
        print (ex)

    for key,val in dict_code_quality_per_language.items():
        result = (float(dict_code_quality_per_language[key])/float(dict_language_repos[key]))
        dict_code_quality_per_language[key] = result

def code_quality_per_language_SSE():

    try:
        with open('../../Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                if dict_code_quality_per_language_SSE:
                    if dict_code_quality_per_language_SSE.get(raw[6]):
                        # print ext+', '+str(dict_code_comment_per_language[ext])
                        dict_code_quality_per_language_SSE[raw[6]] += float(raw[7])
                        dict_language_repos_SSE[raw[6]] += 1
                        # print key

                    else:
                        dict_code_quality_per_language_SSE.update({raw[6]: float(raw[7])})
                        dict_language_repos_SSE.update({raw[6]: 1})
                else:
                    dict_code_quality_per_language_SSE.update({raw[6]: float(raw[7])})
                    dict_language_repos_SSE.update({raw[6]: 1})
    except Exception as ex:
        print (ex)

    for key,val in dict_code_quality_per_language_SSE.items():
        result = (float(dict_code_quality_per_language_SSE[key])/float(dict_language_repos_SSE[key]))
        dict_code_quality_per_language_SSE[key]=result

def result():
    languages = ['swift','java','python','php','javascript']


    a = (float(dict_code_comment_per_language['.swift'])+float(dict_code_quality_per_language['swift']))/2
    b = (float(dict_code_comment_per_language['.java']) + float(dict_code_quality_per_language['java'])) / 2
    c = (float(dict_code_comment_per_language['.py']) + float(dict_code_quality_per_language['py'])) / 2
    d = (float(dict_code_comment_per_language['.php']) + float(dict_code_quality_per_language['php'])) / 2
    e = (float(dict_code_comment_per_language['.js']) + float(dict_code_quality_per_language['js'])) / 2
    result_dict.update({'Swift':a})
    result_dict.update({'Java':b})
    result_dict.update({'Python':c})
    result_dict.update({'PHP':d})
    result_dict.update({'JavaScript':e})


    for key,val in result_dict.items():
        print (key+', '+str(val))

    p = (float(dict_code_comment_per_language_SSE['.swift']) + float(dict_code_quality_per_language_SSE['swift'])) / 2
    q = (float(dict_code_comment_per_language_SSE['.java']) + float(dict_code_quality_per_language_SSE['java'])) / 2
    r = (float(dict_code_comment_per_language_SSE['.py']) + float(dict_code_quality_per_language_SSE['py'])) / 2
    s = (float(dict_code_comment_per_language_SSE['.php']) + float(dict_code_quality_per_language_SSE['php'])) / 2
    t = (float(dict_code_comment_per_language_SSE['.js']) + float(dict_code_quality_per_language_SSE['js'])) / 2

    result_dict_SSE.update({'Swift': p})
    result_dict_SSE.update({'Java': q})
    result_dict_SSE.update({'Python': r})
    result_dict_SSE.update({'PHP': s})
    result_dict_SSE.update({'JavaScript': t})

    print ('SSE\n')
    for key,val in result_dict_SSE.items():
        print (key+', '+str(val))


def genrate_histogram(result_dict,result_dict_SSE):
    n_groups = 5
    Software_Eng = (result_dict['Swift'],result_dict['Java'],result_dict['Python'],result_dict['PHP'],result_dict['JavaScript'])
    Senior_Software_Eng = (result_dict_SSE['Swift'],result_dict_SSE['Java'],result_dict_SSE['Python'],result_dict_SSE['PHP'],result_dict_SSE['JavaScript'])

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, Software_Eng, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Software Engineers')

    rects2 = plt.bar(index + bar_width, Senior_Software_Eng, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Senior Software Engineers')

    plt.xlabel('Languages')
    plt.ylabel('Avg code quality and code-comment percentage%')
    plt.title('Average code quality and code-comment percentage per language')
    plt.xticks(index + bar_width, ('Swift', 'Java', 'Python', 'PHP','JavaScript'))
    plt.legend()

    plt.tight_layout()
    plt.show()

print ('code_comment SE\n')
avg_code_comment_per_language_SE()
print ('code_comment SSE\n')
avg_code_comment_per_language_SSE()
print ('code quality SE\n')
code_quality_per_language_SE()
print ('code quality SSE\n')
code_quality_per_language_SSE()
print ('Final Result\n')

result()
genrate_histogram(result_dict,result_dict_SSE)
