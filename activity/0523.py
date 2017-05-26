# ran_list = [1,2,98, 3,92, 4,44, 7, 9, 11]
#
# def selection(x):
#     length = len(x)-1
#     for i in range(length):
#         for j in range(length-i):
#             if x[j] > x[j+1]:
#                 x[j],x[j+1] = x[j+1], x[j]
#
#     return x
#
# def selection_edit(input_list) :
#     length = len(input_list)
#     for index in range(length):
#         min_index = index
#
#         for index2 in range(index+1,length):
#
#             if input_list[min_index] > input_list[index2]:
#                 min_index = index2
#
#         input_list[index],input_list[min_index] = input_list[min_index],input_list[index]
#
#         print(input_list)
#
# print(selection_edit(ran_list))
#
# class Monster():
#     description = 'poketmon'
#     hp = 100
#     dash_dmage =10
#
#     def __init__(self,name):
#         self.name = name
#
#
#     def attack(self,enemy):
#         enemy.hp = self.dash_dmage
#         print('{}는 {}에게 {}만큼 피해를 줬다.'.format(self.name,enemy.name,enemy.dash_dmage))
#
#     @staticmethod
#     def run():
#         print('도망치기')
#
#     @classmethod
#     def change_type(cls,description):
#         cls.description =description
#
#
# ggobugi = Monster('ggobugi')
# pikachu = Monster('pikachu')
# pikachu.run()
# ggobugi.attack(pikachu)
# pikachu.change_type('digimon')
# print(pikachu.description)