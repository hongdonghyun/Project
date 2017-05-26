class Hamburger:

    def __init__(self,name,price,calorie):
        self.name = name
        self.__price = price
        self.calorie = calorie

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        self.__price =new_price


class Mcdonald(Hamburger):

    def __init__(self,name,price,calorie,Set):
        super().__init__(name,price,calorie)
        self.Set = Set
        if Set == True:
            self.price = self.price+1500
            self.calorie = self.calorie+150
        else:
            pass

#
#
# hamburger = Hamburger('bulgogi',5500,450)
# print(hamburger.price)
# hamburger.price = 5000
# print(hamburger.price)
mc = Mcdonald('ss',1000,140,'sss')
print(mc.calorie)

# bigmac = Mcdonald('bigmac',5500,450,True)
# bigmac.price =5000
# print(bigmac.price)