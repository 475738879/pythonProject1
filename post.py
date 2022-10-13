import requests

str.encode('utf-8').decode("unicode_escape")
url = 'https://fanyi.baidu.com/sug'
s=input("输入")
dic ={
    "kw": s}

resp = requests.post(url,data =dic)

print(resp)
print(resp.text)
print(resp.json())