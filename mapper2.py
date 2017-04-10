f = open("d.txt","r")           # open file, read-only
for line in f:  
    data = line.strip().split("    ") 
    print data
    print len(data)
    if len(data) == 6:
        date, time, store, item, cost, payment = data  #assign each entry to a variable
        print "{0}\t{1}".format(store, cost)
f.close()
