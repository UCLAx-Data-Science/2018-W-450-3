#!/usr/bin/python
import cPickle as pickle
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import sys

sys.stderr.write("Started mapper.\n");

def word_feats(words):
    return dict([(word, True) for word in words])

def subj(subjLine, term):
    subjgen = subjLine.lower()
    if subjgen.find(term) != -1:
        subject = term
        return subject
    else:
        subject = "No match"
        return subject

def main(argv, term):
    classifier = pickle.load(open("classifier.p", "rb"))
    for line in sys.stdin:
        tolk_posset = word_tokenize(line.rstrip())
        d = word_feats(tolk_posset)
        subjectFull = subj(line, term)
        if subjectFull == "No match":
            print "LongValueSum:" + " " + subjectFull + ": " + "\t" + "1"
        else:
            print "LongValueSum:" + " " + subjectFull + ": " + classifier.classify(d) + "\t" + "1"

if __name__ == "__main__":
    search_term = "UCLA"
    main(sys.argv, search_term)