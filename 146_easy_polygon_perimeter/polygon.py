#! /usr/bin/python
'''
A program to calculate polygon perimeters, to solve the challenge posted at:
http://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/
'''

# http://en.wikipedia.org/wiki/Regular_polygon#Circumradius
# r = s / (2*sin(Pi/n))

# therefore
# s = r * 2 * sin(Pi/n)
# circumference = n*s


import argparse
import sys
import math
import logging

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--debug', action='store_true')
    res = parser.parse_args()
    if res.debug:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(res)
    n,r = raw_input().split()
    n = int(n)
    r = float(r)
    logging.debug("n is {}, r is {}".format(n,r))
    c = n * r * 2 * math.sin(math.pi/n)
    print "{:.3f}".format(c)
    return 0

if __name__ == '__main__':
    sys.exit(main())
