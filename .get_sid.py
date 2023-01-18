import re

import requests

resp = requests.get(
    'https://translate.yandex.ru/',
    headers={
        'Host': 'translate.yandex.ru',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'
    }
)

if sid := re.compile(r'SID\s?:\s?[\'"]([^\'"]+)[\'"]').findall(resp.content.decode('utf-8')):
    print('.'.join(i[::-1] for i in sid[0].split('.')))
else:
    print(resp.content.decode('utf-8'))
