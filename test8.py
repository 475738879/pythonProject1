import csv

import requests
import re
def get_conmments():
    url = "https://music.163.com/#//playlist?id=2229469033"
    name_id = url.split('=')[1]
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
        'referer': 'https://music.163.com/playlist?id=2229469033'
    }
    params = "bIzJ4QdGmWKlF3P/4kY9XPfgEkOt7eppzZsUk1ql7sTjQdpkr1kXHphRx6QQI0tVMGOOh3tP6sooXsMFcJuPk9GeimtB9NGc9Xp0sQyyqL5glrEfHCEdI9HMS1zfYsoJ+V1k3EXah3LR5G6B7UgI3pXIQ77QCfLL0bC4WH1SNw415RC7TyH70GlidSRtC1gRY9f3m7Su8qINaCiD7IrJ58Pq3S389CuWUiJeUHrxutxqiGWnLOEM0AfGZYs2WS4NPAx7rUhcaaMqEcWaIlm1xFpY4ZGnYN8ZfCd/iS22Izw="
    encSecKey = "db6907a30e3ea2466e8b6d23d96155ee3cb0d0d26741ddac805a186380a27940ebe79fbc20f3db522c2431922a1c941b874d7ecdb1eab28ec6ed5f2d23f6e07f45ee2031b9c80908e007c2ef4f81dc55075dd4550ac4072d32c32fdc3ef0cdff69593e87479e5777c44baa0422cf4e415ae6b461e382d5733f42ed813f26d6b7"
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    target_url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=".format(name_id)
    reqs = requests.post(target_url, headers=header, data=data)
    reqs.close()
    return reqs
def main():
    page_content = get_conmments().text
    obj = re.compile(r'<div class="n-rcmd">.*?<a href="(?P<name>.*?)"', re.S)
    result = obj.findall(page_content)
    print(result)
    for i in result:
        print(i.group("link").strip())
if __name__== "__main__":
    main()
