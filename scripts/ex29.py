# -*- coding: utf-8 -*-
#pay attention to the ":" at the end of if-statement line!
#注意if条件句下一行有四个空格的缩进！不缩进会报错
people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."
