'''
Created on 2017年6月7日

@author: admin
'''
from test.pickletester import MyList

    

def printme(str):
    '打印任何传入的字符串'
    print(str);
    return;
printme('我要调用用户自定义函数')

def changeint(a):
    a=10
b=2
changeint(b)
print(b)



#!/usr/bin/python
# Filename: func_param.py
def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')
printMax(3, 4) # directly give literal values
x=5
y=3
print(x,y)

def func(x):    #局部变量
    print('x is ',x)
    x=2
    print('changed local to',x)
x=50
func(x)
print('x is still ',x)


def func1():        #全局变量
    global x
    print('x is',x)
    print('changed localx to ',x)
x=50
func1()
print('value of x is',x)


def say(message,time=1):   #默认参数
    print(message*time)
say('hello')
say('world',5)


    


