class animal:
    '''동물이름과 다리의수 색상이 들어있는 animal클래스'''
    sound = '동물의 울음소리 바꾸기'
    def __init__(self, name, leg, color):
        self.__name = name
        self.leg = leg
        self.color = color

    def animal_info(self):
        print('이름 : {}'.format(self.__name))
        print('다리개수 : {}'.format(self.leg))
        print('통상적인 색상 : {}'.format(self.color))

    @classmethod
    def change_sound(cls,sound):
        cls.sound = sound

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name
        print('이름이 변경됨 : {}'.format(self.__name))


class poketmon(animal):
    def __init__(self, name, leg, color, attack):
        super().__init__(name, leg, color)
        self.attack = attack

    def poketmon_info(self):
        print('이름 : {}'.format(self.name))
        print('다리개수 : {}'.format(self.leg))
        print('통상적인 색상 : {}'.format(self.color))
        print('짱짱 센 공격기술 : {}'.format(self.attack))




animal_ = animal('개','4개','겁나많음')
animal_.animal_info()
animal_.change_sound("왈왈왈 으르렁\n")
print(animal_.sound)
animal_.name='efef'

poketmon_ = poketmon('롱스톤','없음','회색','몸통박치기')
poketmon_.poketmon_info()
poketmon_.change_sound('롱스톤은 울지않아')
print(poketmon_.sound)