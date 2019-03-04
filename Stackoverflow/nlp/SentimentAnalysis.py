from  nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from pip._internal import main

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(post):
    score = analyser.polarity_scores(post)
    # print("{:-<40} {}".format(post, str(score)))
    # print(score['neg'])
    return score

def text_subjectivity(post):
    analysis = TextBlob(post)
    print(analysis.sentiment)

def word_stemmer(words):
    ps = PorterStemmer()
    filtered_sentence = []
    for w in words:
        filtered_sentence.append(ps.stem(w))
    return filtered_sentence

def remove_stopwords(post):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(post)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = ''

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence+=(w+' ')

    #print(word_tokens)
    # print(filtered_sentence)
    #print('=========================================================================')
    #print(word_stemmer(filtered_sentence))
    return filtered_sentence


def word_count(post):
    words=word_tokenize(post)
    # print(len(words))
    return len(words)

def sentence_count(post):
    sentences = sent_tokenize(post)
    # print(len(sentences))
    return len(sentences)

def average_word_length(post):
    return 0

import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

# with open('posts_data.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count==2:
#             break
#         if line_count == 0:
#             print(f'Column names {row[8]}')
#             line_count += 1
#         else:
#             print(f'\t{row[8]}')
#             print('==================================================================================')
#             print(remove_tags(row[8]))
#             line_count += 1
#     print(f'Processed {line_count} lines.')






