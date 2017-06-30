import os
import glob
import cPickle
from bs4 import BeautifulSoup as bs
try:
	os.remove("ReadData.pyc")
except:
	print "The file wasn't previously complied"

#Address 1 for News Data 
path = "C:\Project\STS\SourceCode\WordBased\Data\\2554\\2554\download\Texts\Data"
print path
os.chdir(path)
pathAllFiles = path + "\*"
FileNames = list(glob.glob(pathAllFiles))
print FileNames
allFiles = []
MoreNewFiles = []
for i in FileNames:
	pathAllFiles = i + "\*"
	MoreNewFiles += list(glob.glob(pathAllFiles))
for i in MoreNewFiles:
	pathAllFiles = i + "\*"
	allFiles += list(glob.glob(pathAllFiles))
print allFiles


homePath = "C:\Project\STS\SourceCode\WordBased\BigDatabase"

#To Stop Terminal Chaning its Address
os.chdir(homePath)

#print len(allFiles), allFiles[0]
#Parsing XML Files:
database = []
see = 0
for files in allFiles:
	see += 1
	print files
	f = open(files).read()
	f = bs(f, "lxml")
	#print "File Length", len(f)
	count = 0
	for text in f.findAll('s'):
		count += 1
		temp = []
		#if count >= 2: break	
		for word in text.findAll('w'):
			#print word.next.strip()
			if '/' in word['hw']:
				w1 = word['hw'].strip().split('/')
				for i in w1:
					temp.append(i)
			#if '-' in word['hw']:
			#	w1 = word['hw'].strip().split('-')
			#	for i in w1:
			#		temp.append(i)
			else: temp.append(word['hw'].strip())
		database.append(temp)
	print "Count ", count	
cPickle.dump(database, open('databaseD+E.txt', 'wb'))
print "Total No of Files read", see
del database[:]