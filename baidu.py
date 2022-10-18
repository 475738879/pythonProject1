import re

from urllib import request
url = "http://www.baidu.com/"
reponse = request.urlopen(url).read().decode()
pat = r"<title>(.*?)</title>"
data = re.findall(pat, reponse)
print(data[0])