# import and make initial
from math import pi as p, sqrt as s
print(p,s(4.0))

# import example
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
print(response.status)

# url example
from urllib import request
from bs4 import BeautifulSoup
target = request.urlopen("http://www.kma.go.kr/weather/forcast/mid-term-rss.jsp?stndid=108")
soup = BeautifulSoup(target, "html.parser")
for location in soup.selection("location"):
    print("city : ", location.selection_one("city").string)