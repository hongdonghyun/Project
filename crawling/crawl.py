#web_toon 패키지 내부의 NaverWebtooncrawler 클래스형 인스턴스를 생성 인스턴스에서 crawl_episode생성

from web_toon import *

naver_crawl = NaverWebtoonCrawler(316909)

naver_crawl.crawl_episode(1)

