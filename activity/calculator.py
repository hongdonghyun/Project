class calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def plus(self):
        print(self.a + self.b)

    def minus(self,a,b):
        print(self.a - self.b)

    def multiply(self,a,b):
        print(self.a * self.b)

    def division(self,a,b):
        print(self.a / self.b)


class multicalculator(calculator):

    def multi(self):
        print(self.a * self.b )

# new_calculator = calculator(1,2)
# new_calculator.plus()


# new_multi = multicalculator(2,2)
# new_multi.multi()
# print(type(new_multi))

# def pplus(a,b):
#     return a+b
#
# print(pplus(1,3))

class xyz:
    def xxxx(self,a,b):
        self.a =a
        self.b =b
        return a + b

new__ = xyz()
print(new__.xxxx(2,2))


# print(new__)
