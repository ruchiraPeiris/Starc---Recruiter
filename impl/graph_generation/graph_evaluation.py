import networkx as nx
import pickle
from pprint import pprint
import json
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

G = nx.DiGraph(pickle.load(open('saved_objects/combined_graph.p', 'rb')))


def guess(skills):
    distances = dict()

    for skill in skills:

        if not G.has_node(skill):
            continue

        source_path_lengths = dict(nx.single_source_dijkstra_path_length(G, skill))

        for key in source_path_lengths.keys():
            if key not in skills:
                dist = source_path_lengths[key]
                if dist < distances.get(key, 1000):
                    distances[key] = dist

    return distances


if __name__ == '__main__':

    # linkedin_profiles = json.load(open('../final_data/data_for_extraction/part1.json'))

    linkedin_profiles = {}
    d= guess(['c++','java','visual basic','r'])
    d = sorted(d.items(), key=lambda kv: kv[1])
    pprint (d)
    x = 1
    if x == 1:
        results = pickle.load(open('result.p','rb'))

        values = np.fromiter(results.values(), dtype=float)
        keys = np.fromiter(results.keys(), dtype=float)


        plt.plot(keys, values)
        plt.axis([0, 100, 0, 100])
        plt.savefig('plot_image.png')
        plt.show()



    success = 0
    iterations = 2
    limit = range(1, 100)
    results = dict()

    for i in range(len(limit)):
        print('Loop ' + str(i) + 'Running for ' + str(limit[i]))
        for profile in linkedin_profiles:
            all_skills = profile['allSkills']
            all_skills = list(map(str.lower, list(map(str.strip, all_skills.split(',')))))

            all_skills = [x for x in all_skills if G.has_node(x)]

            if len(all_skills) < 1: continue
            popped = all_skills.pop(random.randint(0, len(all_skills) - 1))

            d = guess(all_skills)
            # print('popped')
            # pprint(popped)
            sorted_by_value = dict(sorted(d.items(), key=lambda kv: kv[1])[:limit[i]])
            # print('guesses')
            # pprint(sorted_by_value)

            if popped in sorted_by_value.keys():
                success += 1

        results[limit[i]] = 100*success / len(linkedin_profiles)
        success = 0
        print('Top:{}, Success:{}%'.format(limit[i], results[limit[i]]))

    pprint(results)

    pickle.dump(results,open('result.p','wb'))

    plt.plot(results.keys(), results.values(), 'ro')
    plt.axis([0, 100, 0, 100])
    plt.show()

    for k in results.keys():
        print('{},{}'.format(k,results[k]))