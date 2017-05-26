#
#
# list= [x for x in range(1,5)]
# d = {'apple':'red'}
#
# try:
#     print(d['yellow'])
#
#
# except IndexError as e:
#     print(e)
#     print('IndexError')
#
# except KeyError as e:
#     print(e)
#     print('KeyError')
#
#
#
#

"""
1.정규표현식으로 검사했을 때, 일치하는 패턴이 없을 경우
NotMatchedException을 정의
    1-1. Exception을 상속
    1-2. __init__ 초기화 메서드에 패턴문자열과 소스문자열을 받도록함
    1-3. __str__메서드가 일치하는 결과가 없다는 문자열을 리턴하도록함

2.패턴문자열과 소스문자열을 매개변수로 갖는 search_from_sourece함수를 정의하고,
  re.search에 소스 문자열을 전달했을 때
  MatchObject를 찾지 못하면 NotMatchedException을 발생시킴

3.try-except구문에서 위 함수를 실행해 예외를 발생시킴

4.위 구문에 else절을 추가해서 예외가 발생하지 않았을 경우의 검색결과를 출력

5.위 구문에 finally절을 추가해서 프로그램이 끝났음을 출력
"""

import re


class NotMatchedException(Exception):
    """
    패턴과 소스를 받아 일치하지 않았다를 알려준다.
    """

    def __init__(self, pattern, source):
        self.pattern = pattern
        self.source = source

    def __str__(self):
        return print("일치하는 결과가 없습니다.")


def search_from_source(pattern, source):
    m = re.search(pattern, source)

    if m:
        return m
    else:
        raise NotMatchedException(pattern, source)


try:
    source = 'hongdonghyun web programming school 5th'
    pattern = 'web'
    m = search_from_source(pattern, source)

except NotMatchedException as e:
    print(e)

else:
    print("matched : {} ".format(m.group()))

finally:
    print("프로그램 종료")
