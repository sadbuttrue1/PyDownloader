import logging
from downloader import download
from parameters import args

__author__ = 'true'


def main():
    logging.basicConfig(filename='downloader.log')
    download(args)


if __name__ == '__main__':
    main()
