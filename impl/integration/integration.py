import pandas as pd
import json
from pprint import pprint
import numpy as np


def rank_file(path):

    se_df = pd.read_csv(path)

    ad_data = json.load(open('../ad_inputs/integration_ad.json', 'r'))
    ad_priorities = ad_data['expert_priorities']

    max_priority = max(ad_priorities.values()) + 1
    weights = [
        ad_priorities['experience'],
        ad_priorities['skill'],
        ad_priorities['education'],
        ad_priorities['non_technical'],
        ad_priorities['sentiment'],
        ad_priorities['certifications'],
        ad_priorities['retention_prediction'],

        ad_priorities['code_comment_percentage'],
        ad_priorities['code_quality'],
        ad_priorities['commit_sentiment'],
        ad_priorities['spelling'],
        ad_priorities['popularity'],
        ad_priorities['useof_popular_technologies'],
        ad_priorities['releventness_to_jobadd']
    ]

    se_list = []

    for row in se_df.iterrows():
        index, data = row
        se_list.append(data.tolist()[1:])

    se_list = np.array(se_list)
    weights = np.array(weights)

    weights = max_priority - weights

    product = se_list * weights
    score = []

    for i in range(len(product)):
        score.append(sum(product[i]) / sum(weights))

    names = se_df['name']
    scores = dict(zip(names, score))
    sorted_scores = dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))
    rank = {key: rank for rank, key in enumerate(sorted_scores, 1)}

    rank_column = []
    score_column = []
    for name in names:
        rank_column.append(rank[name])
        score_column.append(scores[name])

    se_df['score'] = score_column
    se_df['rank'] = rank_column

    se_df.to_csv('ranks_'+ path, index=False)

    pprint(score)

if __name__ == '__main__':
    rank_file('for_correlation_se.csv')
    rank_file('for_correlation_sse.csv')

