import re
from collections import Counter

from Github.Github_Api import retrieve_readme


def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('Comments.xml').read()))
incorrect_word_list = []

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    corrected_word = max(candidates(word), key=P)
    if corrected_word != word:
       if corrected_word != 'a':
            incorrect_word_list.append(word)
            print 'incorrect word: '+word+', '+corrected_word
            return False

       else:
           print 'correct word: '+word
           return True
    else:
        print 'correct word: '+word
        return True




def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))



list, tw = retrieve_readme.words_list('salindalakmal')

if list:
    for word in list:
        correction(word.lower())

print 'Length of incorrect word list: '+str(len(incorrect_word_list))

# print correction('pylint')