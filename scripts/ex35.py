# -*- coding: utf-8 -*-

from sys import exit    #导入exit模块
import re				#导入正则表达式模块，注意这里不能有from sys

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	#注意以下写法，使用in关键字可以判断一个字符串中是否含有特定字符
#	if "0" in choice or "1" in choice:      #这个写的不好，因为限制了数字中必须有0或者1，而实际上并不是必须的
	if re.match("^[0-9]+$",choice) != None: #使用正则表达式可以有效的判别一个字符串是否只由数字组成
		how_much = int(choice)    #int()函数可以将字符串转为数字，可以转换纯数字，也可以转0x，0b这些不同进制的字符串
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		#exit函数：传入0表示正常退出程序，传入正整数表示异常退出，不同的数字表示不同的异常类型
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False   #注意在python中，True和False首字母都是大写的
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it , whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):  #注意这种写法，把相同的输出信息提取出来，有利于代码的复用性
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()
