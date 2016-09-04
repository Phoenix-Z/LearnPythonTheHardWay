# -*- coding: utf-8 -*-
#这个练习用于学习Python中的dict(字典),它是一个存储键值对的存储结构，定义方式有点像JavaScript中的对象

# create a mapping of state to abbreviation
# Python中字典的定义：{键名:值，...键名:值}
# 注意字典中的元素是无序的，即遍历整个字典得到的顺序，未必与创建时的顺序一样
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'Califonia': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
# 可以在字典定义之外添加新的元素，这与JavaScript中添加对象的属性是一样的,但是Python中字典允许键名是数字！
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 删除一个元素，del关键字同样适用于list，即可以使用del删除list中的元素
# del cities['OR']

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states 
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state 
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


#Python字典常用的函数和方法：
#1.函数：
#(1)len(dict): 计算字典元素个数，即键的总数
#(2)str(dict): 将这个字典打印出来，包括一对大括号
#2.方法：
#(1)dict.clear(): 删除字典内的所有元素
#(2)dict.copy(): 返回一个字典的浅拷贝
#(3)dict.get(key, default = None): 获取键对应的值，如果值不再字典中返回default值
#	注意：如果只传入键名，default值就为None，所以在上面的程序中，使用了not state进行判断
#(4)dict.has_key(key): 如果键在字典中返回True,否则返回False
#(5)dict.keys(): 以列表返回一个字典所有的键
#(6)dict.values(): 以列表返回一个字典所有的值
#(7)dict.items(): 以列表返回一个字典所有的键值对

