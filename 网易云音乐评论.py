from Crypto.Cipher import AES
from base64 import b64encode

import requests
import json


data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_411214279",
    "threadId": "R_SO_4_411214279"
}
## params: bUM2x.encText,
## encSecKey: bUM2x.encSecKey

d= data
e ="010001"
f ="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "nVMEz65CNmypYp1Q"

def Get_encSecKey( ):##
    return "51458895f9a066a4d75661d66b61598f9f6eff6c29f936696b706869ea7cc22ed8dc37281a521f02849ac6c199ab0473e865b3fa22627485135883277b02aefa5d3d299e888342ba817a0080a5346f9026ea6be46dd4318cb3c46c0f0077f819a66a04954466286878ac34fbd139b5a1a2f0db4ca16bb4b61173c55899e89605"

def Get_encText(data):
    first = enText(data, g)
    second  = enText(first,i)
    return second

def to_16(a):
    size = 16 - len(a) % 16
    return a+size*chr(size)

def enText(a,b):
    iv = "0102030405060708"
    a = to_16(a)
    aes  = AES.new(key=b.encode("utf-8"),mode= AES.MODE_CBC, iv=iv.encode("utf-8")) ##这两步就是aes加密过程
    bs  = aes.encrypt(a.encode('utf-8'))
    return  str(b64encode(bs),"utf-8")


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

resp=requests.request(url=url,method="POST", data={
    "params": Get_encText(json.dumps(data)),
    "encSecKey": Get_encSecKey()
})


str = resp.content.decode()
dic_json = json.loads(str)

hotComments= dic_json["data"]["hotComments"]

with open("hotcomments.txt","w",encoding='utf-8') as file:
    for i in hotComments:
        file.writelines(i["content"]+"\n")
    print("over!")

resp.close()
file.close()
