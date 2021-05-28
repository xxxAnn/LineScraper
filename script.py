import math
import time

import requests
import re
import os

p = re.compile(r'style="background-image:url\((.*?);compress=true')
url = input("Sticker pack ID >> ")

url = "{}{}{}".format("https://store.line.me/stickershop/product/", url, "/ja")
save = input("where to save >> ")

index = 0

r = requests.get(url)

おわってない = "⬜"
おわってる = "⬛"

t = p.findall(r.text)
length = len(t)

try:
    os.mkdir(save)
    os.mkdir('temp')
except FileExistsError:
    pass

for s in t:
    おわってるすう = round((index/length)*10)
    おわってないすう = 10 - おわってるすう
    print('\r' + おわってる*おわってるすう + おわってないすう*おわってない, end="")
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