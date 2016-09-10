# -#- coding: utf-8 -*-
from nose.tools import *
from bin.app2 import app
from tests.tools import assert_response

#web.py框架提供了如下的API来处理请求：
#app.request(localpart='/', method='GET', data=None, host='0.0.0.0:8080', headers=None, https=False)
#参数：1.请求的URL;2.请求方法;3.form表单数据;4.主机地址;5.报文头;6.是否使用SSL
#调用这个方法并没有真正启动服务器，而是模拟了一个请求，并试图获取响应

def test_index():
	# check that we get a 404 on the / URL
	resp = app.request("/")
	assert_response(resp, status = "404")
	
	# test our first GET request to /hello
	resp = app.request("/hello")
	assert_response(resp)
	
	#make sure default values work for the form 
	resp = app.request("/hello", method = "POST")
	assert_response(resp, contains = "Nobody")
	
	# test that we get expected values
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello", method = "POST", data = data)
	assert_response(resp, contains = "Zed")