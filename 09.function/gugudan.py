def make_gugu(num):
    for index in range(1,10):
        return [(num,y,num * y) for y in range(1,10)]


def print_gugu(print_type,gugu_list):
    if print_type == 'simple':
        for item in gugu_list:
            print(item)
    elif print_type == 'normal':
        for x,y,z in gugu_list:
            print('{} * {} = {}'.format(x,y,z))


def gugu(range_,print_type,make_gugu,print_gugu):
    
    for num in range_:
        print('{}'.format(''+str(num)+'단'))
        new_gugu_dan = make_gugu(num)
        print_gugu(print_type,new_gugu_dan)

        print('')

gugu(range(2,4),'simple',make_gugu,print_gugu)

