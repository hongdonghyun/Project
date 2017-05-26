# def return_sting(input_text):
#     ''' 함수설명'''
#     if input_text == 'red':
#         return('apple')
#     elif input_text =='yellow':
#         return('banana')
#     elif input_text =='green':
#         return('melon')
#     else:
#         return("I don't know")
# print(return_sting('red'))

# def ssquare(*args) :
#     """ args는 튜플로 옴 풀어줘야 한다 """
#     if len(args)==2:
#         return args[0] *args[1]
#     elif len(args)==1:
#         return args[0] * args[*]
#     else:
#         ('하나 또는 두개의 숫자를 입력하세요')
#
# print(ssquare(3))

# def retrun_two_int(input_int1,input_int2):
#     summary_tuple = ()
#     sum_ = input_int1 + input_int2
#     if input_int1 > input_int2:
#         sub_ = input_int1 - input_int2
#     else:
#         sub_ = input_int2 - input_int1
#
#         summary_tuple = summary_tuple + (sum_,)
#         summary_tuple = summary_tuple + (sub_,)
#         return summary_tuple
#
# print(retrun_two_int(10,20))

# def kargs_set(*args):
#     print(args)
# kargs_set(10,20,30)

aaa = [(lambda x,y : '{} x {] ={}'.format(x,y,x*y))(x,y) for x in range(1,10) for y in range(1,10)]

for item in aaa:
print(item)


