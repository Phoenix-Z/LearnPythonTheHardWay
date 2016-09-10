# -#- coding: utf-8 -*-
from nose.tools import *
import re

#这是一个自定义的函数，用来判断响应是否与预期的一样
def assert_response(resp, contains = None, matches = None, headers = None, status = "200"):

	assert status in resp.status, "Expexted response %r not in %r" % (status, resp.status)
	
	if status == "200":
		assert resp.data, "Response data is empty."
		
	if contains:
		assert contains in resp.data, "Response does not contain %r" % contains
		
	if matches:
		reg = re.compile(matches)
		assert reg.matches(resp.data), "Response does not match %r" % matches
		
	if headers:
		assert_equal(resp.headers,headers) 