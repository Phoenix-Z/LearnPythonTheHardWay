# -*- coding: utf-8 -*-
# have to go over again!
import random 	#导入产生随机数的模块
from urllib import urlopen    #从urllib库中导入urlopen模块，可以从给定网址下载文件
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []         # WORDS是一个list

PHRASES = {   # PHRASES是一个dict
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# load up the words from the website
#从给定的网址获取信息
for word in urlopen(WORD_URL).readlines():
#字符串的strip()方法：移除字符串头尾指定的字符（默认为空格），这与java中trim()方法很像
	WORDS.append(word.strip())

#print WORDS
	
def convert(snippet, phrase):
#字符串的capitalize()方法：将字符串的第一个字母变成大写,其他字母变小写。
	class_names = [w.capitalize() for w in
	#随机生成WORDS列表的一个子列表，元素个数与snippet中"%%%"的个数相同
					random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		#随机产生一个1到3的数字表示参数个数
		param_count = random.randint(1, 3)
		param_names.append(", ".join(random.sample(WORDS,param_count)))
	
	for sentence in snippet, phrase:
		#这是python中用来复制列表的一种方式。这里使用了列表的分割切片语法[:]，得到列表从第一个到最后一个元素的切片
		result = sentence[:]
		
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
		
	return results
	
#keep going until they hit CTRL-D
try:
	while True:
		# snippets获取的是PHRASES中的keys，这表示需要替换的pattern
		snippets = PHRASES.keys()
		#shuffle表示混排，就是用来打乱顺序的
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			#print question, answer
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print question
			
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
			
except EOFError:
	print "\nBye"
		
					
					
