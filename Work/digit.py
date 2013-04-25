import sys

args = sys.argv

try:
	print args[1]
	print args[1]*2
	print int(args[1])*2	

except IndexError:
	print "ERROR: You must insert second command in the command line. e.g. python digit.py 500 ."

