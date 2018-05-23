import os,sys
import numpy as np
from util import *


def ngram_probs(filename='raw_sentences.txt'):
	"""calculate each bigram and trigram frequency"""
	cnt2, cnt3 = {}, {}
	n_cnt2 = 0
	n_cnt3 = 0
	with open(filename, 'r') as f:
		for line in f:
			sent = ' '.join(line.strip().split(' '))
			bow = tokenize2bow(sent)
			bow = to_lowercase(bow)
			
			for i in xrange(len(bow)):
				if i < len(bow)-1:
					# bigram count
					w1 = bow[i]
					w2 = bow[i+1]
					if (w1, w2) not in cnt2.keys():
						cnt2[(w1, w2)] = 1
					else:
						cnt2[(w1, w2)] += 1

				if i < len(bow)-2:
					# trigram count
					w1 = bow[i]
					w2 = bow[i+1]
					w3 = bow[i+2]
					if (w1, w2, w3) not in cnt3.keys():
						cnt3[(w1, w2, w3)] = 1
					else:
						cnt3[(w1, w2, w3)] += 1

	# normalize count to frequency
	for k,v in cnt2.iteritems():
		cnt2[k] = v / float(n_cnt2)
	for k,v in cnt3.iteritems():
		cnt3[k] = v / float(n_cnt3)

	return cnt2, cnt3


def prob3(bigram, cnt2, cnt3):
	"""
	Calculate log-prob of the next word,
	according to bigram, trigram probability
	"""
	prob = {}
	bigram_cnt = cnt2[bigram]
	for k in cnt3.keys():
		w1,w2,w3 = k
		if (w1, w2) == (bigram):
			prob[w3] = np.log(cnt3[(w1, w2, w3)] / cnt2[(w1, w2)])
	return prob


def predict_max(starting, cnt2, cnt3):
	"""automatically complete sentence given start"""
	


def predict_beam(bigram, beam_size, sent_len, cnt2, cnt3):
	pass


if __name__ == '__main__':

	test_file = 'raw_sentences.txt'