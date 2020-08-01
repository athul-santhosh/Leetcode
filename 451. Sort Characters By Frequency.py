#Sort Characters By Frequency

from collections import Counter

def frequencySort(s):
	#print(Counter(s).most_common())
	string = "" 
	freq = Counter(s)
	print(freq)
	s = sorted(freq ,key = lambda x : freq[x] ,reverse = True)
	for k in s:
		string += k* freq[k]
	print(string)


				
	



print(frequencySort("Trbsfsdfrrgree"))






