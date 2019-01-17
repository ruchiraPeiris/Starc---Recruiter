
import sys
import os, os.path
# comment symbol
commentSymbol = '#'
acceptableFileExtensions = '.py'

if not acceptableFileExtensions:
    print 'File extension not found'
    quit()

currentDir = os.getcwd()
print currentDir

filesToCheck = []
for root, _, files in os.walk(currentDir):
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
print 'Code to comment Ratio:   '+str((float(totalCommentLineCount)/float(codeLines))*100)+' %'