'''
Created on 2017年6月11日

@author: admin
'''
from _operator import index
from ctypes.test.test_pickling import name

name='abcdefhncdseesss'
print(name[::])
print(name[::-1])

print(name.find('c',1,20))#查找c在列表中的位置
print(name.rfind('c',1,20))#从右边开始查找c在列表中的位置

print(name.index('c'))#查找c在列表中的位置
print(name.rindex('c'))#从右边开始查找c在列表中的位置
#find与index的区别，find只能找单个值 ，index可以找串查找失败只会报-1，而index查找失败会异常
a=name.index('c')
print(name[name.index('c')+1::2])

a=[123,32,211]
print(len(a))
print(len(a))


b=[1,5]
b[2:]=[2,3,4]#指定位置增加数据
b.insert(2, (4,5,6))
print(b)
c=[1,2,4]
c.append(5)#追加，只有追加单个，，直接修改原列表，不是返回一个修改过的新列表
print(c)
a=[1,2,3]
b=[4,5]
a.extend(b)#可以追加多个值 
print(a)


b[1:2]=[]#删除指定数据
print(b)
print(b.pop())#移除该值，并有返回该值,后面开始删除
print(b)
x=[1,2,3,4,5,6,2,4,6,7,2,9]
x.remove(2)
print(x)#移除，也只移除第一个




x=[[1,2],1,2,1,[1,2,[2,4]]]#统计出现的次数
print(x.count([1,2]))
x.reverse()#反向存值
print(x)

y=[5,3,9,1,64,12,54,22]
y.sort()
print(y)

y=[5,3,9,1,64,12,54,22]
y.sort(reverse=True)
print(y)

y=['sss','ss','dw','3331','eee']
y.sort(key=len, reverse=False)#key是排序方式，reverse是倒序
print(y)


#判断文件后缀
name=input('请输入abc.txt')
print(name.endswith('.txt'))

#判断文件前缀
name1='sdf skk skkl dyuiw fs skf '
print(name1.startswith('sdf'))