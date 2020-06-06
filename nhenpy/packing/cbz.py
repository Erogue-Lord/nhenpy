import zipfile
import os

def cbz(folder, name):
    with zipfile.ZipFile(os.path.abspath(f'{folder}/../{name}.cbz'), 'w') as zipf:
        for filename in os.listdir(folder):
            zipf.write(os.path.abspath(f'{folder}/{filename}'))
