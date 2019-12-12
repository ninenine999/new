'''
Created on 2017年6月20日

@author: admin
'''
class Animal(object):
    def __init__(self,name='动物',color='白色'):
        self.name=name
        self.color=color
class Horse(Animal):
    horserNum=0
    def __init__(self,name,color):
        super().__init__(name, color)
        self.setHorseNum()
    @classmethod
    def setHorseNum(cls):
        cls.horserNum+=1
bailongma=Horse("白龙马",'枣红色')
#bailongma.horserNum+=1

print(bailongma.name)
print(bailongma.color)
print(bailongma.horserNum)

chituma=Horse('赤免马','棕色')
#Horse.horserNum+=1
print(chituma.name)
print(chituma.color)
print(chituma.horserNum)
