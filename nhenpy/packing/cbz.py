import zipfile
import os

def cbz(folder, name):
    """create an cbz file"""
    with zipfile.ZipFile(os.path.abspath(f'{folder}/../{name}'), 'w') as zipf:
        for filename in os.listdir(folder):
            zipf.write(os.path.abspath(f'{folder}/{filename}'))
