import re
 
NON_WORDS = re.compile("[^a-z0-9' ]")
 
# stop words pulled from the below url
# http://www.textfixer.com/resources/common-english-words.txt
STOP_WORDS = set('''a able about across after all almost also am
among an and any are as at be because been but by can cannot
could dear did do does either else ever every for from get got
had has have he her hers him his how however i if in into is it
its just least let like likely may me might most must my neither
no nor not of off often on only or other our own rather said say
says she should since so some than that the their them then
there these they this tis to too twas us wants was we were what
when where which while who whom why will with would yet you
your'''.split())
 
def get_index_keys(content, add=True):
    # Very simple word-based parser.  We skip stop words and
    # single character words.
    words = NON_WORDS.sub(' ', content.lower()).split()
    words = [word.strip("'") for word in words]
    words = [word for word in words
                if word not in STOP_WORDS and len(word) > 1]
    # Apply the Porter Stemmer here if you would like that
    # functionality.
 
    # Apply the Metaphone/Double Metaphone algorithm by itself,
    # or after the Porter Stemmer.
 
    if not add:
        return words
 
    # Calculate the TF portion of TF/IDF.
    counts = collections.defaultdict(float)
    for word in words:
        counts[word] += 1
    wordcount = len(words)
    tf = dict((word, count / wordcount)
                for word, count in counts.iteritems())
    return tf