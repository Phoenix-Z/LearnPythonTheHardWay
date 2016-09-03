# -#- coding: utf-8 -*-

#%r和%s的区别：%r输出时可以看出变量的数据类型，比如字符串输出时会带引号，而%s输出时则没有引号
#formatter = "%s %s %s %s"
formatter = "%r %r %r %r"  
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
#print formatter % ("我","爱","我","家")
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
#以下是最后一个的输出，很奇葩，有的使用了单引号，有的使用了双引号，据说是Python自己选择一种最有效的方式进行输出
#'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'