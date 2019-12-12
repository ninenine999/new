'''
Created on 2017年6月12日

@author: admin
'''

#global全局变量
def printLin(m):
    for i in range(0,m):
        print("-"*1)
        i=i+1
n=int(input('请输入打印个数：'))
printLin(n)

def add3Sum(a,b,c):
    sum1=a+b+c
    return sum1
def add3avg(a,b,c):
    y=add3Sum(a, b, c)
    x=y/3
    print(x)
add3avg(1, 3, 5)
