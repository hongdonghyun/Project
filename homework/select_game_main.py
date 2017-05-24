
from homework.select_game import Cat_grow

print('===================================\n')
print('고양이 : 키워\n')
print('인간  : 네?\n')
print('고양이 : 키우라고\n')
print('===================================\n')

make_flag=None
new_cat = Cat_grow(None,None,None)


while True:
    print('\n행동을 선택하세요.')
    print('1.놀아본다 2.훈련 3.잠잔다 4.신상정보 입력/보기 0.종료')
    select = input("입력 : ")
    if select == '1':

        pass

    elif select == '2':

        print('\n훈련을 선택하세요.')
        print('1.배변훈련 2.캣타워 등반 3.쥐 장난감 가지고 놀아버리기 4.돌아가기\n')
        tra_select =input('입력 :')
        if new_cat.name ==None:
            print('고양이의 신상을 먼저 입력해주세요.\n')

        elif tra_select == '1':
            if new_cat.fatigue > 70:
                print('{}이(가) 패캠수강생마냥 피로에 찌들어있습니다.\n 잠을 취하세요.'.format(new_cat.name))
                continue

            print('{}이(가) 열심히 똥을 쌉니다.'.format(new_cat.name))
            new_cat.cat_training_intelligence(10, 15)

            if new_cat.intelligence == 5:
                print('{}이(가) 덜 멍청해졌습니다!'.format(new_cat.name))
            elif new_cat.intelligence == 20:
                print('{}은(는) 이제 주인을 알아볼 정도의 지능을 가졌습니다!'.format(new_cat.name))
            elif new_cat.intelligence == 100:
                print('{}은(는) 이제 주인보다 똑똑합니다!'.format(new_cat.name))

        elif tra_select =='2':
            if new_cat.fatigue > 70:
                print('{}이(가) 패캠수강생마냥 피로에 찌들어있습니다.\n 잠을 취하세요.'.format(new_cat.name))
                continue

            print('{}이(가) 열심히 캣타워를 등반합니다.'.format(new_cat.name))
            new_cat.cat_training_strength(10,20)

            if new_cat.strength == 5:
                print('{}이(가) 어좁이를 벗어났습니다!'.format(new_cat.name))
            elif new_cat.strength == 20:
                print('{}은(는) 이제 몸통박치기가 가능해집니다!'.format(new_cat.name))
            elif new_cat.strength == 100:
                print('{}은(는) 이제 주인보다 힘이쎕니다!'.format(new_cat.name))

        elif tra_select == '3':
            if new_cat.fatigue > 70:
                print('{}이(가) 패캠수강생마냥 피로에 찌들어있습니다.\n 잠을 취하세요.'.format(new_cat.name))
                continue

            print('{}이(가) 쥐 장난감을 열심히 쫓아다닙니다.'.format(new_cat.name))
            new_cat.cat_training_agility(10, 10)


            if new_cat.agility == 5:
                print('{}은(는) 이제 100m를 30초안에 뜁니다!'.format(new_cat.name))
            elif new_cat.agility == 20:
                print('{}은(는) 아주 민첩하여 눈에 잘 띄지않습니다!'.format(new_cat.name))
            elif new_cat.agility == 100:
                print('{}은(는) 이제 주인보다 민첩합니다!'.format(new_cat.name))

        elif tra_select == '4':
            continue

    elif select == '3':
        if new_cat.fatigue < 20:
            print('{}은(는) 피곤하지 않아요!'.format(new_cat.name))
        else:
            print('힘쎄고 강한아침!\n 피로가 회복되었어요.')
            new_cat.fatigue = 0
            new_cat.cat_older(1)

        if new_cat.age == 30:
            print('{}은(는) 나이가 들어 하늘나라로 가버렸습니다.\n'.format(new_cat.name))
            print("게임종료")
            break

    elif select == '4':

        if make_flag == None:
            new_cat = None
            cat_input =input("이름 입력 : ")
            cat_input2 = input("종류 입력 : ")
            cat_input3 = input("나이 입력 : ")
            if cat_input3 >='30':
                print("다시입력하세요\n")
                continue

            new_cat = Cat_grow(cat_input,cat_input2,cat_input3)
            print('입력하신 정보는 다음과 같습니다.\n')
            new_cat.cat_info()
            make_flag ='1'

        elif make_flag =='1':
            new_cat.cat_info_all()


    elif select == '0':
        break

    else:
        print('다시 입력하세요\n')
