'''
Created on 2017年6月16日

@author: admin
'''
class Home:
    def  __init__(self,area):
        self.area=area
        self.rongNaList=[]
        self.light='off'
    def __str__(self):
        msg= '家当前的可用面积：'+str(self.area)+','
        for temp in self.rongNaList:
            msg +=temp.getBedName()+','
        msg=msg.strip(',')
        return msg
    def containItem(self,item):
        area1=item.getBedArea()
        if self.area>area1:
            self.rongNaList.append(item)
            self.area-=area1
        else:
            print('当前添加物品失败')

class Bed:
    def __init__(self,name,area1):
        self.name=name
        self.area=area1
    def __str__(self):
        msg= self.name+'床的面积为：'+str(self.area)+self.getBedName()
        return msg
    def getBedArea(self):
        getBedArea=self.area
        return getBedArea
    def getBedName(self):
        return self.name
home=Home(100)
bed=Bed('木头',12)
home.containItem(bed)
print(home)
bed=Bed('席梦思',12)
home.containItem(bed)
print(home)


        