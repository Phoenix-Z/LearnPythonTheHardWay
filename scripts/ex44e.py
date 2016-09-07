# -*- coding: utf-8 -*-
#在一个类的内部定义另一个类的对象，然后在这个类的内部调用其他类的函数和方法
class Other(object):
	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"
		
class Child(object):
	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"
		
son = Child()

son.implicit()
son.override()
son.altered()

