# -*- coding: utf-8 -*-
#这是讲上述三种子类与父类之间交互方式的综合
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
		
	def override(self):
		print "PARENT override()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		#这里使用super传入的参数，并没有提供父类的信息，Python会使用特定算法(MRO)帮我们找到需要使用的函数
		#试想如果Child多重继承自多个类，而这些类有可能都会有altered函数，那么将调用哪个父类中的函数呢？
		#所以虽然Python支持多重继承，但是在实际开发中最好尽量避免使用。
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


#super()函数更多地使用在__init__函数中，即调用父类的构造函数，以下是个例子
#class Child(Parent):

 #   def __init__(self, stuff):
 #       self.stuff = stuff
 #       super(Child, self).__init__()