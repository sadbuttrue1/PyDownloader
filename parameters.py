import argparse

__author__ = 'true'

parser = argparse.ArgumentParser()
parser.add_argument('url', help='url that we want to download')
parser.add_argument('-d', '--dir', help='where we download (by default – in current script folder)')
parser.add_argument('-s', '--subdirs', nargs='+', help='set of subdirs')
parser.add_argument('-r', '--retries', help='count of retries (default 10)')
args = parser.parse_args()
