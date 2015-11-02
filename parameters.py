import argparse

__author__ = 'true'

parser = argparse.ArgumentParser()
parser.add_argument('url', help='url that we want to download')
parser.add_argument('--subdirs', nargs='+', help='set of subdirs')
args = parser.parse_args()
