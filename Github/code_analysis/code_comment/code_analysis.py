import os
import re
import csv
from pylint import lint
from pylint.lint import Run
import invoke_sonar as sonar


class WritableObject(object):
    "dummy output stream for pylint"
    def __init__(self):
        self.content = []
    def write(self, st):
        "dummy write"
        self.content.append(st)
    def read(self):
        "dummy read"
        return self.content


def run_pylint(filename):
    "run pylint on the given file"
    from pylint import lint
    from pylint.reporters.text import TextReporter
    pylint_output = WritableObject()
    lint.Run([filename], reporter=TextReporter(pylint_output), exit=False)
    for l in pylint_output.read():
        if l.split(' ', 1)[0] == 'Your':
            return l

def invoke():
    try:
        with open('../../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for user in csv_reader:
                if os.path.isfile('../../files/code_snippets/'+user[0]+'/'+user[0]+'.py'):
                    print user[0]+', '+run_pylint('../../files/code_snippets/'+user[0]+'/'+user[0]+'.py')
                    return
    except Exception, ex:
        print ex


def pylintScore():

    Run(['warnings', '../../Github_Api/retrieve_commits.py'])
    return lint.msg


# print +pylintScore()

invoke()
