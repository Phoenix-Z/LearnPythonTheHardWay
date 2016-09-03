# -*- coding: utf-8 -*-
#elif等价于else if
#注意：在python中，只要是出现了":"(引号),那么就是告诉python下一行开始就是一个块,
#因此下一行必须缩进4个空格，直到出现了不缩进的行，表示块结束了。
people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
