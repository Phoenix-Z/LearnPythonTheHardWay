# -*- coding: utf-8 -*-
#子类重写父类中的函数
class Parent(object):
	def override(self):
		print "PARENT override()"
		
class Child(Parent):
	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()