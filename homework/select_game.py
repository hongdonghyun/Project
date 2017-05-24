class Cat_grow:
    def __init__(self, name, type, age,strength=0,intelligence=0,agility=0,fatigue=0): #고양이의 신상정보
        self.name = name
        self.type = type
        self.age = age
        self.strength = 0
        self.intelligence = 0
        self.agility = 0
        self.fatigue = 0

    def cat_training_intelligence(self, intelligence, fatigue):
        self.intelligence += intelligence
        self.fatigue += fatigue

    def cat_training_strength(self,strength,fatigue):
        self.strength += strength
        self.fatigue += fatigue

    def cat_training_agility(self,agility,fatigue):
        self.agility += agility
        self.fatigue += fatigue

    def cat_older(self,aage):
        self.age +=aage



    def cat_info(self): # 고양이 신상출력
        print('이름 : {}, 종류 : {}, 나이 : {}'.format(self.name,self.type,self.age))

    def cat_info_all(self):
        print('이름 : {}, 종류 : {}, 나이 : {}'.format(self.name, self.type, self.age))
        print('힘 : {}, 민첩 : {}, 지능 : {} 피로도 : {}'.format(self.strength, self.agility, self.intelligence,self.fatigue))




