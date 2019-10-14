#!/usr/bin/python3
from requests import get, post, Session
from bs4 import BeautifulSoup

def request_url(url):

    key = get(url)
    soup = BeautifulSoup(key.text, 'html.parser')
    cookie = soup.find(attrs={"name": "key"}).get('value')

    param = {'id': '869',
            'holdthedoor': 'Submit',
            'key': cookie
            }
    example = post(url, data=param,cookies=key.cookies)
    if example.status_code == 200:
        print("ojo con eso manito")
    else:
        print(example.status_code)

    #print(soup.prettify())

for cont in range(4096):
    scraper1 = request_url('http://158.69.76.135/level1.php')
