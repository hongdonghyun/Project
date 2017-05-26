champion = 'lux'

def local1():
    champion ='ahri'
    print('local1: : '.locals())

    def local2():
        champion = 'asdasd'
        print('local2 : '.locals())
        local2()
     
local1()

print(''.locals())

