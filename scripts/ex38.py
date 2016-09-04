# -*- coding: utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#同大多数语言一样，Python中的字符串也有split方法，用于将字符串拆分，并返回一个list对象
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	#注意pop操作是从list的结尾删除元素并返回给当前变量
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]   #list中的索引是从0开始的，因此索引为1是指向list中的第二个元素
print stuff[-2]  #Python中使用负数从后往前遍历list，如-1表示的是list中最后一个元素，而-2表示倒数第二个元素
print stuff.pop()
print ' '.join(stuff) #与JavaScript一样，Python也有join方法，将一组元素组合成一个字符串，但是与JavaScript中的使用顺序不同
print '#'.join(stuff[3:5]) #list[i:j]表示获取的是[i,j)的元素，即不包括j对应索引的元素