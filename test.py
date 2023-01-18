async def use():
    from trayan import (
        TraYan, AsyncTraYan,
        detect, translate,
        async_detect, async_translate,
        get_supported_langs
    )
    from trayan.models.translator import Language

    ru = 'красивый мужчина в отличных трусах'
    en = 'a handsome man in great underpants'
    proxy = None  # 'scheme://login:password@ip:port'

    with TraYan() as t:
        print(f'{ru} — {t.detect(ru, Language.RU)}')
        print(f'ru-en — {t.translate(ru, Language.RU, Language.EN)}')

    print(f'{en} — {detect(en)}')
    print(f'en-ru — {translate(en)}')

    async with AsyncTraYan(proxy=proxy) as t:
        print(f'{en} — {await t.detect(en, (Language.RU,))}')
        print(f'en-ru — {await t.translate(en, Language.EN, Language.RU)}')

    print(f'{ru} — {await async_detect(ru, proxy=proxy)}')
    print(f'ru-en — {await async_translate(ru, proxy=proxy)}')

    print(f'поддерживаемые языки: {TraYan.supported_langs}')

    print(f'supported langs: {get_supported_langs()}')


if __name__ == '__main__':
    import asyncio

    asyncio.run(use())


# def use():
#     import re
#     import requests
#     # resp = requests.get(
#     #     'https://translate.yandex.ru/',
#     #     headers={
#     #         'Host': 'translate.yandex.ru',
#     #         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
#     #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     #         'Accept-Language': 'en-US,en;q=0.5',
#     #         'Accept-Encoding': 'gzip, deflate, br',
#     #     }
#     # )
#     # print(resp)
#     # token = '.'.join(
#     #     i[::-1] for i in re.findall(r'SID\s?:\s?[\'"]([^\'"]+)[\'"]', resp.content.decode('utf-8'))[0].split('.'))
#     # print(token)
#     token = 'f40509bb.63c81700.6eb28263.74722d74657874'
#
#     resp = requests.post(
#         f'https://translate.yandex.net/api/v1/tr.json/translate',
#         headers={
#             'Host': 'translate.yandex.net',
#             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
#             'Accept': '*/*',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Origin': 'https://translate.yandex.ru',
#             'Referer': 'https://translate.yandex.ru',
#         },
#         params=dict(
#             id=f'{token}-0-0',
#             srv='tr-text',
#             lang='ru-en',
#             reason='type-end',
#             format='text',
#             ajax=1,
#             text='красивый мужчина в отличных трусах',
#             options=4
#         ),
#     )
#     print(resp)
#     # print(resp.json())
#     print(resp.content.decode('utf-8'))
#
#     # resp = requests.get(
#     #     f'https://translate.yandex.net/api/v1/tr.json/detect',
#     #     headers={
#     #         'Host': 'translate.yandex.net',
#     #         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
#     #         'Accept': '*/*',
#     #         'Accept-Language': 'en-US,en;q=0.5',
#     #         'Accept-Encoding': 'gzip, deflate, br',
#     #         'Origin': 'https://translate.yandex.ru',
#     #         'Referer': 'https://translate.yandex.ru/',
#     #     },
#     #     params=dict(
#     #         sid=token,
#     #         srv='tr-text',
#     #         text='белка',
#     #         # hint='ru,en',
#     #         options=1
#     #     )
#     # )
#     # print(resp)
#     # # print(resp.json())
#     # print(resp.content.decode('utf-8'))
#
#
# if __name__ == '__main__':
#     use()


# async def use():
#     import re
#
#     from aiohttp import ClientSession
#
#     TOKEN = 'f40509bb.63c81700.6eb28263.74722d74657874'
#
#     from trayan import detect, async_detect
#
#     # print(await async_detect('красивый мужчина в отличных трусах', ['ru', 'en']))
#     # print(detect('красивый мужчина в отличных трусах', ['ru', 'en']))
#
#     async with ClientSession() as session:
#         if not (token := (TOKEN or input())):
#             async with session.request(
#                     'get',
#                     'https://translate.yandex.ru/',
#                     headers={
#                         'Host': 'translate.yandex.ru',
#                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
#                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#                         'Accept-Language': 'en-US,en;q=0.5',
#                         'Accept-Encoding': 'gzip, deflate, br',
#                     },
#
#             ) as resp:
#                 token = '.'.join(
#                     i[::-1] for i in
#                     re.findall(r'SID\s?:\s?[\'"]([^\'"]+)[\'"]', await resp.text('utf-8'))[0].split('.'))
#                 print(token)
#
#         async with session.request(
#                 'post',
#                 'https://translate.yandex.net/api/v1/tr.json/translate',
#                 params=dict(
#                     id=f'{token}-0-0',
#                     srv='tr-text',
#                     lang='ru-en',
#                     reason='type-end',
#                     format='text',
#                     ajax=1,
#                     text='красивый мужчина в отличных трусах',
#                     options=4
#                 ),
#                 headers={
#                     'Host': 'translate.yandex.net',
#                     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
#                     'Accept': '*/*',
#                     'Accept-Language': 'en-US,en;q=0.5',
#                     'Accept-Encoding': 'gzip, deflate, br',
#                     'Origin': 'https://translate.yandex.ru',
#                     'Referer': 'https://translate.yandex.ru/',
#                 },
#         ) as resp:
#             print(await resp.json(encoding='utf-8'))
#
#         print(session.cookie_jar._cookies)
#
#         # async with session.request(
#         #         'get',
#         #         'https://translate.yandex.net/api/v1/tr.json/detect',
#         #         params=dict(
#         #             sid=token,
#         #             srv='tr-text',
#         #             text='красивый мужчина в отличных трусах',
#         #             hint='ru,en',
#         #             options=1
#         #         ),
#         #         headers={
#         #             'Host': 'translate.yandex.net',
#         #             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
#         #             'Accept': '*/*',
#         #             'Accept-Language': 'en-US,en;q=0.5',
#         #             'Accept-Encoding': 'gzip, deflate, br',
#         #             'Origin': 'https://translate.yandex.ru',
#         #             'Referer': 'https://translate.yandex.ru/',
#         #         },
#         # ) as resp:
#         #     print(await resp.json(encoding='utf-8'))
#
#
# if __name__ == '__main__':
#     import asyncio
#
#     asyncio.run(use())


# async def use():
#     import requests
#     import aiohttp
#
#     http = '85.89.180.71:3128'
#     https = ''
#     socks4 = ''
#     socks5 = ''
#     proxies = (f'http://{http}', f'https://{https}', f'socks4://{socks4}', f'socks5://{socks5}')
#     for proxy in proxies:
#         resp = requests.get(
#             'https://api.ipify.org?format=json',
#             proxies={
#                 'http': proxy,
#                 'https': proxy
#             } if proxy else None
#         )
#         print(resp.json())
#     for proxy in proxies:
#         try:
#             async with aiohttp.request('get', 'https://api.ipify.org?format=json', proxy=proxy or None) as resp:
#                 print(await resp.json(encoding='utf-8'))
#         except:
#             ...
#
#
# if __name__ == '__main__':
#     use()
