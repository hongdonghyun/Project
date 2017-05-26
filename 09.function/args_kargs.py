#return값 tuple

def print_args(*args):
    print(args)

#return값 dict

def print_kargs(**kargs):
    print(kargs)

def print_args_kargs(*args,**kargs):
    print(args)
    print('')
    print(kargs)



print_args('hello','world','!!')
print('\n')


print_kargs(hello='HELLO',world='WORLD',sssss='!!!!!!')
print('\n')

print_args_kargs('hello',hello='HELLO')

