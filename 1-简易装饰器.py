# 定义一个装饰器，大于100的时候，返回-1
def check(func): 

	'''检查被装饰函数的结果，当结果大于100，直接返回-1'''
	def inner(x, y):  
		# print(func.__name__)
		# print(x, y)
		result = func(x, y)  #调用原来的函数，返回一个结果
		if result > 100:  #结果大于100，返回-1
			return -1
		return result  #小于100，返回原函数的返回结果
	return inner


@check
def foo(x, y):
	return x ** y


print(foo(10,3))
print(foo(5,3))
print(foo(3,3))