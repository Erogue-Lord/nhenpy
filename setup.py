#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='yahd',
      version='1.0',
      description='Command line tool for downloading content from nhentai',
      author='Erogue Lord',
      author_email='maarmota42@gmail.com',
      url='https://github.com/Erogue-Lord/yahd',
      packages=find_packages(),
      license = 'MIT',
      entry_points={
        'console_scripts': [
            'yahd = yahd.downloader:main',
        ],
      },
      install_requires=[
          'requests',
          'beautifulsoup4'
      ],
     )
