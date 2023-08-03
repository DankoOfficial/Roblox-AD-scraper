# Author: @DankoOfficial on Github
# Discord: 5sky
from requests import get
from random import randint
from os import path, makedirs

adsType, done = input('>> Ads Type\n\n[1] Up\n[2] Sides\n[3] Down\n\n>> '), []

while not adsType in ['1','2','3']: adsType = input('>> Ads Type\n\n[1] Up\n[2] Sides\n[3] Down\n\n>> ')

makedirs('Scraped') if not path.exists('Scraped') else ""

while True:
    srca = get(f'https://www.roblox.com/user-sponsorship/{adsType}').text.split('<img src="')[1].split('"')[0]
    if srca not in done:
        src = get(srca)
        open(f'Scraped/{randint(100000,200000)}.png','wb').write(src.content)
        done.append(srca)
        print(f'>> Scraped {len(done)} ads so far - {srca}',end='\r')
