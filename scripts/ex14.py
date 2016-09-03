# -#- coding: utf-8 -*-
from sys import argv

script,user_name = argv

promt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "i'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(promt)

print "Where do you live %s?" % user_name
lives = raw_input(promt)

print "What kind of computer do yo have?"
computer = raw_input(promt)

#注意以下这种写法！
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)