# -*- coding: utf-8 -*-
#remember this: get X from Y

#__init__有点像带参构造器，而self有点像this，与其他语言不同，
#Python需要将self作为参数显式传入，供函数调用，以告诉Python某个变量是实例的变量，而不是局部变量
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

#将list作为一个对象传入容易理解，但是怎么和lyrics变量联系上的呢？	
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()