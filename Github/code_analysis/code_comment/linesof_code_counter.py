
import sys
import os, os.path
import csv
from collections import OrderedDict


# comment symbol
acceptableFileExtensions = ['.java','.php','.cpp','.py','.rb','.swift','.ts','.js']
dict_normalized_score = OrderedDict()
def load_users():
    try:
        with open('../../../Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for user in csv_reader:
                user_dir = '../../files/code_snippets/SSE/'+user[0]
                if os.path.exists(user_dir):
                    currentDir = user_dir
                    if len(os.listdir(currentDir)) == 0:
                        print(user[0])
                        #dict_normalized_score.update({user[0]: 0})
                        continue
                    else:
                       cc_ratio = code_comment_ratio(currentDir, user[0])
                       dict_normalized_score.update({user[0]: cc_ratio})
        normalize(dict_normalized_score)
    except Exception as ex:
        print(ex)


def code_comment_ratio(dir_to_check, user_to_check):

    commentSymbol = []
    if not acceptableFileExtensions:
        print('File extension not found')
        quit()

    print('\n'+dir_to_check)

    filesToCheck = []
    for root, _, files in os.walk(dir_to_check):
        for f in files:
            fullpath = os.path.join(root, f)
            print(fullpath)
            if '.git' not in fullpath:
                for extension in acceptableFileExtensions:
                    if fullpath.endswith(extension):
                        filesToCheck.append(fullpath)
                        if extension == '.py':
                            commentSymbol.append('#')
                        elif extension == '.java':
                            commentSymbol.append('//')
                            commentSymbol.append('*')
                        elif extension == '.php':
                            commentSymbol.append('*')
                            commentSymbol.append('//')
                        elif extension == '.rb':
                            commentSymbol.append('#')
                        elif extension == '.swift':
                            commentSymbol.append('//')
                        elif extension == '.ts':
                            commentSymbol.append('//')
                        elif extension == '.js':
                            commentSymbol.append('//')
                            commentSymbol.append('*')



    if not filesToCheck:
        print('No files found.')
        quit()

    lineCount = 0
    totalBlankLineCount = 0
    totalCommentLineCount = 0

    print('')
    print('Filename\tlines\tblank lines\tcomment lines\tcode lines')
    # for loop
    for fileToCheck in filesToCheck:
        with open(fileToCheck) as f:

            fileLineCount = 0
            fileBlankLineCount = 0
            fileCommentLineCount = 0

            for line in f:
                lineCount += 1
                fileLineCount += 1

                lineWithoutWhitespace = line.strip()
                if not lineWithoutWhitespace:
                    totalBlankLineCount += 1
                    fileBlankLineCount += 1
                else:
                    for symbol in commentSymbol:
                        if lineWithoutWhitespace.startswith(symbol) and len(lineWithoutWhitespace)>2:
                            totalCommentLineCount += 1
                            fileCommentLineCount += 1

            print(os.path.basename(fileToCheck) + \
                  "\t" + str(fileLineCount) + \
                  "\t" + str(fileBlankLineCount) + \
                  "\t" + str(fileCommentLineCount) + \
                  "\t" + str(fileLineCount - fileBlankLineCount - fileCommentLineCount))

    codeLines = lineCount - totalBlankLineCount - totalCommentLineCount

    #print ''
    #print 'Totals'
    #print 'Lines:         ' + str(lineCount)
    #print 'Blank lines:   ' + str(totalBlankLineCount)
    #print 'Comment lines: ' + str(totalCommentLineCount)
    #print 'Code lines:    ' + str(codeLines)
    ratio = (float(totalCommentLineCount) / float(codeLines))
    print('Code to comment percerntage of '+user_to_check+':  ' + str(ratio))
    return ratio




def normalize(dict_name_score):

    #print(dict_name_score)

    maximum = max(dict_name_score, key=dict_name_score.get)
    minimum = min(dict_name_score, key=dict_name_score.get)

    print(maximum + ',' + str(dict_name_score[maximum]))
    print(minimum + ',' + str(dict_name_score[minimum]))
    print('////////////////////////////////////')
    for key,val in dict_name_score.items():
        final_score = 1 + float((val - dict_name_score[minimum])*9)/float(dict_name_score[maximum]-dict_name_score[minimum])
        print(key+', '+str(round(final_score,3)))

load_users()