import requests
import re
import os

url='https://vid.puffyan.us'
player="mpv"

def search_yt():
    global url
    global player
    search=input("Search YouTube: ")
    query=search.replace(" ", "+")
    response=requests.get(f'{url}/search?q={query}')
    #string="watch\?v=.{11}"
    x=re.findall(r'(https?://\S+)', response.text)[0]
    url=x.replace("\">", "")
    print(url)
    os.system(f"{player} {url}")

search_yt()
