#装饰器：
#定义 本质是函数（装饰其他函数）就是为其他函数添加附加功能
#原则：1.不可修改被装饰的函数的源代码。
#      2.不能修改被装饰的函数的调用方式。（装饰器对于被修饰的装饰器是透明的，因为没有影响函数）
#实现装饰器的知识储备：
#1.函数即变量
#2.高阶函数
#   a:把一个函数名当做实参传给另外一个函数(在不修改源代码的情况下为其添加功能)
#   b：返回值中包含函数名（不修改函数的调用方式）
#3.嵌套函数
#高阶函数+嵌套函数=》嵌套函数
# import time
# def timmer(func):
#
#     def warpper(*args,**kwargs):
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('the func run time is %s'%(stop_time-start_time))
#     return warpper
# @timmer
# def test1():
#     time.sleep(3)
#     print('in the test1')
# test1()
#
# cale =lambda x:x*3#匿名函数
# print(cale(3))

#2.高阶函数
# import time
# def bar():
#     time.sleep(3)
#     print('in the bar')
# def test1(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print('the func run time is %s'%(stop_time-start_time))
#
# test1(bar)
# bar()


# import time
# def bar():
#     time.sleep(3)
#     print('sdfkka sdfja wo ksd fal dls fa')
# def test2(func):
#     print(func)
#     return func
# bar=test2(bar)
# bar()

#
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#
#     bar()
# foo()


import time
def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s' % (stop_time - start_time))
    return deco
#@timer  #相当于test1=timer(test1)
def test1():
    time.sleep(3)
    print('int the test1')
@timer #想在哪个函数上加上新功能就用这个
def test2(names,age):
    time.sleep(3)
    print('int the test2%s   %s'%(names,age))
test1()
test2('管新约是只猪一头','23')