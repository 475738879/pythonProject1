#拿到页面源代码  requests
#通过re来提取想要的有效信息  re模块
import csv

import requests
import re

url = 'https://movie.douban.com/top250'
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36"
}
resp = requests.get(url, headers=header)
# resp = requests.get(url, headers=header,verify =False)
page_content = resp.text #爬取到的页面源代码

# obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
# obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<span class="other">&nbsp;/&nbsp;(?P<asas>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?', re.S)
# obj = re.compile(r'<div class="hd">.*?<span class="title">(?P<name>.*?)</span>', re.S)
# obj = re.compile(r'<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp', re.S)
# obj = re.compile(r'<li>.*?<div class="item">.*?<span class="other">&nbsp;/&nbsp;(?P<asas>.*?)</span>', re.S)
# obj = re.compile(r'<div class="star">.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>', re.S)
# obj = re.compile(r'<div class="bd">.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<ave>.*?)</span>.*?<span>(?P<people>.*?)人评价</span>', re.S)
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                 r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<div class="star">.*?<span class="rating_num" property="v:average">(?P<ave>.*?)</span>.*?'
                 r'<span>(?P<people>.*?)人评价</span>', re.S)

result = obj.finditer(page_content)

for i in result:
    print(i.group("name").strip())
    # print(i.group("asas").strip())
    print(i.group("year").strip())
    # print(i.group("pingfen").strip());
    print(i.group("ave").strip());
    print(i.group("people").strip());
f = open("data.csv", mode="w",encoding='UTF-8')
cswriter = csv.writer(f)
for i in result:
    dic = i.groupdict()
    dic['year'] = dic['name'].strip()
    dic['year'] = dic['year'].strip()
    dic['year'] = dic['ave'].strip()
    dic['year'] = dic['people'].strip()
    cswriter.writerow(dic.values())

resp.close

