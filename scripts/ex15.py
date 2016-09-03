# -#- coding: utf-8 -*-
#sys是一个包，argv是这个包中的一个模块
from sys import argv
script,filename = argv

#使用open函数可以找到文件，并返回一个file对象给txt变量
txt = open(filename)

print "Here's your file %r:" % filename
#file.read([size])函数是读取文件内容，如果不写size，则一直读到文件末尾(EOF)，否则读入size字节的内容
#file对象调用read函数后文件指针不会回溯到文件头
print txt.read()
#读完文件就关闭文件对象是个好习惯
txt.close()
#python不会限制同一个文件被多次打开
txt2 = open(filename)
print txt2.read()
txt2.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()