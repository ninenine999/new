'''
Created on 2017年6月1日

@author: admin
'''
from ctypes.test.test_pickling import name
names =['x','y','z','n']
for y in names:
    print(y)

x=0
for y in [1,2,3,4,5,6,7,8,9,10]:
    x=x+y
    print(x)
 
 
 
x=0
for y in range(101):
     x=x+y
     print(x)

  
x=0
n=99
while n>0:
   x=x+n
   n=n-2
   print(x) 


L = ['Bart', 'Lisa', 'Adam']
x=3
n=3
while n>0:
    x=x-1
    n=n-1
    print('hello '+L[x])
    
n=1
while n<100:
    if n>10:
        break
    print(n)
    n=n+1
    print('end')
 
 
n=0
while n<10:
     n=n+1
     print('test%s  '%n,end='') 

n=0
while n<10:
    n=n+1
    if n % 2==0:
        continue
    print(n)