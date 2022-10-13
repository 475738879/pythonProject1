#拿到页面源代码  requests
#通过re来提取想要的有效信息  re模块

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
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<span class="other">&nbsp;/&nbsp;(?P<asas>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?', re.S)
# obj = re.compile(r'<div class="hd">.*?<span class="title">(?P<name>.*?)</span>', re.S)
# obj = re.compile(r'<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp', re.S)
# obj = re.compile(r'<li>.*?<div class="item">.*?<span class="other">&nbsp;/&nbsp;(?P<asas>.*?)</span>', re.S)
result = obj.finditer(page_content)
for i in result:
    print(i.group("name").strip())
    print(i.group("asas").strip())
    print(i.group("year").strip())


resp.close

