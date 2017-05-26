def make_gugu(num):
    for x in range(1,10):
        return [(num,y,num*x)for y in range(1,10)]

def print_gugu(print_type,gugu_list):
    if print_type=='simple':
        for item in gugu_list:
            print(item)
    elif print_type =='normal':
        for x,y,z in gugu_list:
            print('{} x {} = {}'.format(x,y,z))

def gugu(range_,print_type,make_gugu,print_gugu):
   
    for index in range_:
        print('{}'.format(''+str(index)+'단'))
        new_gugu = make_gugu(index)
        print_gugu(print_type,new_gugu)

        print('')


gugu(range(2,4),'normal',make_gugu,print_gugu)

