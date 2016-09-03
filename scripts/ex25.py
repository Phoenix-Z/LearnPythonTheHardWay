# -*- coding: utf-8 -*-

#分解字符串方法
def break_words(stuff):
#注意此处一对"""之间的文字是用来描述函数的作用的，会在help(ex25)或者help(break_words)中显示
#这就是文档注释，与java中的/**...*/是一个意思
    """This function will break up words for us."""
#使用split函数将字符串分割
    words = stuff.split(' ')
    return words

#给单词按字典顺序进行排序，使用sorted()函数
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#打印单词数组的第一个，注意这里使用的是pop操作，也就是说每pop一下，第一个单词就会出栈(被删除)
def print_first_word(words):
    """Prints the first word after popping it off."""
#注意pop操作传入的参数是0，表示的是第一个元素
    word = words.pop(0)
    print word

#打印单词数组中的最后一个元素，与上一个函数类似，需要注意pop操作传入的参数是-1，表示出栈的是最后一个元素
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted (sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


#使用python解释器与其进行交互
#输入python进入交互界面
#导入ex25.py模块：import ex25(即 import 文件名（不加后缀名）)
#除了以上导入的方法，还可以使用from ex25 import *,表示从ex25模块中导入所有的东西
#这个可以类比java 的导入与静态导入的区别
#当不清楚某个模块的作用，或者有哪些函数时，可以使用help(模块名)
#当不清楚某个模块的某个函数的作用时，可以使用help(模块名.函数名)
