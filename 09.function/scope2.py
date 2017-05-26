
global_level= 100

def level_add(value):
    value += 30
    print(value)


level_add(global_level)
print(global_level)


def level_add2():
    global global_level
    global_level += 30
    print(global_level)

level_add2()
print(global_level)
