#!/bin/usr/python3

import re
import requests
import argparse
from bs4 import BeautifulSoup

sq = argparse.ArgumentParser(description='Startpage CLI Search.')
sq.add_argument('-q', metavar='Query', help='Input your keyword or query. Use " if query contains spaces.')
qData = sq.parse_args()

# Request URL
spUrl = "https://www.startpage.com/sp/search"

# Request Headers
reqHeaders = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Moozilla/5.0 (Windows 95; rv:124.0) Lizard/20100101 IceWeasle/124.0"
}

# Request Body
reqData = {
    "query": qData.q,
    "cat": "web"
}	

req = requests.post(url=spUrl, headers=reqHeaders, data=reqData)
res = BeautifulSoup(req.text, "html.parser")

urls = []
for link in res.find_all('a'):
    result = link.get('href')
    if "startpage" not in str(result).strip():
        if "Startpage" not in str(result).strip():
            if "http" in str(result).strip():
                urls.append(result)
                urlsDedupe = list(set(urls))
                for url in urlsDedupe:
                    print("Search Result: " + url + "\n\n <-------------- = = =|::|= = = -------------> \n") 