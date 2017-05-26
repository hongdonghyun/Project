


def add_args(arg1,arg2):
    print(arg1+arg2)

def run_something(func,arg1,arg2):
    func(arg1,arg2)

run_something(add_args,5,9)


def outer(a,b) :
    print('{},{},{}'.format(a,b,'여기는 바깥함수'))

    def inner(c,d):
        print('{},{},{}'.format(c,d,'여기는 안쪽함수'))
        return c + d
    return inner(a,b)

print(outer(4,7))


def knights(saving):
    def inner(quote):
        return "we are the knights who say: '%s'"%quote
    return inner(saving)

print(knights('ddd'))

