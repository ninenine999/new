'''
Created on 2017年6月19日

@author: admin
'''
class Animail(object):
    def test1(self):
        self.a=10
        self.__b=11
class Dog(Animail):
    pass
aa=Animail()
aa.test1()