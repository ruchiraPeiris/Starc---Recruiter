from pprint import pprint
import csv
import sys

class DataReader:

    '''
    1 read files
        open dir
        read file line by line
        open two files
    2 read counts to an array
        declare array lang[i] = count of those who know i
        declare dictionary knows_combination[i,j] = number who knows i and knows j
        populate worked_with[ i ] = array of langs ith person worked with

    3 get association counts
        for each lang[i]
            for each worked_with[j]
                if ( worked_with[j] contains lang[i] )
                    lang_prob [i] += 1

    4 calculate weights
        for each lang_prob [i]
            weight[i] = 1/(lang_prob[i]/lang[i])  ... more the probability closer they should be on the graph        

    4 print results
    '''


    def do_process(self):
        dataset_dir = 'DataSet/ProgrammingLanguages.csv'
        item_count_dir = 'item count/database.csv'

        dataset_file = open(dataset_dir, 'r')
        item_count_file = open(item_count_dir, 'r')

        dataset_lines = [line.rstrip('\n').rstrip() for line in dataset_file if line.strip()]
        item_count_lines = [line.rstrip('\n') for line in item_count_file]

        knows_combination = []
        lang = {}

        for combination in dataset_lines:
            knows_combination.append(combination.split(';'))

        for item_count in item_count_lines:
            count = item_count.split(',')
            lang[count[0]] = int(count[1])

        lang_prob = {}
        for l_lang in lang.keys():
            for combination in [x for x in knows_combination if l_lang in x]:
                for c_lang in combination:
                        key = l_lang + ',' + c_lang
                        lang_prob[key] = lang_prob.get(key, 0) + 1

        
        lang_dist = {}
        for lang_combination in lang_prob.keys():
            lang_name = lang_combination.split(',')[0]
            lang_prob[lang_combination] = lang_prob[lang_combination]/lang[lang_name]
            if lang_prob[lang_combination] > 1: lang_prob[lang_combination] = 1
            # lang_dist[lang_combination] = 1 - lang_prob[lang_combination]

        # pprint(knows_combination)

        pprint(sorted(lang_prob.items(), key=lambda x: x[1]))


        # writing to a file
        # somedict = sorted(lang_prob.items(), key=lambda x: x[1])
        # with open(sys.stderr) as f:
        #   w = csv.writer(sys.stdout)
        #   w.writerows(somedict)

if __name__ == '__main__':
    reader = DataReader()
    reader.do_process()
    # pprint(reader.read_all_folders_as_list('person_data'))
