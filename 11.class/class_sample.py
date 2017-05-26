class Shop:
    description = 'description'
    def __init__(self,name,shop_type,address):
        self.name = name
        self.shop_type = shop_type
        self.address = address

    def shop_info(self):
        print('상점정보 ({})'.format(self.name))
        print('유형: {}'.format(self.shop_type))
        print('주소: {}'.format(self.address))

    def change_type(self,change_type):
        self.shop_type = change_type


    @classmethod
    def change_desc(cls,description):
        cls.description = description

    @staticmethod
    def print_():
        print('hello')

    # @property #get
    # def shop_type(self):
    #     return self.shop_type
    #
    # @shop_type.setter
    # def shop_type(self,new_shop_type):
    #     self.__shop_sype = new_shop_type
    #     print('{}'.format(self.shop_type))


class PCroom(Shop):

    def __init__(self,name,shop_type,address,price):
        super().__init__(name,shop_type,address)
        self.price = price

    def shop_info(self):
        print('pc방 ({})'.format(self.name))
        print('유형: {}'.format(self.shop_type))
        print('주소: {}'.format(self.address))
        print('요금: {}'.format(self.price))


### 다형성과 덕 타이핑
#다형성 : 동일한 실행이지만, 다른 동작을 수행할 수 있도록 허용하는 것
class User:
    def __init__(self,name):
        self.name = name

    def eat_something(self,something):
        something.eat()

    def eat_food(self,food):
        food.eat()

    def eat_drink(self,drink):
        drink.eat()

class Something:
    def __init__(self,name):
        self.name =name

    def eat(self):
        print('{}는 무엇인지 몰라 먹을 수 없다!'.format(self.name))

class Food(Something):
    def eat(self):
        print('{}을 먹었다 배가부르다!'.format(self.name))

class Drink(Something):
    def eat(self):
        print('{}을 마셨다. 갈증이 해소됐다!'.format(self.name))
