# z가 1이면 더하고 2면 빼고 함수를 f1에 넣어서 실행

def sss(x,y,z):
    if z == 1:
        return x +  y
    elif z == 2:
        return x - y

f1 = sss(3,2,1)
print(f1)
