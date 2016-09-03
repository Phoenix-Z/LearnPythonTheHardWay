# -#- coding: utf-8 -*-

#Here's some new strange stuff, remember type it exactly

#以下定义了两个字符串变量
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#直接引用以上两个变量
print "Here's are the days: ", days
#下面这行，可以看到在结果中，换行符并没有正常输出，这就是%r的作用：原样输出（程序员怎么写，它就怎么输出，可能引号不一样）
print "a new line: %r" % "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#这种方式是可以正常输出换行符的
print "Here are the months: ", months

#一对三个双引号括起来的范围可以输入任意长的字符串，输出时就是输入的原样输出
#三个引号必须连写，不可有空格！
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
