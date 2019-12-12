'''
Created on 2017年6月18日

@author: admin
'''
from ctypes.test.test_pickling import name
from _hashlib import new
from test.support import _MemoryWatchdog
class Person(object):
    def __init__(self, name, age):
        self.__name=name#私有属性
        self.__age=age
        self.high=180#公有属性
    def __str__(self):
        return "年龄为："+str(self.__age)
    def setNewAge(self,newAge):
        if newAge>0 and newAge<80:
            self.__age=newAge
        else :
            print('输入错误请重新输入')
    def getAge(self):
        return self.__age
    def __del__(self):#系统要结束是做的时
        print('输入完成')
xiaoming=Person('小明',18)
print('_________1_________')
xiaoming1=xiaoming
xiaoming2=xiaoming
print(xiaoming)
print(xiaoming1)
print(xiaoming2)

print('_________2_________')
del xiaoming
del xiaoming1
del xiaoming2#引用计数，如果对象删除完了之后，那么就直接kill掉
print('_________3_________')

#虽然没有调用__del__方法，那是谁调用的呢？
#python解释器，如果检测到一个对象没有任何用处 了，那么就把这个对象kill掉的
