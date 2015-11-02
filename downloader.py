from datetime import datetime
import logging
import os
import urllib.request
from bs4 import BeautifulSoup
import sys

__author__ = 'true'


def download(args):
    base_url = args.url
    if args.dir:
        directory = args.dir
    else:
        directory = ''
    if args.retries:
        retries = int(args.retries)
    else:
        retries = 10
    if args.subdirs:
        for subdir in args.subdirs:
            inside(base_url, subdir, directory, retries)
    else:
        inside(base_url, '', directory, retries)


def inside(base_url, subdir, directory, retries):
    retried = 0
    page_opened = False
    while retried < retries and not page_opened:
        try:
            page = urllib.request.urlopen(base_url + subdir)
            # TODO detect files and save it
            # print(page.info())
            page_opened = True
        except:
            retried += 1
            page_opened = False
            continue
    if not page_opened:
        logging.warning('at %s\nfailed to open %s, skipping\n error: %s', datetime.now(), base_url + subdir,
                        sys.exc_info())
        return
    soup = BeautifulSoup(page.read(), "html.parser")
    for a in soup.find_all('a'):
        link = a.get('href')
        if '?' not in link:
            if '.' in link:
                full_path = directory + base_url + subdir
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
                file_saved = False
                retried = 0
                while retried < retries and not file_saved:
                    try:
                        file = urllib.request.URLopener()
                        file.retrieve(base_url + subdir + link, full_path + link)
                        file_saved = True
                    except:
                        retried += 1
                        file_saved = False
                        continue
                if not file_saved:
                    logging.warning('at %s\nfailed to save %s, skipping\n error: %s', datetime.now(), base_url + subdir,
                                    sys.exc_info())
            else:
                inside(base_url, subdir + link, directory, retries)
    soup.decompose()
    page.close()
