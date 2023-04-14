import math
import time

import requests
import re
import os

p = re.compile(r'style="background-image:url\((.*?)\);')
url = input("Sticker pack ID >> ")

# go on https://store.line.me/stickershop, find a pack you like
# click on the page then take the number you see after product/
# for example if you want https://store.line.me/stickershop/product/19142873/en
# then the sticker pack ID is 19142873.

url = f"https://store.line.me/stickershop/product/{url}/ja"
save = input("where to save >> ")

index = 0

r = requests.get(url)

ndone = "⬜"
done = "⬛"

t = p.findall(r.text)
length = len(t)

try:
    os.mkdir(save)
    os.mkdir('temp')
except FileExistsError:
    pass

for s in t:
    donecount = round((index/length)*10)
    ndonecount = 10 - donecount
    print('\r' + done*donecount + ndonecount*ndone, end="")
    with open('temp/temp.png', 'wb') as f_out:
        r = requests.get(s, stream=True)
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f_out.write(chunk)
    try:
        os.rename('temp/temp.png', '{}/{}.png'.format(save, str(index)))
    except FileExistsError:
        pass
    index += 1

print("\nDone!")