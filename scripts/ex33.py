# -*- coding: utf-8 -*-
numbers = []
def getNumbers(len, inc):
	for i in range(0, len, inc):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
#	i = 0
#	while i < len:
#		print "At the top i is %d" % i
#		numbers.append(i)
#		i = i + inc
#		print "Numbers now: ", numbers
#		print "At the bottom i is %d" % i

getNumbers(10, 2)
print "The numbers: "

for num in numbers:
	print num