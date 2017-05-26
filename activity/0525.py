import re

class EmptyMatchedException(Exception):

    def __init__(self,pattern,string):
        self.pattern =pattern
        self.string = string

    def __str__(self):
        return print('일치하는 결과가 없습니다.')


def search(pattern,string):
    m = re.findall(pattern,string)

    if m:
        return m
    else:
        raise EmptyMatchedException(pattern,string)


try:
    # string = 'Lux, the Lady of Luminocity'
    # pattern = 'man'
    # m = search(pattern,string)
    pass


except EmptyMatchedException as e:
    print(e)

else:
    string = 'Lux, the Lady of Luminocity'
    pattern =r'L\w*'
    m = search(pattern,string)
    print(m)