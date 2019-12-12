# # #生成器
# # def fib(max):
# #     n = 0
# #     a = 0
# #     b = 1
# #     while n<max:
# #         yield  b
# #         #print(b)
# #         a = b
# #         b=b+a
# #         n=n+1
# #     return 'done'
# # f=fib(100)
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
#
#
#
# #生成器
# def fib(max):
#     (n,a,b)=(0,0,1)
#     while n<max:
#         yield  b
#         #print(b)
#         (a,b)=(b,a+b)
#         n=n+1
#     return 'done'
# f=fib(10)
# while True:
#     try:
#         x=next(f)
#         print('f:',x)
#     except StopIteration as e:
#         print('genwiooe fka o',e.value)
#         break
#
#
#
#
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")