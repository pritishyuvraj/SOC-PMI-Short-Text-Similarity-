from nltk.corpus import wordnet

def returnWordSim(word1, word2):
	word1 = wordnet.synsets(word1)
	word2 = wordnet.synsets(word2)
	if word1 and word2:
		ans = word1[0].wup_similarity(word2[0])
		if ans == None:
			ans = 0.0
		return ans
	else: 
		return 0.0