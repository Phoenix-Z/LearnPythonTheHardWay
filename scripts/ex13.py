# -#- coding: utf-8 -*-
#import关键字是将python模块(modules)集的模块导入到当前脚本文件中(模块类似于库)
#argv(arguments variable)接受用户在运行脚本时传入的参数,命令行参数在读入时也是以字符串的形式读入的
from sys import argv

#下面这行就是将运行脚本时需要传入的参数绑定到变量上
#"unpacks" argv
script,first,second,third = argv
#script是指脚本文件，即当前文件
print "The script is called:", script
#第一个参数
print "Your first variable is:", first
print "Do you want it?",
flag = raw_input()
#第二个参数
print "Your second variable is:", second
#第三个参数
print "Your third variable is:", third

#运行的命令行：(运行时只能正好传入四个参数，不能多也不能少)
#python ex13.py first 2nd 3rd

#运行的结果：
#The script is called: ex13.py
#Your first variable is: first
#Your second variable is: 2nd
#Your third variable is: 3rd