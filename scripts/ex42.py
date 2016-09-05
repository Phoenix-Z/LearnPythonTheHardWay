# -*- coding: utf-8 -*-
## Animal is-a object (yes, sort of confusing) look at the extra credit
#注意object的首字母是小写的
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):
	
	def __init__(self, name):
		##Person has-a name
		self.name = name
		
		##Person has-a pet of some kind
		#这里是确保给Person类的pet对象赋上None的初始值
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		#Employee has-a name like a Person does
		#调用父类的__init__函数给子类的属性赋值，这和Java中的super()有点类似
		super(Employee, self).__init__(name)
		#Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a Fish
class Salmon(object):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()