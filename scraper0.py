#!/usr/bin/python3
from requests import get, post
from bs4 import BeautifulSoup

def request_url(url):

    param = {'id': '869',
            'holdthedoor': 'Submit'
            }
    example = post(url, data=param)
    if example:
        print("ojo con eso manito")
    else:
        print(example.status_code)

for cont in range(1024):
    scraper1 = request_url('http://158.69.76.135/level0.php')
