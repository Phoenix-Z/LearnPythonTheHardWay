# -#- coding: utf-8 -*-
#python中的函数：函数定义以def开头，在def同一行，写上函数名，形参列表
#注意：在def一行的末尾一定要加上":"
#函数体写在下面几行，注意函数体的每一行都要有四个空格！(即一个TAB键)，(这个叫做缩进(indent))
#函数体结束后的下一行一定要顶格写，以告诉Python函数定义已经结束了


#this one is like your scripts with argv
#形参前加上一个"*"，表示这个参数可以接受多个实参,(相当于把多个形参打包)，
#然后在函数体把包打开(unpack)，取出实参，一般情况下不需要这么做
def print_two(*args):
	arg1,arg2 = args	
	print "arg1: %r,arg2: %r" % (arg1,arg2)
	
#ok, that *args is actually pointless,we can just do this
#正常情况下，同其他一样即可
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)
	
#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this one takes no arguments
def print_none():
	print "I got nothing."

#以下是调用函数，注意传入相应的参数	
print_two("Zed","Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()