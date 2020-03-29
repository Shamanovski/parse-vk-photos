import re
import requests

from jinja2 import Template
from bs4 import BeautifulSoup

with open('fashion.html', 'r') as f:
    html = f.read()


s = BeautifulSoup(html, "html.parser")
pre_imgs = [(re.search(r'url\((.+)\)', element["style"]).group(1), element.a['href'])
            for element in s.find_all(class_='photos_row')]
ctr = 0
images = []
for _, img_link in pre_imgs:
    resp = requests.get(img_link, cookies={'remixsid': '6b7f477b01e5e21b1c65970e98f2022c782c976339edbf24769e6'})
    with open('bla.html', 'w', encoding='utf-8') as f:
        f.write(resp.text)
    s = BeautifulSoup(resp.text, "html.parser")
    image = re.search(r'Сохранить к себе в альбом<\/a><\/li><li><a href="(.+?)"', resp.text).group(1)
    images.append(image)
    ctr += 1
    print("images added", ctr)

items = zip([item[0] for item in pre_imgs], images)
with open('photos-template.html', 'r') as f:
    markup = f.read()
template = Template(markup)
with open('rendered.html', 'w', encoding='utf-8') as f:
    f.write(template.render(items=list(items)))
