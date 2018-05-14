# 定义一个装饰器，大于100的时候，返回-1
from functools import wraps
def check(func): 
	@wraps(func)
	def inner(x, y):  
		'''this is inner'''
		result = func(x, y)  
		if result > 100:  
			return -1
		return result  
	return inner


@check
def foo(x, y):
	'''this is foo'''
	return x ** y


print(foo.__doc__)

