import csv
from  nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet
from gensim import corpora

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

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    #print(word_tokens)
    print(filtered_sentence)
    print('=========================================================================')
    print(word_stemmer(filtered_sentence))
    return filtered_sentence


def word_count(post):
    words=word_tokenize(post)
    print(len(words))
    return len(words)

def sentence_count(post):
    sentences = sent_tokenize(post)
    print(len(sentences))
    return len(sentences)

def average_word_length(post):
    return 0

with open('posts_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count==2:
            break
        if line_count == 0:
            # print(f'Column names {row[16]}')
            line_count += 1
        else:
            # print(f'\t{row[8]}')
            #word_count(row[16])
            #sentence_count(row[16])
            remove_stopwords(row[8])
            line_count += 1
    # print(f'Processed {line_count} lines.')






