# -*- coding: utf-8 -*-
#这是自动化测试文件，与JUnit4一样，可以在同一个文件中测试多个函数
#这个文件的命名是：**_tsets.py，并且需要放在tests目录下，否则nosetests不会运行它
#最好对每一个模块生成一个测试文件，不要混在一起
from nose.tools import *     #导入nose的相关测试工具
from ex47.game import Room  #导入需要测试的模块或者class

#与Junit4一样，测试文件由若干个函数构成，函数命名有要求：
#以"test_"开头，这与JUnit4中在方法上加上@Test注解是一个道理
#但是和在JUnit中一样，也可以写一些帮助函数，来移除冗余代码
def test_room():
	gold = Room("GoldRoom", 
				"""This room has gold in it you can grab. There's a
				door to the north.""")
	#这里的assert_equal函数是测试的关键，可以看出它也使用了断言机制
	#用以判断中间变量或结果是否与想象的一致
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
	
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)
	
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)