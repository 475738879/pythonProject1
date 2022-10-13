import requests

# str.encode('utf-8').decode("unicode_escape")
url = 'https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6'
dic ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
resp = requests.get(url,headers =dic)

print(resp)
print(resp.text)

