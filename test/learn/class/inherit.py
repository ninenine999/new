'''
Created on 2017年6月18日

@author: admin
'''
class Animal(object):
    def __init__(self,name='动物',color='白色'):
        self.name=name
        self.color=color
    def __del__(self):
        print('___________1______')
class Dog(Animal):
    #def __init__(self,name='狗',color='白色'):
        #self.__name=name
       # self.__color=color
   # def __del__(self):
      #  print('___________1______')
    def printInfo(self):
        print('名字是：%s'%self.name)
        print('名字是：%s'%self.color)

wangcai=Dog(name='旺财')  
wangcai.printInfo()     