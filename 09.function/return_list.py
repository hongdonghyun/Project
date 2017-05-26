def return_list(value,result=None):
    if result == None;
        result=[]
    result.append(value)
    return result


#기존 result에 전달할 리스트 변수가 있던 경우
l=['apple']
n_l =return_list('banana',l)
print(n_l)

n_l = return_list('lemon',n_l)
print(n_l)


#return_list함수에 result매개변수로 사용할 list변수를 전달하지 않은 경우

n_l = return_list('mango')
print(n_l)



