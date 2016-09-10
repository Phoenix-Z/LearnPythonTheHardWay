# -#- coding: utf-8 -*-
import web

#urls使响应请求的，比如通过浏览器访问根目录"/"，则跳转至Index这个类来处理请求
#urls = ('/', 'Index')
urls = ('/hello', 'Index')

app = web.application(urls, globals())

# render变量是获取模板所在的目录
render = web.template.render('templates/', base = "layout")

class Index(object):
	def GET(self):
		form = web.input(greet = "Hello", name = "Nobody")
		greeting = "%s, %s!" % (form.greet, form.name)
		return render.index(greeting = greeting)
		#render.后面接的是html模板的名字，即选用index.html还是foo.html作为模板
		#variable是在html中声明的，需要传入的参数
#		return render.foo(variable = greeting)
		
if __name__ == "__main__":
	app.run()
