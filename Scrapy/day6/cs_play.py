class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")
    def show_life_value(self):
        self.__life_value-=50
        print(self.__life_value)
    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r1.show_life_value()
r2 = Role('Jack', 'terrorist', 'B2')  #生成一个角色
r1.buy_gun('AK47')