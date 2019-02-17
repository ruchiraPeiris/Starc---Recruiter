import csv
import operator

weights =[
    [3,4,2,5,1],
    [2,3,5,4,1],
    [2,1,5,4,3],
    [5,1,2,3,4],
    [4,3,1,5,2],
    [2,1,4,5,3],
    [3,1,2,5,4],
    [2,1,4,3,5]
]
user_rank = {}
user_rank2 =  {}

def rank_SE():
    for item in weights:

        with open('features.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:

                N = (6-item[0])*float(raw[4])+(6-item[1])*float(raw[1])+(6-item[1])*float(raw[2])+(6-item[2])*float(raw[3])+(6-item[3])*float(raw[6])+(6-item[4])*float(raw[5])
                D = (6-item[0])*2+(6-item[1])+(6-item[2])+(6-item[3])+(6-item[4])
                final_score = float(N)/float(D)
                user_rank.update({raw[0]:final_score})
            print('Software Engineers: '+str(sorted(user_rank.items(), key=operator.itemgetter(1),reverse=True)))
def rank_SSE():
    for item in weights:

        with open('features_SSE.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for raw in csv_reader:

                N = (6-item[0])*float(raw[4])+(6-item[1])*float(raw[1])+(6-item[1])*float(raw[2])+(6-item[2])*float(raw[3])+(6-item[3])*float(raw[6])+(6-item[4])*float(raw[5])
                D = (6-item[0])*2+(6-item[1])+(6-item[2])+(6-item[3])+(6-item[4])
                final_score = float(N)/float(D)
                user_rank2.update({raw[0]:final_score})
            print('Senior Software Engineers: '+str(sorted(user_rank2.items(), key=operator.itemgetter(1),reverse=True)))

rank_SE()
print()
print('///////////////////////////////////////////////////////////////////////////////////////////')
print()
rank_SSE()