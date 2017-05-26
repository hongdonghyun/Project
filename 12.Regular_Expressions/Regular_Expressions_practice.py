import re
import string

source ='Lux, the Lady of Luminosity'
m = re.match('Lux',source)
m = re.match('.*Lady',source)
m = re.search('o',source)
m = re.match(r'.*(Lady).*',source)
l = re.findall('y.?.?',source)

# if m:
#     print(m.group())

# printable = string.printable
#
# print(printable)
# print(re.findall('\w',printable))
# print(re.findall('\W',printable))
# print(re.findall('\d',printable))
# print(re.findall('\D',printable))
# print(re.findall(r'\s',printable))
#   1번  a로 시작하는 4글자 단어 찾기
# re.findeall(\ba\w{3}\b)

#   2번  r로 끝나는 단어 찾기
# re.findall(r'\w*r\b')

#   3번  a,b,c,d,e아무문자나 3번연속
# re.findall(r'\w*[abcde]{3}\w*')

#   4번  re.sub를 사용해서 ,로 구분된 앞/뒤 단어에 대해 앞단어는 대문자화 시키고, 뒷단어는 대괄호로 감싼다.
#   이 과정에서, 각각의 앞/뒤에 before, after그룹 이름을 사용한다.
#  re.compile(r'(?P<before>\w+)(?P<center>\s*,\s*)(?P<after>\w+')
#  lambda m : '{}{}{}'.format
#과제
story = """Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia."""

m = re.findall({'a'},story)
print(m)
