def range_gen(num):
    i=0
    while i <num:
        yield i
        i+= 1

gen = range_gen(10)
gen
print(type(gen))

print(gen.__next__())
print(gen.__next__())
