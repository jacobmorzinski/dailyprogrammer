#! /usr/bin/python
'''
A program to print trees, to solve the challenge posted at:
http://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/
'''

import argparse
import sys
import logging
#logging.basicConfig(level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    res = parser.parse_args()
    logging.debug(res)
    width,bottom,top = raw_input().split()
    width = int(width)
    logging.debug("width is {}, bottom is {}, top is {}".format(width,bottom,top))
    if width%2 == 0:
        raise Exception("width must be odd")
    for i in range(1,2+width/2):
        print " "*(1+width/2-i) + top*(i*2 -1)
    print " "*(width/2 -1) + bottom*3
    return 0

if __name__ == '__main__':
    sys.exit(main())
