def deco1(func):
    print('enter deco1')
    def wrap1(*args, **kwargs):
        print('enter wrap1') #里面的东西shi'zai
        result = func(*args, **kwargs)
        print('exit wrap1')
        return result
    print('exit deco1')
    return wrap1


def deco2(func):
    print('enter deco2')
    def wrap2(*args, **kwargs):
        print('enter wrap2')
        result = func(*args, **kwargs)
        print('exit wrap2')
        return result
    print('exit deco2')
    return wrap2


def deco3(func):
    print('enter deco3')
    def wrap3(*args, **kwargs):
        print('enter wrap3')
        result = func(*args, **kwargs)
        print('exit wrap3')
        return result
    print('exit deco3')
    return wrap3
#装饰过程1，2，3顺次往下去的
@deco1
@deco2
@deco3
def foo(x, y):
    '''this is foo'''
    print('---------EXEC foo----------')#原函数也加个打印 这里是真正执行我原来的函数
    return x ** y

print('---------define finished---------')


print('===============================================')

#装饰过程
def bar(x, y):
    '''this is bar'''
    print('---------EXEC bar----------')#原函数也加个打印 这里是真正执行我原来的函数
    return x ** y
#手动去走 装饰过程 小鱼被大鱼吃，大鱼被鲨鱼吃。。
wrap3 = deco3(bar) 
wrap2 = deco2(wrap3)
wrap1 = deco1(wrap2)
# 等价于
# wrap1 = deco1(deco2(deco3(bar)))

print('---------define finished---------')

#这里用的wrap1() bar和wrap1还不一样 我们还少重要一步
#print(wrap1(3,2))

# print(bar)
# print(wrap1)#此时这两个还不一样
bar = wrap1 
# print(bar)
# print(wrap1) #此时一样了
print(bar(3, 2)) #偷梁换柱

