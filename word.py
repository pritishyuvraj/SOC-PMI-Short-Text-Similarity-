import os
import math
import numpy as np 
import cPickle
import sys
import time
try:
	os.remove("word.pyc")
except:
	print "No duplicate file found"

#Loading Database and Dictionary
print "Loading Database ........."
start = time.time()
database = cPickle.load(open('databaseA.txt', 'rb'))
database += cPickle.load(open('databaseB.txt', 'rb'))
database += cPickle.load(open('databaseC.txt', 'rb'))
database += cPickle.load(open('databaseD+E.txt', 'rb'))
print "....Database Loaded..."
monoDic = cPickle.load(open('wordDictA+B+C+D+E.txt', 'rb'))
print "...Dictionary Loaded....."
print "Total time in loading.....", time.time() - start
def fpmi(word, dictionary, wordDict, m):
	for i in wordDict:
		wordDict[i].append(math.log(((wordDict[i][0] * m)/ (dictionary[i] * dictionary[word])), 2))
	return wordDict

def bothOccurence(word, database, alpha):
	Bigram = {}
	for i in database:
		if word in i:
			for j in xrange(len(i)):
				if i[j] == word:
					start = j - alpha
					if j-alpha < 0: start = 0
					end = j + 5
					if j+ alpha >= len(i): end = len(i) - 1
					for z in xrange(start, end+1):
						#print i[z]
						if i[z] == word: continue
						if i[z] not in Bigram:
							Bigram.setdefault(i[z], [])
							Bigram[i[z]].append(1.0)
						else:
							Bigram[i[z]][0] += 1
	return Bigram

def word_sim(word1 = "car", word2 = "automobile"):
	#data = open("Data.txt", "r")
	#database = []
	# m = 4004227
	# n = 73179
	m, n = 0.0, 0.0
	Beta, Gamma = 3, 3
	##From Sample Database
	#for i in data:
	#	i = i.strip().split()
	#	m += len(i)
	#	database.append(i)
	#print database 

	#From Actual Database
	#Count m
	#m += [len(row) for row in database]
	#sys.exit(0)
	global database
	global monoDic
	#monoDic = {}
	#for i in database:
	#	for j in i:
	#		m += 1
	#		if j not in monoDic:
	#			monoDic.setdefault(j, 1.0)
	#		else:
	#			monoDic[j] += 1
	#n = len(monoDic)
	#cPickle.dump(monoDic, open('wordDictA+B+C.txt', 'wb'))
	#print m, n
	
	m, n = 44476363, 373100 
	#sys.exit(0)
	#print monoDic
	if word1 in monoDic and word2 in monoDic:
		B1 = ((np.log(monoDic[word1]))**2) * ((math.log(n, 2))/Beta)
		B2 = ((np.log(monoDic[word2]))**2) * ((math.log(n, 2))/Beta)
		print B1, B2
	else:
		print "Words not found in the database"
		return 0
	alpha = 5
	BigramWord1 = bothOccurence(word1, database, alpha)
	#print word1, len(BigramWord1)
	BigramWord2 = bothOccurence(word2, database, alpha)
	#print word2, (BigramWord2)
	BigramWord1 = fpmi(word1, monoDic, BigramWord1, m)
	BigramWord2 = fpmi(word2, monoDic, BigramWord2, m)
	BigramWord1 = sorted(BigramWord1.items(), key=lambda e: e[1][1], reverse=True)
	BigramWord2 = sorted(BigramWord2.items(), key=lambda e: e[1][1], reverse=True)
	B1, B2 = int(math.floor(B1)), int(math.floor(B2))
	BigramWord1, BigramWord2 = dict(BigramWord1[0:B1]), dict(BigramWord2[0:B2])
	commonWords = []
	key1, key2 = BigramWord1.keys(), BigramWord2.keys()
	#print BigramWord1, BigramWord2
	CommonKeys = list(set(key1).intersection(key2))
	F1, F2 = 0, 0
	for i in CommonKeys:
		F1 += BigramWord2[i][1]**Gamma
		F2 += BigramWord1[i][1]**Gamma
	print CommonKeys
	try:
		Similarity = (F1 / float(len(BigramWord1))) + (F2 / float(len(BigramWord2)))
	except:
		return 0
	print Similarity
	if Similarity > 25:
		Similarity = 1
	else:
		Similarity = Similarity/25
	return Similarity
	