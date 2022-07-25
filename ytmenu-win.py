#!/usr/bin/env python

import requests
import re
import pwd
import subprocess

MPV_EXECUTABLE = "mpv"

url = "https://vid.puffyan.us"

search=input("Search YouTube: ")
query=search.replace(" ", "+")
response=requests.get(f'{url}/search?q={query}')
x=re.findall(r'(https?://\S+)', response.text)[0]
x=x.replace("\">", "")

args = [
    MPV_EXECUTABLE,
    f"{x}",
    "--force-media-title={}".format(
        "Rise and live again. As my fist of vengeance. As my Moon Knight."
    )
]

mpv_process = subprocess.Popen(args, stdout=subprocess.DEVNULL)

mpv_process.wait()
