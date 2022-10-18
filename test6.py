#1.拿到主页面的源代码，提取到子页面的链接地址
#2.通过href拿到子页面的内容，从子页面中拿到图片的下载地址
#3.下载图片
import requests
from bs4 import BeautifulSoup
import re
url = "http://bizhi360.com/weimei/"
resp = requests.get(url)
resp.encoding = "UTF-8"

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", attrs={"class": "pic-list"}).find_all("a")
for a in alist:
    s = "http://bizhi360.com/"+a.get("href")
    #拿到子页面的源代码
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    child_page_resp = requests.get(s, headers=headers)
    child_page_resp.encoding = "UTF-8"
    child_page_text = child_page_resp.text
    #从子页面中拿到图片的下载途径
    # child_page = BeautifulSoup(child_page_text, "html.parser")
    # p = child_page.find("div", attrs={"class": "article"})
    obj = re.compile(r'<div class="article">.*?<a href="(?P<name>.*?)"', re.S)
    result = obj.finditer(child_page_text)

    for i in result:
        print(i.group("name").strip())
resp.close()
