reasonCount = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data) != 2:
		continue
	thisKey, feedback = data
	
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, reasonCount)
		
		reasonCount = 0
	oldKey = thisKey
	reasonCount++	
		
	
if oldKey != None:
	print oldKey, "\t", reasonCount