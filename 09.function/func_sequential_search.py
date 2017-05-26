

def search(input_string,input_key):
    index=0
    while index < len(input_string):
        if input_key == input_string[index]:
            return index
        index +=1

aa=search('abcdefghijak','e')
print(aa)



