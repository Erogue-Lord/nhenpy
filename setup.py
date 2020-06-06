#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='nhenpy',
      version='1.1',
      description='Command line tool for downloading content from nhentai',
      author='Erogue Lord',
      author_email='maarmota42@gmail.com',
      url='https://github.com/Erogue-Lord/nhenpy',
      packages=find_packages(),
      license = 'MIT',
      entry_points={
        'console_scripts': [
            'nhenpy = nhenpy.downloader:main',
        ],
      },
      install_requires=[
          'requests',
          'beautifulsoup4'
      ],
     )
