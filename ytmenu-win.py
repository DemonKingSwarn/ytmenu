#!/usr/bin/env python

import requests
import re
import os
import pwd

def get_username():
    return pwd.getpwuid(os.getuid())[0]

url='https://vid.puffyan.us'
player="C://Users//" + get_username() + "//AppData//Roaming//mpv//mpv.exe"
print(player)
def search_yt():
    global url
    global player
    search=input("Search YouTube: ")
    query=search.replace(" ", "+")
    response=requests.get(f'{url}/search?q={query}')
    x=re.findall(r'(https?://\S+)', response.text)[0]
    url=x.replace("\">", "")
    print(url)
    os.system(f"{player} {url}")

search_yt()
