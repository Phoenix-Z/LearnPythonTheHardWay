# -#- coding: utf-8 -*-
import re  #导入正则表达式，用于判断是否是数字

#将预留字以list形式保存，注意不要漏掉了双引号
directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stops = ["the", "in", "of", "form", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]

def scan(input):
	#保存结果的list
	sentence = []
	#先将输入的字符串分割
	words = input.split()
	
	for word in words:
		#使用临时变量将用户输入全部变成小写，这样便于比较
		#不直接将word变成小写，是为了保留用户输入，以便输出
		tmp = word.lower()
		if tmp in directions:    #用户输入是否为方向
			sentence.append(("direction", word))
		
		elif tmp in verbs:      #用户输入是否为动词
			sentence.append(("verb", word))
		
		elif tmp in stops:       #用户输入是否为介词
			sentence.append(("stop", word))
		
		elif tmp in nouns:     #用户输入是否为名词
			sentence.append(("noun", word))
		
		elif re.match('^[0-9]+$',word) != None:    #用户输入是否为数字
			sentence.append(("number", int(word)))
		
		else:         #错误的用户输入
			sentence.append(("error", word))
			
	return sentence