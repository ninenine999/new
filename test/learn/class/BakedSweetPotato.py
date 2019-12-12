'''
Created on 2017年6月15日

@author: admin
'''
#烤地瓜
#1.熟了没？0-3生，超过3半生不熟、超过5熟了、超过8烤焦了cookedLevel
#2.表示烤熟状态cookedString
#3.地瓜原料：condiments

class BakedSweetPotato:
    def __init__(self):
        self.cookedLevel=0
        self.cookedString='生的'
        self.condiments=[]
    def __str__(self):
        msg1='您的地瓜已经处于'+ self.cookedString +'的状态'
        if len(self.condiments)>0:
            msg1+='已添加辅料'
            for temp in self.condiments:
                msg1=msg1+temp+','
            msg1.strip(',')
        return msg1
    def cook(self,time):
        self.cookedLevel+=time
        if self.cookedLevel<3:#错在没有加self，，这个是需要带上类是哪一个然后才能取值
           self.cookedString='生的'
        elif self.cookedLevel<5:
           self.cookedString='半生不熟'
        elif self.cookedLevel<8:
           self.cookedString='熟的'
        else:
           self.cookedString='烤焦了'
    def add(self,temp):
        self.condiments.append(temp)
Potato=BakedSweetPotato()
print(Potato.cookedString)
print(Potato.condiments)
print(Potato.cookedLevel)
Potato.cook(4)
print(Potato.cookedLevel)
Potato.cook(2)
print(Potato)
Potato.add('蕃茄酱')
print(len(Potato.condiments))
print(Potato)
Potato.add('辣椒油')
print(Potato)

        