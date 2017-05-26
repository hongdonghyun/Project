def make_student(name,age,gender):
    return {
            'name' : name,
            'age' : age,
            'gender' : gender
            }

def print_student(student):
    for key,value in student.items():
        print('{} : {}'.format(key,value))

s1 = make_student('hongdonghyun',27,"남성")
print_student(s1)


# make_student를 키워드 인자로 호출한 결과를  s2에 할당
#키워드 순서는 age,name gender순으로 주어짐

s2 = make_student(age=27,name='hongdonghyun',gender='남성')
print_student(s2)

