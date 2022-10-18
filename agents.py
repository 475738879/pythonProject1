import random
import re
from urllib import request
import requests
agent1 = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
agent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"
agent3 = "Mozilla/5.0 (Linux; Android 10; HMA-AL00 Build/HUAWEIHMA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/6002 MicroMessenger/7.0.12.1620(0x27000C36) Process/tools NetType/WIFI Language/zh_CN ABI/arm64"
agent4 = "Mozilla/5.0 (Linux; Android 8.1.0; PBAM00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.1.0) NABar/2.0"
agent5 = "Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.1.0) NABar/2.0"

url = "http://www.baidu.com/"
list = [agent4,agent5,agent3,agent2,agent1]

agent = random.choice(list)
print(agent)
header = {
'user-agent': agent
}
resp = requests.get(url, headers=header)
test = resp.text
# print(test)
obj = re.compile(r'<meta name="description" content="(?P<t1>.*?)">', re.S)
result = obj.finditer(test)

for i in result:
    print(i.group("t1").strip())
    # print(i.group())
resp.close()

