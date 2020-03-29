import re
import requests

with open('fashion.html', 'r') as f:
    html = f.read()

links = re.findall(r'href="(https://vk\.com/photo.+?)"', html)
index = links.index('https://vk.com/photo139408591_456243380')
links = links[index:]
for link in links:
    print(link)
    resp = requests.get(link, cookies={'remixsid': '6b7f477b01e5e21b1c65970e98f2022c782c976339edbf24769e6'})
    image_link = re.search(r'https://pp\.userapi\.com/c841632/v841632113/.+\.jpg', resp.text).group()
    resp = requests.post('https://api.imgur.com/3/image', headers={'Authorization': 'Client-ID 090f2f7bbc72b32'},
                         data={'album': '96Zv0TFeAywKPws', 'image': image_link}).json()
    print(resp)
    if resp['data'].get('error', None) is not None:
        raise Exception(resp)
