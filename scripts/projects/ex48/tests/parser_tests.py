# -#- coding: utf-8 -*-
from nose.tools import *
from ex48 import lexicon
from ex48.parser import *

def test_parse1():   #测试一个正好合适的句子
	result = lexicon.scan("bear go east")
	assert_equal(parse_sentence(result), "bear go east")
	
def test_parse2():     #测试是否将无用的单词去掉
	result = lexicon.scan("a bear go the east")
	assert_equal(parse_sentence(result), "bear go east")
	
def test_parse3():    #测试是否抛出异常
	result = lexicon.scan("a bear go to the east")
	#注意assert_raises()的用法，第一个参数是期望抛出的异常，第二个参数是希望测试的函数名
	#第三个及之后的所有参数是需要传入的参数
	assert_raises(ParserError, parse_sentence, result)