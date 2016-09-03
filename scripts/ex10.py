# -#- coding: utf-8 -*-
tabby_cat = "\tI'm tabbbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#三个单引号跟三个双引号一样的效果
thin_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print "%r\n" % tabby_cat  #结果是："\tI'm tabbbed in."  记住：%r is for debugging, %s is for displaying
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print thin_cat

#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,