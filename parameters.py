import argparse

__author__ = 'true'

parser = argparse.ArgumentParser()
parser.add_argument('url', help='url that we want to download')
parser.add_argument('-d', '--dir', help='where we download (by default – in current script folder)')
parser.add_argument('-s', '--subdirs', nargs='+', help='set of subdirs')
parser.add_argument('-r', '--retries', type=int, help='count of retries (default 10)')
parser.add_argument('-t', '--multithread', help='enable multithreading', action='store_true')
args = parser.parse_args()
