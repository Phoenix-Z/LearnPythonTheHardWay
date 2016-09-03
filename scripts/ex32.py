# -*- coding: utf-8 -*-
#变量名 = [ele1, ele2, ....] 这在python 中叫做list，有点像数组，索引从0开始，
#可以使用for...in...:来遍历list。二维list：[[1,2,3],[4,5,6]]
#注意：list中不要求元素类型一致，可以放入任意类型的元素，因此与Java中的list较为类似，
#注意：它是可以放入相同元素的，所以它不是一个set
the_count = [1, 2, 2, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
#这里使用%r是因为，list中的元素类型不一致，不可以简单地使用%d，当然使用%s也没问题，
#不过看不出来原来list中类型不一样
for i in change:
	print "I got %r" % i

#以下是自己创建的list，而不是初始化而来的，首先用[]来告诉python这个变量表示的是list
#we can also build lists ,first start with an empty one 
elements  = []

#range函数用法:
#(1)range(stop)，range默认从0开始，因此range(4)返回的是[0,1,2,3],即[0,4)
#(2)range(start,stop),返回的是[start,stop),如下面的range(0,6)返回的就是[0, 1, 2, 3, 4, 5]
#(3)range(start,stop,step),依然返回的是[start,stop)，但是step表示的步长，即可以控制增长的幅度
#then use the range function to do 0 to 5 counts
#for i in range(0, 6, 2):
#	print "Adding %d to the list." % i
#	#append is a function that lists understand
#	elements.append(i)
elements.extend(range(0,6));      #这句话与上面的for-loop等效

#now we can print them out too
for i in elements:
	print "Elements was: %d" % i

#在python中，可以直接对对象(如list对象)进行操作的函数叫函数(function)，
#而对象可以调用的函数叫做方法(method)，即如list.append(obj)
#参考：http://www.tutorialspoint.com/python/python_lists.htm
#list中的函数和方法：
#1.函数：
#(1)len(list):获取list的长度
#(2)max(list):获取list中最大的元素
#(3)min(list):获取list中最小的元素
#2.方法：
#(1)list.append(obj):将一个元素添加到list的末尾
#(2)list.count(obj): 获取obj在list中出现的次数
#(3)list.extend(seq):将seq中的元素添加到list中
#(4)list.index(obj):返回obj在list第一次出现时的索引
#(5)list.insert(index, obj):将obj插入到index处
#(6)list.pop(obj = list[-1]):弹出list中的最后一个元素并返回
#(7)list.remove(obj):删除list中的obj
#(8)list.reverse():将list中的元素逆序
#(9)list.sort([func]):给list中的元素排序，可以传入一个排序的函数，以告诉python如何排序
