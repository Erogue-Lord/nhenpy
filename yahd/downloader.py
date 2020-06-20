import urllib.request
import os
import itertools
import re
import argparse
import shutil

from bs4 import BeautifulSoup
import requests

from .packing import cbz

formats = {
    'jpg': None,
    'cbz': cbz,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('-f', '--format', default='cbz')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    download(args.url, args.format, args.output)

def download(url: str, format: str, output):
    """download all the files from an nhentai url"""
    try:
        file = formats[format]
    except KeyError:
        raise ValueError(f"unknow option {format}\noptions: {', '.join([key for key in formats])}")

    #parse de html file and get the necessary data
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.title.string.split(' » ')[0] #format the name
    div = soup.find('div', attrs={'id': 'cover'})
    cover_url = div.a.img["data-src"]

    #extract the gallerie id
    id = re.findall('\d*', cover_url)
    id = ''.join(id)

    #create the images folder
    output = output or f'{title}.{format}' #if the outpus is None asing the title
    path = os.path.abspath(f"{os.getcwd()}/{output.split('.')[0]}/")
    if not os.path.exists(path):
        os.makedirs(path)

    print(title)
    print("downloading...")

    #download all images
    for i in itertools.count(1):
        try:
            image_url = f'https://i.nhentai.net/galleries/{id}/{i}.jpg'
            urllib.request.urlretrieve(image_url, os.path.abspath(f'{path}/{str(i).zfill(2)}.jpg'))
        except urllib.error.HTTPError:
            break
        else:
            print(image_url)

    #create the final file
    if file is None:
        print(f"created {os.path.relpath(path)}/")
    else:
        print('Finished Download\ncreacting file...')
        file(path, f'{output}')
        shutil.rmtree(path)
        print(f"created {output}")
