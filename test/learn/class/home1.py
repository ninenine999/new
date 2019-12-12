'''
Created on 2017年6月18日

@author: admin
'''
'''
Created on 2017年6月12日

@author: admin
'''
class Home(object):  
    def __init__(self,area):  
        self.area = area  
        self.jiaju_list=[]  
  
    def cun_fang(self,item):  
        self.new_area = item.get_area()  
        if self.new_area<= self.area:  
            self.area =  self.area-self.new_area;  
            print ("家里还有%s平米"%self.area) 
        else:  
            print ("家里空间不够了") 
        self.jiaju_list.append(item.get_name())  
  
    def __str__(self):  
        msg="家具列表: "  
        for temp in self.jiaju_list:  
            msg+=temp  
        return msg  
  
class jiaju(object):  
    def __init__(self,name,new_area):  
        self.name=name  
        self.new_area = new_area  
  
  
    def get_area(self):  
        return self.new_area  
  
    def get_name(self):  
        return self.name  
  
def get_obj(name,new_area):  
    return jiaju(name,new_area)  
  
  
  
  
home = Home(200)  
bed = get_obj("bed",10)  
  
deng = get_obj("deng",20)  
home.cun_fang(deng)  
home.cun_fang(bed)  
print (home)  