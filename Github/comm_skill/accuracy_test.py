from collections import Counter

from Github.comm_skill.spell_checker import correction, words, WORDS, P


def unit_tests():
    assert correction('speling') == 'spelling'  # insert
    assert correction('korrectud') == 'corrected'  # replace 2
    assert correction('bycycle') == 'bicycle'  # replace
    assert correction('inconvient') == 'inconvenient'  # insert 2
   # assert correction('arrainged') == 'arranged'  # delete
    assert correction('peotry') == 'poetry'  # transpose
    assert correction('peotryy') == 'poetry'  # transpose + delete
    assert correction('word') == 'word'  # known
    assert correction('quintessential') == 'quintessential'  # unknown
    assert words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(words('This is a test. 123; A TEST this is.')) == (
        Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))
    assert len(WORDS) == 32198
    assert sum(WORDS.values()) == 1115585
    assert WORDS.most_common(10) == [('the', 79809),
                                     ('of', 40024),
                                     ('and', 38312),
                                     ('to', 28765),
                                     ('in', 22023),
                                     ('a', 21124),
                                     ('that', 12512),
                                     ('he', 12401),
                                     ('was', 11410),
                                     ('it', 10681)]
    assert WORDS['the'] == 79809
    assert P('quintessential') == 0
    assert 0.07 < P('the') < 0.08
    return 'unit_tests pass'


def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.clock()

    good, unknown = 0, 0
    n = len(tests)
    for word, truth_value in tests:
        w = correction(word)
        print str(w)+ ','+str(truth_value)
        print w == bool(truth_value)
        good += (w == bool(truth_value))
        if w != bool(truth_value):
            print 'test if condition'
            unknown += (word not in WORDS)

    dt = time.clock() - start
    print n
    print good


    correct_percentage = float(good * 100) / float(n)
    unknown_percentage = float(unknown * 100 )/float(n)
    words_per_second = int(n / dt)
    print str(correct_percentage)+'% of '+str(n)+' correct ('+str(unknown_percentage)+'% unknown) at '+str(words_per_second)+' words per second'



def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    return [(word, truth_value)
            for (word, truth_value) in (line.split(':') for line in lines)]





def test_corpus(filename):
    print("Testing " + filename)
    spelltest(Testset(open(filename)))


#test_corpus('spell-testset1.txt')  # Development set
#test_corpus('spell-testset2.txt')  # Final test set

# Supplementary sets
#test_corpus('wikipedia.txt')
#test_corpus('aspell.txt')

test_corpus('readme_test_dataset')

# Long test, for the patient only
# test_corpus('birkbeck.txt')
