# -#- coding: utf-8 -*-
#print 行后不加逗号，用户输入在下一行，否则在同一行接受输入
print "How old are you?"

#raw_input函数读入的是一个字符串，有时需要转换类型

#age = raw_input()
age = input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


#纯数字输入
#当输入为纯数字时
#input返回的是数值类型，如int,float
#raw_inpout返回的是字符串类型，string类型

#输入字符串为表达式
#input会计算在字符串中的数字表达式，而raw_input不会。
#如输入 “57 + 3”:
#input会得到整数60
#raw_input会得到字符串”57 + 3”