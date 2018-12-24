import re

def lineCount(fileName):
    file = open(fileName,'r')
    content = file.read()
    pat = r'(/\*.*?\*/|//.*?$)'
    lineCount = 0
    commentCount = 0
    blankCount = 0
    codeCount = 0

    print content
    print '////////////////////////////////////////////////////////////'
    for comment in re.findall(pat,content,re.DOTALL|re.MULTILINE):
            commentCount+=1
            print comment


    for x in file:
        print x
        codeCount+=1

    print 'code line count: '+codeCount.__str__()


lineCount('code')