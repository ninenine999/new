# import time
# def logger():
#     time_format='%Y-%m-%d %x'
#     time_current=time.strftime(time_format)
#     with open('a.txt','a+') as f:
#         f.write('%s    end action\n'%time_current)
# def test1():
#     print('in the test1')
#     logger()
# def test2():
#     print('in the test2')
#     logger()
# def test3():
#     print('in the test3')
#     logger()
# test1()
# test2()
# test3()

# def test1(x,*args):
#     print(x)
#     print(args)
# test1(1,42,2,4,21,41)#传不固定的参数

def test(**kwargs):
    print(kwargs)
#把n个关键字参数，转换成字典

def test3(name,**kwargs):
    print(name)
    print(kwargs)

