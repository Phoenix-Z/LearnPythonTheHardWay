# -#- coding: utf-8 -*-

#这是自己构造一个异常类的方式，可以看是它是继承Exception类，这与java很像
#但是抛出自定义的异常，需要使用raise关键字，而非throw
class ParserError(Exception):
	pass

class Sentence(object):
	
	def __init__(self, subject, verb, obj):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]
		
	def make_sentence(self):   
		#这个函数是将主谓宾连成一个句子，注意在类的内部定义函数，不要忘了传入self参数
		sen = [self.subject, self.verb, self.object]
		return " ".join(sen);

# peek函数是判断剩下的单词列表的首个单词是否合法，而不将该单词取出
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None
		
# match函数不仅判断首个单词是否合法，还将该单词取出
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None
	
# skip函数是用来跳过那些stop属性的单词的	
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

# 转换verb		
def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
		
	else:
		raise ParserError("Expected a verb next.")
		
# 转换object
def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		
# 转换subject
def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next.")
		
# 转换整个句子
def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
	sen = Sentence(subj, verb, obj)
	return sen.make_sentence()