# -#- coding: utf-8 -*-
from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

#python -m pydoc file.seek
#file.seek函数是用来移动文件指针的，原型是这样的：file.seek = seek(offset[,whence])whence的取值只有三种
#0：移动文件指针从文件开头开始移动，offset应该大于等于0，whence默认为0
#所以f.seek(0)中,offset = 0，whence = 0(默认值)
#1：移动文件指针从当前位置开始移动，offset可以是正或者负
#2:	移动文件指针从文件末尾开始移动，offset应该是负数
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
#	print line_count, f.seek(line_count - 1,0).readline()  这句是不对的，因为seek处理的是字节，而不是一行
#Inside readline() is code that scans each byte of the file until it finds a \n character, 
#then stops reading the file to return what it found so far. The file f is responsible for maintaining 
#the current position in the file after each readline() call, so that it will keep reading each line.
	print line_count, f.readline(),
#注意：readline函数会自动返回一个换行，所以输出会多出若干换行，只要加上一个逗号就可以避免输出多余的换行	

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three line:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)