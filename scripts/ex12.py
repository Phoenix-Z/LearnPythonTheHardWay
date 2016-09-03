# -#- coding: utf-8 -*-

#可以在raw_input函数中直接传入字符串以提示用户输入，但是需注意传入的字符串和用户输入中间可能需要手动添加空格
age = raw_input("How old are you?      ")
height = raw_input("How tall are you?       ")
weight = raw_input("How much do you weight?       ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)