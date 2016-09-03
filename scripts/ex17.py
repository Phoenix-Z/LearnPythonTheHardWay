# -#- coding: utf-8 -*-
from sys import argv
#exists是用来判断文件是否存在的，存在则返回True，否则返回False
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line,how? 这里就是想说明可以级联调用函数，但是没有中间变量，关闭操作将无法进行，据说是这样操作完之后Python会自动帮你关闭
in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read()

#可以使用len()来获取文件数据的长度，注意这里不是直接获取文件的长度，而是先获取文件中的数据，然后再判断数据的长度。
print "The input file is %d bytes long" % len(indata)

#正是因为上面进行了import操作，以下句子才可以直接使用exists方法，返回True或者False
print "Does the output file exists? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CRTL_C to abort."
#这句话可以让程序暂停，有想法的操作
raw_input()

#python 是严格区分大小写的，w和W是不一样的，需注意！
out_file = open(to_file, "w")
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
