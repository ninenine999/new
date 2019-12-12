class Dog(object):
    def __init__(self,name):
        self.name=name
        self.__food='馒头'
    @property
    def eat(self):
        print('%s吃的%s'%(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        self.__food=food
        print('%s吃的%s'%(self.name,self.__food))
    @eat.deleter
    def eat(self):
        del self.__food
        print('删完了')
ww=Dog('小黄')
ww.eat

ww.eat='包子'
del ww.eat
