#import sys
#filename = sys.argv[0]

#f = open(filename, 'r') # opening file for reading
#for line in f: # for each line in file
#	print(line)
#f.close() # closing the file


import sys
filename = sys.argv[0]

f = open(filename, 'r') # opening file for reading
for line in f: # for each line in file
	print(line[::-1])
f.close() # closing the file