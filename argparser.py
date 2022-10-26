import argparse

parser = argparse.ArgumentParser(description='Cleaner')
parser.add_argument('file', metavar='file', type=str, nargs='+')

args = parser.parse_args()
