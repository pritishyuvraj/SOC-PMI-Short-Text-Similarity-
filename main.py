import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

import wordSim
import try1
#import word as wd 
import wn3
#S1 = raw_input("")
#S2 = raw_input("")
S1 = "A cemetry is a place where dead people's bodies or their ashes are buried."
S2 = "A graveyard is an area of land, sometimes near a church, where dead people are buried."
#S1 = "The president was assinated in his car"
#S2 = "The president was assinated and driver could do nothing"
#S1 = "The minor was raped inside a car, people stood and did nothing"
#S2 = "The girl was raped by the driver and people did nothing"
#S2 = "Cricket match was being played between two decisive teams"
#S1, S2 = S1.strip().split(), S2.strip().split()
tokenizer = RegexpTokenizer(r'\w+')
S1 = tokenizer.tokenize(S1)
S2 = tokenizer.tokenize(S2)

#ps = PorterStemmer()
#S1 = [ps.stem(word.lower()) for word in S1]
#S2 = [ps.stem(word.lower()) for word in S2]
ltz = WordNetLemmatizer()
S1 = [ltz.lemmatize(word.lower()) for word in S1]
S2 = [ltz.lemmatize(word.lower()) for word in S2]

#print S1, S2
'''
tokenizer = RegexpTokenizer(r'\w+')
S1 = tokenizer.tokenize(S1)
S2 = tokenizer.tokenize(S2)
'''
S1_filtered = [word for word in S1 if word not in stopwords.words('english')]
S2_filtered = [word for word in S2 if word not in stopwords.words('english')]
print S1, S2
#print S1_filtered, S2_filtered
#End of Step 1
#print stopwords.words('english')

#Start of Step 2
score, common = wordSim.wordSim(S1_filtered, S2_filtered)
S1_next = [word for word in S1_filtered if word not in common]
S2_next = [word for word in S2_filtered if word not in common]
print "Common", common 
print "Paragraph", S1_next, S2_next
h, w = len(S1_next), len(S2_next)
Matrix1 = [[0.0 for x in xrange(w)] for x in xrange(h)]
print S2_next
for i in xrange(len(Matrix1)):
	print S1_next[i], Matrix1[i]
for i in xrange(len(S1_next)):
	for j in xrange(len(S2_next)):
		Matrix1[i][j] = try1.calling(S1_next[i], S2_next[j])
print S2_next
for i in xrange(len(Matrix1)):
	print S1_next[i], Matrix1[i]
#End of Step 3

#Begining of Step 4
Matrix2 = [[0.0 for x in range(w)] for x in range(h)]
print "SOCPMI"
for i in xrange(len(S1_next)):
	for j in xrange(len(S2_next)):
		Matrix2[i][j] = wn3.returnWordSim(S1_next[i], S2_next[j])
print S2_next
for i in xrange(len(Matrix2)):
	print S1_next[i], Matrix2[i]
#End of Step 4

#Begining of Step 5
Matrix = [[0.0 for x in xrange(w)] for x in xrange(h)]
print "Final Matrix"
for i in xrange(len(S1_next)):
	for j in xrange(len(S2_next)):
		Matrix[i][j] = (0.5*Matrix1[i][j]) + (0.5*Matrix2[i][j])
print S2_next
for i in xrange(len(Matrix)):
	print S1_next[i], Matrix[i]
#Looping to find Pi
def delete(matrix, i, j):
	for row in matrix:
		del row[j]
	matrix = [matrix[i1] for i1 in xrange(len(matrix)) if i1 != i]
	return matrix
Pi = []
while(len(Matrix)>0 and len(Matrix[i])>0):
	#Search for maximum Element
	maxelement = 0
	maxi, maxj = 0, 0
	for i in xrange(len(Matrix)):
		for j in xrange(len(Matrix[i])):
			if Matrix[i][j] > maxelement:
				maxelement = Matrix[i][j]
				maxi = i
				maxj = j
	Pi.append(Matrix[maxi][maxj])
	Matrix = delete(Matrix, maxi, maxj)
	print "Matrix"
	for i in xrange(len(Matrix)):
		print Matrix[i]
	print "Pi", Pi

#End of Step 5

#Begining of Step 6
Delta = 2.0
similarity = ((Delta + sum(Pi)) * (len(S1_next) + len(S2_next)))/(2*len(S1_next)*len(S2_next))
print "Similarity Score", similarity