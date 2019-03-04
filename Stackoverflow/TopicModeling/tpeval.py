# Import required packages
import csv
import json
import logging
import numpy as np
import pandas as pd
import pyLDAvis.gensim
import re
import warnings

from Stackoverflow.nlp import SentimentAnalysisImpl as stimpl

warnings.filterwarnings('ignore')  # To ignore all warnings that arise here to enhance clarity

from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from numpy import array

# Import dataset
p_df = pd.read_csv('D:/Desktop data/FYP/data/uer_answer_posts_latest.csv')
# Create sample of 100 posts
p_df = p_df.sample(n=100)
# Convert to array
docs = array(p_df['Body'])


# TAG_RE = re.compile('<.*?>')
def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def docs_preprocessor(docs):
    tokenizer = RegexpTokenizer(r'\w+')
    for idx in range(len(docs)):
        docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

    # Remove numbers, but not words that contain numbers.
    docs = [[token for token in doc if not token.isdigit()] for doc in docs]

    # Remove words that are only one character.
    docs = [[token for token in doc if len(token) > 3] for doc in docs]

    # Lemmatize all words in documents.
    lemmatizer = WordNetLemmatizer()
    docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

    return docs


def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values


# docs =remove_tags(docs)
# Define function for tokenize and lemmatizing
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

# docs[idx] = docs[idx].lower()  # Convert to lowercase.
def evaluate(docs):
    # global docs
    # Perform function on our document
    docs = docs_preprocessor(docs)
    # Create Biagram & Trigram Models
    from gensim.models import Phrases
    if __name__ == "__main__":
        # Add bigrams and trigrams to docs,minimum count 10 means only that appear 10 times or more.
        bigram = Phrases(docs, min_count=10)
        trigram = Phrases(bigram[docs])

        for idx in range(len(docs)):
            for token in bigram[docs[idx]]:
                if '_' in token:
                    # Token is a bigram, add to document.
                    docs[idx].append(token)
            for token in trigram[docs[idx]]:
                if '_' in token:
                    # Token is a bigram, add to document.
                    docs[idx].append(token)
        # Remove rare & common tokens
        # Create a dictionary representation of the documents.
        dictionary = Dictionary(docs)
        dictionary.filter_extremes(no_below=10, no_above=0.2)
        # Create dictionary and corpus required for Topic Modeling
        corpus = [dictionary.doc2bow(doc) for doc in docs]
        print('Number of unique tokens: %d' % len(dictionary))
        print('Number of documents: %d' % len(corpus))
        print(corpus[:1])

        # Set parameters.
        num_topics = 20
        chunksize = 500
        passes = 20
        iterations = 400
        eval_every = 1

        # Make a index to word dictionary.
        temp = dictionary[0]  # only to "load" the dictionary.
        id2word = dictionary.id2token

        lda_model = LdaModel(corpus=corpus, id2word=id2word, chunksize=chunksize, \
                             alpha='auto', eta='auto', \
                             iterations=iterations, num_topics=num_topics, \
                             passes=passes, eval_every=eval_every)
        # Print the Keyword in the 5 topics
        print(lda_model.print_topics())

        # Compute Coherence Score using c_v
        coherence_model_lda = CoherenceModel(model=lda_model, texts=docs, dictionary=dictionary, coherence='c_v')
        coherence_lda = coherence_model_lda.get_coherence()
        print('\nCoherence Score: ', coherence_lda)

        # Compute Coherence Score using UMass
        coherence_model_lda = CoherenceModel(model=lda_model, texts=docs, dictionary=dictionary, coherence="u_mass")
        coherence_lda = coherence_model_lda.get_coherence()
        print('\nCoherence Score: ', coherence_lda)
        """
               Compute c_v coherence for various number of topics
    
               Parameters:
               ----------
               dictionary : Gensim dictionary
               corpus : Gensim corpus
               texts : List of input texts
               limit : Max num of topics
    
               Returns:
               -------
               model_list : List of LDA topic models
               coherence_values : Coherence values corresponding to the LDA model with respective number of topics
               """

        model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=corpus, texts=docs,
                                                                start=2,
                                                                limit=40, step=6)
        # Show graph
        import matplotlib.pyplot as plt

        limit = 40;
        start = 2;
        step = 6;
        x = range(start, limit, step)
        plt.plot(x, coherence_values)
        plt.xlabel("Num Topics")
        plt.ylabel("Coherence score")
        plt.legend(("coherence_values"), loc='best')
        plt.show()

        return coherence_lda

def get_coherance_user_wise(file_path, column_name_for_user_id, text_column_name):
    df = pd.read_csv(file_path)
    df = df.sort_values(column_name_for_user_id)
    user_data = []
    user_data.append(['UserId', 'coherance'])
    df_line = 0

    for index, row in df.iterrows():
        text=''
        if df_line == 0:
            previous_user = ''
            df_line += 1
        else:
            current_user = row[column_name_for_user_id]
            if previous_user == '' or previous_user == current_user:
                text += row[text_column_name]
                df_line += 1
            if df_line == len(df.index) or (previous_user != '' and previous_user != current_user):
                score=evaluate(text)
                user_data.append([previous_user, score])
                print('user = ', previous_user, ' => code count  = ', score)
                text=''
                df_line += 1
            previous_user = current_user

    with open('C:/Users/pc/Desktop/FYP data/test_results/coherance_results_user_wise.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in user_data:
            writer.writerow(row)
    csvFile.close()

    return user_data

file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/answer_posts.csv'
column_name_for_user_id='OwnerUserId'
count_type='answer_posts'
text_column_name='Body'
print('==========================================================================================')
data=get_coherance_user_wise(file_path_for_answer_posts, column_name_for_user_id,text_column_name)
print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_word_count_answer_posts',data)
print('**********************************   END   *******************************************')

