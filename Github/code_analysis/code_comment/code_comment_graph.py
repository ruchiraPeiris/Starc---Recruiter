import matplotlib.pyplot as plt
import numpy as np
import csv


plt.ylabel('Comment-code percentage %')
plt.xlabel('Applicants')
x = np.arange(1,25)
#x_array_SE = []
y_array_SE = []
#x_array_SSE = []
y_array_SSE = []


def loadSE():
    try:
        with open('../../../Github_repos.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                #x_array_SE.append(raw[0])
                y_array_SE.append(raw[5])

    except Exception as ex:
        print(ex)


def loadSSE():
    try:
        with open('../../../Github_repos_SSE.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for raw in csv_reader:
                #x_array_SSE.append(raw[0])
                y_array_SSE.append(raw[5])
                print(raw[5])

    except Exception as ex:
        print(ex)

loadSE()
loadSSE()
print(y_array_SSE)

line_se, = plt.plot(x , list(map(float,y_array_SE)),label = 'Software Engineer')
line_sse, = plt.plot(x, list(map(float, y_array_SSE)),label = 'Senior Software Engineer')


plt.legend([line_se, (line_se, line_sse)], ["Software Engineers", "Senior Software Engineers"])

plt.show()
