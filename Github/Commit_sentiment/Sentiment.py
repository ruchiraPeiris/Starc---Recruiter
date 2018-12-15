import os
from textblob import TextBlob
import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#Afinn method--------------------------------------------------------------------------

afinnTextOpen = os.path.join (os.path.dirname (__file__), "afinn.txt")
afinnText = open (afinnTextOpen, 'r')


afinn = dict(map(lambda (w, s): (w, int(s)), [ws.strip().split('\t') for ws in afinnText ]))
pattern_split = re.compile(r"\W+")

def sentimentAfinn(text):

    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))

    else:
        sentiment = 0


    return sentiment

#StanfordNLP method---------------------------------------------------------------------
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
        #print(sentencePolarity)
    return sentimentLevel

#Bag of words method-----------------------------------------------------------------------
def bagofwords(comment):
    comment = comment.replace(".", " ")
    comment = comment.replace("?", " ")
    comment = comment.replace("!", " ")

    count = 0
    sentiBOW = 0
    for word in comment.split():
        x = ','+word+','

        positivewordsOpen = os.path.join (os.path.dirname (__file__), "positivewords.txt")
        positivewords = open (positivewordsOpen, 'r')
        if x in positivewords.read():
            count = count + 1

        negativewordsOpen = os.path.join (os.path.dirname (__file__), "negativewords.txt")
        negativewords = open (negativewordsOpen, 'r')
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
#------------------------------------------------------------------------------------------

def calEmotionalLevel(comment):
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

    return emotionalLevel


