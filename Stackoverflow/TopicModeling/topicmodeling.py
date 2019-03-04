import nltk
import spacy
import random
import gensim
import csv
from nltk.corpus import wordnet as wn

from nltk.stem.wordnet import WordNetLemmatizer



spacy.load('en')
from spacy.lang.en import English
parser = English()

def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

en_stop = set(nltk.corpus.stopwords.words('english'))

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

def prepare_text_for_lda(text):
    tokens = tokenize(text)
    print('lenth = ',len(tokens))
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


text_data = []
with open('posts_data.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 10:
            break
        if line_count == 0:
            #print(f'Column names {row[16]}')
            line_count += 1
        else:
            #print(f'\t{row[8]}')
            tokens = prepare_text_for_lda(row[8])
            if random.random() > .99:
                print(tokens)
                text_data.append(tokens)
            line_count += 1
    #
    # for line in f:
    #     tokens = prepare_text_for_lda(line)
    #     if random.random() > .99:
    #         print(tokens)
    #         text_data.append(tokens)

# from gensim import corpora
#
# dictionary = corpora.Dictionary(text_data)
# dictionary.filter_extremes(no_below=4, no_above=0.8)
# corpus = [dictionary.doc2bow(text) for text in text_data]
# import pickle
# pickle.dump(corpus, open('corpus.pkl', 'wb'))
# dictionary.save('dictionary.gensim')


from gensim import corpora
dictionary = corpora.Dictionary(text_data)
print('text_data = ',text_data)
print('Dictionary = ',dictionary)
corpus = [dictionary.doc2bow(text) for text in text_data]

print('corpus = ',corpus)
import pickle
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')



# NUM_TOPICS = 5
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
# ldamodel.save('model5.gensim')
# topics = ldamodel.print_topics(num_words=4)
# for topic in topics:
#     print(topic)
#
#
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 3, id2word=dictionary, passes=15)
# ldamodel.save('model3.gensim')
# topics = ldamodel.print_topics(num_words=4)
# for topic in topics:
#     print(topic)

# print('corpus = ',corpus)
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 10, id2word=dictionary, passes=15)
# ldamodel.save('modelnew.gensim')
# topics = ldamodel.print_topics(num_words=4)
#
# for topic in topics:
#     print(topic)


import gensim
NUM_TOPICS = 10
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('model5.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)