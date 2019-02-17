import matplotlib.pyplot as plt
import numpy as np
import csv


x = np.arange(1,11)
rank_with_all_features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rank_without_sentiment = [2, 1, 3, 7, 6, 16, 5, 8, 9, 10]
rank_without_codecomment = [1, 2, 3, 7, 9, 4, 5, 6, 10, 8]
rank_without_codequality = [1, 2, 3, 6, 7, 4, 8, 5, 9, 12]
rank_without_popularity = [1, 4, 11, 2, 6, 3, 7, 12, 5, 10]

def without_sentiment():
    plt.xlabel('Top 10 Users')
    plt.ylabel('Rank with all the features and Rank without one feature')
    line_previuos, = plt.plot(x , list(map(float,rank_with_all_features)),label = 'With all features')
    line_new, = plt.plot(x, list(map(float, rank_without_sentiment)),label = 'without sentiment')


    plt.legend([line_previuos, (line_previuos, line_new)], ["With all features'", "without sentiment"])

    plt.show()

def without_codecomment():
    plt.xlabel('Top 10 Users')
    plt.ylabel('Rank with all the features and Rank without one feature')
    line_previuos, = plt.plot(x , list(map(float,rank_with_all_features)),label = 'With all features')
    line_new, = plt.plot(x, list(map(float, rank_without_codecomment)),label = 'without code_comment_ratio')


    plt.legend([line_previuos, (line_previuos, line_new)], ["With all features", "without code_comment_ratio"])

    plt.show()

def without_codequality():
    plt.xlabel('Top 10 Users')
    plt.ylabel('Rank with all the features and Rank without one feature')
    line_previuos, = plt.plot(x , list(map(float,rank_with_all_features)),label = 'With all features')
    line_new, = plt.plot(x, list(map(float, rank_without_codequality)),label = 'without code quality')


    plt.legend([line_previuos, (line_previuos, line_new)], ["With all features", "without code quality"])

    plt.show()

def without_popularity():
    plt.xlabel('Top 10 Users')
    plt.ylabel('Rank with all the features and Rank without one feature')
    line_previuos, = plt.plot(x , list(map(float,rank_with_all_features)),label = 'With all features')
    line_new, = plt.plot(x, list(map(float, rank_without_popularity)),label = 'without popularity')


    plt.legend([line_previuos, (line_previuos, line_new)], ["With all features", "without popularity"])

    plt.show()

without_sentiment()
without_codecomment()
without_codequality()
without_popularity()