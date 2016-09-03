# -#- coding: utf-8 -*-
#file对象具有的操作：：
#close -- Closes the file. Like File->Save.. in your editor.
#read -- Reads the contents of the file. You can assign the result to a variable.
#readline -- Reads just one line of a text file.
#truncate -- Empties the file. Watch out if you care about the file.
#write('stuff') -- Writes "stuff" to the file.write takes a parameter of a string you want to write to the file

from sys import argv
script,filename = argv

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

#truncate是清空文件内容，在写模式下，无需先truncate，因为python会自动truncate
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#注意占位符的位置，一定是在write内部，不要写在外部！
target.write("%s\n%s\n%s" % (line1,line2,line3))
print "And finally, we close it."
target.close()