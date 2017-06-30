import os
try:
	os.remove("try1.pyc")
except:
	print "Duplicate Module doesn't exist"
	
def display(array, len1, len2, string1, string2):
	print list(string2)
	for i in xrange(1, len1+1):
		print string1[i-1], array[i]

def dynammicProg(string1="Pritish", string2="Yuvraj"):
	len1, len2 = len(string1), len(string2)
	string1, string2 = string1.lower(), string2.lower()
	array = [[0 for i in xrange(len2+1)] for j in xrange(len1+1)]
	for i in xrange(len1+1):
		for j in xrange(len2+1):
			if i==0 or j==0:
				array[i][j] = 0
				continue
			if string1[i-1] == string2[j-1]:
				array[i][j] = array[i-1][j-1] + 1
			else:
				array[i][j] = max(array[i-1][j], array[i][j-1])
	#print array
	#print "Printing"
	#display(array, len1, len2, string1, string2)
	return array[i][j]

def starting(string1="Pritish", string2="Pritieish"):
	if len(string2) > len(string1):
		string1, string2 = string2, string1
	count = 0
	string1, string2 = string1.lower(), string2.lower()
	for i in xrange(len(string2)):
		if string1[i] == string2[i]:
			count += 1
	return count

def maxCommon(string1="Pritish", string2="Yuvraj"):
	if len(string2) > len(string1):
		string1, string2 = string2, string1
	string1, string2 = string1.lower(), string2.lower()
	count, i, j = 0, 0, 0
	maxi = 0
	while(count<len(string2)):
		j = count
		#print "Loop1", i, j
		while i<len(string1) and j<len(string2):
			#print "Loop2", i, j, string1[i], string2[j], string1, string2
			if string1[i]!=string2[j]:
				i += 1
				continue
			else:
				temp = 0
				while(string1[i]==string2[j]):
					#print "Loop3", i, j, string1[i]
					i += 1
					j += 1
					temp += 1		
					if i>=len(string1) or j>=len(string2):
						break
				if temp > maxi: 
					maxi = temp
				if i>=len(string1) or j>=len(string2):
					break
		count += 1
		#print "Count", count
	#print "Common", maxi
	return maxi

def calling(string1 = "place", string2="land"):
	LCS = dynammicProg(string1, string2)
	#print LCS, float(LCS**2), float(len(string1)),float(len(string2))
	V1 = float(LCS**2) / (float(len(string1)) * float(len(string2)) )

	start = starting(string1, string2)
	#print start
	V2 = float(start)**2 / (float(len(string1))* float(len(string2)))

	nmax = maxCommon(string1, string2)
	#print nmax
	V3 = float(nmax)**2 / (float(len(string1))*float(len(string2)))
	#print V1, V2, V3
	alpha = 0.33 * (V1 + V2 + V3)
	#print alpha
	return alpha
#calling()