import rkxor
import sys
if len(sys.argv) > 3 :
	print "Too many arguments! used first arg as plaintext, second as key"
print rkxor.rkxor(sys.argv[1],sys.argv[2])
