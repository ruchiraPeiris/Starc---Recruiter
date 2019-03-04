from __future__ import unicode_literals
from spacy.lang.en import English
import spacy

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

#=======================================================================================================================

import nltk
nltk.download('wordnet')

#=======================================================================================================================

from nltk.corpus import wordnet as wn


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

#=======================================================================================================================

from nltk.stem.wordnet import WordNetLemmatizer

def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

#=======================================================================================================================

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

#=======================================================================================================================

def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

#=======================================================================================================================

import re
TAG_RE = re.compile(r'<[^>]+>')

# TAG_RE = re.compile('<.*?>')
def remove_tags(text):
    return TAG_RE.sub('', text)

#=======================================================================================================================

def topic_display(corpus):
    import pyLDAvis.gensim
    lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
    pyLDAvis.display(lda_display)
    pyLDAvis.show(lda_display, ip='127.0.0.1', port=8888, n_retries=10, local=True, open_browser=True, http_server=None)

#=======================================================================================================================

def get_topics(text_data,specification):
    global dictionary, corpus, lda
    from gensim import corpora
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    import pickle
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    # ==================================================================================================================
    import gensim
    NUM_TOPICS = 10
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=20)
    ldamodel.save('model5.gensim')

    job_specification = prepare_text_for_lda(specification)
    job_specification_bow = dictionary.doc2bow(job_specification)
    print('**********************************job specification**********', job_specification_bow)
    print('**********************************models**********', ldamodel.get_document_topics(job_specification_bow))

    scores=ldamodel.get_document_topics(job_specification_bow)

    for idx, topic in ldamodel.print_topics(-1):
        print('Topic: {} \nWords: {}'.format(idx, topic))
    total=0
    for s in scores:
        total+=s[1]
        print(s)

    print(total,'=>matching percentage :',total/20)
    # ==================================================================================================================
    dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
    corpus = pickle.load(open('corpus.pkl', 'rb'))
    lda = gensim.models.ldamodel.LdaModel.load('model5.gensim')
    # topic_display(corpus)
    return total/20

# ======================================================================================================================

import pandas as pd

def get_topic_user_wise(file_path, column_name_for_user_id,specification):
    df = pd.read_csv(file_path)
    df = df.sort_values(column_name_for_user_id)
    user_data = []
    users=[]
    df_line = 0

    for index, row in df.iterrows():
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]

            if previous_user == '' or previous_user == current_user:
                line_before = remove_tags(str(row[8]))
                line_after = re.sub(' +', ' ', line_before)
                tokens = prepare_text_for_lda(line_after)
                user_data.append(tokens)
                df_line += 1

            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                socre=0
                if user_data!=[]:
                    socre=get_topics(user_data,specification)
                print('user = >', current_user,'score = >',socre)
                users.append([previous_user, socre])
                user_data = []
                df_line += 1

            previous_user = current_user
    return users


# file_path_for_comments='D:/Desktop data/FYP/data/uer_answer_posts_latest.csv'
# column_name_for_user_id='OwnerUserId'
#
# get_topic_user_wise(file_path_for_comments,column_name_for_user_id)
#
# newtext='Deliver consultancy/training on WSO2 technologies and products for our customers around the globe (on-site and off-site) Provide architectural / development leadership for the technological needs of our customers Provide efficient solutions to WSO2 customers through quick start programs, technical meetings, technical calls, and support queries Debug incidents reported by customers and provide solutions and fixesHelp WSO2 customers to deploy WSO2 products in their environments which include both on-premise and cloud-based deployments Evangelization and community activities, which includes blogging about WSO2 products and technology Contributions to the StackOverflow community'