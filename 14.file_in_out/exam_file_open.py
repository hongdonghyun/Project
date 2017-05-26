skills = '''fff
ddd
werwerwer
qqqq
rrr
'''

f = open('skills.txt''xt')
f.write(skills)
f.close()

try:
    f = open('skiils.txt','xt')

except FileExistsError:
    print('file is already exist')

print('program terminate')

f = open('skills.txt','rt')
skills = f.read()
f.close()
print(skills)