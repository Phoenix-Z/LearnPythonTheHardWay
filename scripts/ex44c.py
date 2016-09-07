# -*- coding: utf-8 -*-
#在子类中重写父类的某个方法，但又希望调用父类的那个方法，需使用super
class Parent(object):
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		#这里的super和java中的含义是一样的，但是需要注意传入的参数
		#既要传入子类名，又需要传入self
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()