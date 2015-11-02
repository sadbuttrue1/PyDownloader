import os
import urllib
from bs4 import BeautifulSoup

__author__ = 'true'


def download(args):
    base_url = args.url
    if args.dir:
        directory = args.dir
    else:
        directory = ''
    if args.retries:
        retries = args.retries
    else:
        retries = 10
    if args.subdirs:
        for subdir in args.subdirs:
            inside(base_url, subdir, directory, retries)
    else:
        inside(base_url, '', directory, retries)


def inside(base_url, subdir, directory, retries):
    # TODO skip on fail
    page = urllib.request.urlopen(base_url + subdir, retries=retries)
    soup = BeautifulSoup(page.read(), "html.parser")
    for a in soup.find_all('a'):
        link = a.get('href')
        if '.' in link:
            full_path = directory + base_url + subdir
            if not os.path.exists(full_path):
                os.makedirs(full_path)
            #     TODO catch fails
            urllib.request.retrieve(base_url + subdir + link, full_path + link)
        else:
            inside(base_url, subdir + link, directory, retries)
    soup.decompose()
    page.close()
