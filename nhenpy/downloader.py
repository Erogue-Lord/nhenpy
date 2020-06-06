import urllib.request
import os
import itertools
import re
import argparse
import shutil

from bs4 import BeautifulSoup
import requests

from .packing import cbz

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()
    download(args.url)

def download(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.title.string.split(' » ')[0]
    print(title)
    div = soup.find('div', attrs={'id': 'cover'})
    cover_url = div.a.img["data-src"]
    id = re.findall('[0-9]*', cover_url)
    id = ''.join(id)
    path = os.path.abspath(f'{os.getcwd()}/temp/')
    if not os.path.exists(path):
        os.makedirs(path)
    print("downloading...")
    for i in itertools.count(1):
        try:
            image_url = f'https://i.nhentai.net/galleries/{id}/{i}.jpg'
            urllib.request.urlretrieve(image_url, os.path.abspath(f'{path}/{str(i).zfill(2)}.jpg'))
        except urllib.error.HTTPError:
            break
        else:
            print(image_url)
    print('Finished Download\ncreacting file...')
    cbz('temp', title)
    shutil.rmtree(path)
