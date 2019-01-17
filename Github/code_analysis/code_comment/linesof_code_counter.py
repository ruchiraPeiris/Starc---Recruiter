
import sys
import os, os.path
import csv
# comment symbol
commentSymbol = '#'
acceptableFileExtensions = '.py'

def load_users():
    with open('../../../Github_repos.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for user in csv_reader:
            user_dir = '../../files/code_snippets/'+user[0]
            if os.path.exists(user_dir):
                currentDir = user_dir
                code_comment_ratio(currentDir, user[0])

def code_comment_ratio(dir_to_check, user_to_check):

    if not acceptableFileExtensions:
        print 'File extension not found'
        quit()

    print dir_to_check

    filesToCheck = []
    for root, _, files in os.walk(dir_to_check):
        for f in files:
            fullpath = os.path.join(root, f)
            if '.git' not in fullpath:
                for extension in acceptableFileExtensions:
                    if fullpath.endswith(extension):
                        filesToCheck.append(fullpath)

    if not filesToCheck:
        print 'No files found.'
        quit()

    lineCount = 0
    totalBlankLineCount = 0
    totalCommentLineCount = 0

    print ''
    print 'Filename\tlines\tblank lines\tcomment lines\tcode lines'
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
                elif lineWithoutWhitespace.startswith(commentSymbol):
                    totalCommentLineCount += 1
                    fileCommentLineCount += 1

            print os.path.basename(fileToCheck) + \
                  "\t" + str(fileLineCount) + \
                  "\t" + str(fileBlankLineCount) + \
                  "\t" + str(fileCommentLineCount) + \
                  "\t" + str(fileLineCount - fileBlankLineCount - fileCommentLineCount)

    codeLines = lineCount - totalBlankLineCount - totalCommentLineCount

    print ''
    print 'Totals'
    print '--------------------'
    print 'Lines:         ' + str(lineCount)
    print 'Blank lines:   ' + str(totalBlankLineCount)
    print 'Comment lines: ' + str(totalCommentLineCount)
    print 'Code lines:    ' + str(codeLines)
    print 'Code to comment Ratio of '+user_to_check+':  ' + str((float(totalCommentLineCount) / float(codeLines)) * 100) + ' %'


load_users()