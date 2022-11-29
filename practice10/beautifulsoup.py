# beautifulsoup4라는 pypi에서 다운 받은 웹스크래핑 패키지임 삭제해서 실행은 안댐

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())