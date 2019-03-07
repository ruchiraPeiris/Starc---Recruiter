import re
import math
from textblob import TextBlob
import os
from nltk.stem import LancasterStemmer
import sys

afinnTextOpen = os.path.join (os.path.dirname (__file__), "afinn.txt")
afinnText = open(afinnTextOpen, 'r')

afinn = [ws.strip().split('\t') for ws in afinnText]

afinn_dict = dict()
for item in afinn:
    afinn_dict[item[0]] = int(item[1])

pattern_split = re.compile(r"\W+")
afinn = afinn_dict


def sentimentAfinn(text):
    words = pattern_split.split(text.lower())
    sentiments = list(map(lambda word: afinn.get(word, 0), words))
    if sentiments:
        sentiment = float(sum(sentiments)) / math.sqrt(len(sentiments))

    else:
        sentiment = 0
    return sentiment


# StanfordNLP method---------------------------------------------------------------------
def calSentimentLevel(sentimentRate):
    slevel = 0
    if sentimentRate >= 5:
        slevel = 2
    elif sentimentRate >= 1 and sentimentRate < 5:
        slevel = 1
    elif sentimentRate == 0:
        slevel = 0
    elif sentimentRate <= -5:
        slevel = -2
    elif sentimentRate <= -1 and sentimentRate > -5:
        slevel = -1
    return slevel


def textBlb(text):
    blob = TextBlob(text)
    sentimentLevel = 0
    totalPolarity = blob.sentiment.polarity
    polarityLevel = 0
    count = 0

    for sentence in blob.sentences:
        sentencePolarity = sentence.sentiment.polarity
        if sentencePolarity <= -0.75:
            sentimentLevel = -2
            break;

        elif sentencePolarity >= 0.75:
            sentimentLevel = 2
            break;

        elif sentencePolarity > 0.40 and sentencePolarity < 0.75:
            sentimentLevel = 1
            break;

        elif sentencePolarity <= -0.40 and sentencePolarity > -0.75:
            sentimentLevel = -1
            break;

        elif sentencePolarity > -0.40 and sentencePolarity < 0.40:
            sentimentLevel = 0

        polarityLevel = polarityLevel + sentencePolarity
        count = count + 1
        # print(sentencePolarity)
    return sentimentLevel


# Bag of words method-----------------------------------------------------------------------
def bagofwords(comment):
    comment = comment.replace(".", " ")
    comment = comment.replace("?", " ")
    comment = comment.replace("!", " ")


    count = 0
    sentiBOW = 0
    for word in comment.split():
        x = ',' + word + ','

        positiveTextOpen = os.path.join(os.path.dirname(__file__), "positivewords.txt")
        negativeTextOpen = os.path.join(os.path.dirname(__file__), "negativewords.txt")
        afinnText = open(afinnTextOpen, 'r')

        positivewords = open(positiveTextOpen, 'r')
        if x in positivewords.read():
            count = count + 1

        negativewords = open(negativeTextOpen, 'r')
        if x in negativewords.read():
            count = count - 1

    if count <= -20:
        sentiBOW = -2
    elif count < 0:
        sentiBOW = -1
    elif count == 0:
        sentiBOW = 0
    elif count >= 20:
        sentiBOW = 2
    elif count > 0:
        sentiBOW = 1

    return sentiBOW

# ---------------------------------------------------------------------


def match_from_stem(required, candidate):

    stemmer = LancasterStemmer()
    required = list(map(str.lower, list(map(stemmer.stem, required))))
    candidate = list(map(str.lower, list(map(stemmer.stem, candidate))))

    intersection = list(set(required) & set(candidate))
    return len(intersection)/len(required)

# ------------------------------------------------------------------------------------------


def calc_emotional_level(comment):
    '''
    :param comment: a string of text
    :return: emotional level as a integer between -2 and 2.
    '''
    emotionalLevel = 0
    sentiAF = sentimentAfinn(comment)
    sentiBOW = bagofwords(comment)
    sentiSNLP = textBlb(comment)

    Slvl = sentiAF + sentiBOW + sentiSNLP

    if Slvl >= 3:
        emotionalLevel = 2
    elif Slvl >= 1.5 and Slvl < 3:
        emotionalLevel = 1
    elif Slvl >= -1.5 and Slvl < 1.5:
        emotionalLevel = 0
    elif Slvl <= -1.5 and Slvl > -3:
        emotionalLevel = -1
    elif Slvl <= -3:
        emotionalLevel = -2

    return emotionalLevel, sentiAF, sentiBOW, sentiSNLP


if __name__ == "__main__":
    # print(calc_emotional_level('i am a motivated indivdual positive driven passionate idiot'))
    required = 'passionate hard-working team spirited personality energetic challenging'
    candidate = 'highly motivated team working passionate individual'
    print(match_from_stem(required.split(' '), candidate.split(' ')))

