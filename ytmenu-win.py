import requests
import re
import os

url='https://vid.puffyan.us'
player="vlc"
search=input("Search YouTube: ")
query=search.replace(" ", "+")
response=requests.get(f'{url}/search?q={query}')
#string="watch\?v=.{11}"
x=re.findall(r'(https?://\S+)', response.text)[0]
replaced_str=x.replace("\">", "")
print(replaced_str)
os.system(f"start {player} {replaced_str}")
