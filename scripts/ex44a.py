# -*- coding: utf-8 -*-
#子类继承父类的所有函数
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
		
class Child(Parent):
#The use of pass under class Child: is how you tell Python that you want an empty block. 
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()