import re

f = open('example.html')
html = f.read()


# parser
class Node(object):
    """HTML태그 하나를 가지는 클래스
        내부에 다른 클래스를 가질수도 있음
        가장 큰 범위는 <html></html>
    """
    _pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'  # {tag}.*? 클래스 ()안은 그룹화
    _pattern_tag_content = r'^<[^!]*?>([.\w\W]*)</.*?>$'  # ^$는 소스문자열의 시작과 끝을 나타낸다.
    _pattern_tag_class = r'class=[\'\"](\w*)[\'\"]' #class의 value를 찾는 정규식 class=안에 "value" value값을 그룹화하여 그룹을 호출해 빼낸다.

    def __init__(self, source):  # 초기화 함수
        self.source = source

    def __str__(self):  # source의 주소값을 호출 한다.
        return '{}\n{}'.format(
            super().__str__(),
            self.source
        )

    def find_tag(self, tag):
        pattern = re.compile(self._pattern_tag_base.format(tag=tag))  # pattern 함수에 사용할 패턴을 컴파일
        m_list = re.finditer(pattern, self.source)  # m_list에 finditer(pattern,iterator)
        if m_list:
            return_list = [Node(m.group()) for m in m_list]  # m_list만큼 순회하면서 return_list에 Node(m.group())이 추가됨
            return return_list if len(return_list) > 1 else return_list[0]  # 값 반환 1이상이면 길이만큼 아니면 0
        return None

    @property
    def class_(self):
        """
        해당 Node가 가진 class속성의 value를 리턴(문자열)
        :return:
        """
        pattern = re.compile(self._pattern_tag_class)  # pattern compile
        m_list = re.finditer(pattern, self.source)  # m_list리스트에 re.finditer의 결과값 리스트를 입력
        if m_list: #m_list가 있다면
            return_list = [m.group(1) for m in m_list] #return_list에 값을 저장한다
            return return_list if len(return_list) >1 else return_list[0] #반환하는데 리스트의 길이가 1보다 크면 return_list를 아니면 return_list[0]을 반환
        return None
        # if m:
        #     return m.group(1)
        # return None

    @property
    def content(self):
        """
        Node인스턴스의 내용을 리턴
        :return: Node(태그)내부의 내용을 리턴
        """
        pattern = re.compile(self._pattern_tag_content)
        m = re.search(pattern, self.source.strip())
        if m:
            return m.group(1)
        return None


with open('example.html') as f:  # 자동으로 파일을 닫아준다.
    html = Node(f.read())

node_div = html.find_tag('div')


print(node_div.class_)




# node_p_list = node_div.find_tag('p')

# for node_p in node_p_list:
#     print(node_p.content)
#
# print(node_div)




# pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'  # {tag}.*? 클래스
# pattern_tag_content = r'^<.*?>([.\w\W]*)</.*?>$'
# def find_tag(tag, source):
#     """주어진 tag 문자열 또는 문자열의 리스트 반환
#     :param tag: 검색을 원하는 태그 ex)'div'
#     :param source:태그를 검색할 전체 문자열
#     :return: 검색 결과가 1개일 경우에는 tag문자열, 2개 이상 일 경우에는 tag문자열의 리스트
#     """
#     pattern = re.compile(pattern_tag_base.format(tag=tag))
#     m_list = re.finditer(pattern, source)
#     if m_list:
#         return_list = [m.group() for m in m_list]
#         return return_list if len(return_list) > 1 else return_list[0]
#     return None
#
#
# def get_tag_content(tag_string):
#     """
#     tag 문자열이 주어졌을 때, 해당 tag의 내용을 리턴
#     :param tag_string: <tag>내용</tag>형태의 문자열
#     :return: 위 형태에서 '내용부분
#     """
#     pattern = re.compile(pattern_tag_content)
#     m = re.search(pattern, tag_string.strip())
#     if m:
#         return m.group(1)
#     return None
# html문자열 변수에서 'div'태그의 내용을 찾아 반환한다.
# div = find_tag('div', html)
# p_list = find_tag('p', div)
# print(p_list)
# for p in p_list:
#     print(get_tag_content(p))
#
# div_content = get_tag_content(div)
# print(div_content)
