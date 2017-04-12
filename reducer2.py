reasonCount = 0
oldKey = None
#opening both input file and output files
f = open("moutput2.txt","r")
o = open("r2output.txt","w")
lines = f.readlines()
#Sorting mapper output
lines.sort()
for line in lines:
	data = line.strip().split("\t")
	
	if len(data) != 2:
		continue
	thisKey, feedback = data
	
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, reasonCount)
		o.write("{0}\t{1}\n".format(oldKey,reasonCount)) 
		reasonCount = 0
	oldKey = thisKey
	reasonCount+=1	
		
	
if oldKey != None:
	print oldKey, "\t", reasonCount
        o.write("{0}\t{1}\n".format(oldKey,reasonCount)) 
 
#Closing input and output files
f.close()
o.close()
