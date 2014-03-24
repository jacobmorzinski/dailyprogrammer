#! /usr/bin/python
'''
A program to print differences in prices, to solve the challenge posted at:
http://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/
'''

'''
Sample Input
4
CarriageBolt 45
Eyebolt 50
Washer 120
Rivet 10
CarriageBolt 45
Eyebolt 45
Washer 140
Rivet 10

Sample Output
Eyebolt -5
Washer +20
'''

import argparse
import sys
import logging
#logging.basicConfig(level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    res = parser.parse_args()
    logging.debug(res)
    n = int(raw_input())
    logging.debug("n is {}".format(n))
    old_prices = {}
    new_prices = {}
    for i in xrange(n):
        line = raw_input()
        j = line.rfind(" ")
        name = line[:j]
        price = int(line[j+1:])
        old_prices[name] = price
    logging.debug(old_prices)
    for i in xrange(n):
        line = raw_input()
        j = line.rfind(" ")
        name = line[:j]
        price = int(line[j+1:])
        new_prices[name] = price
    logging.debug(new_prices)
    for _,k in enumerate(new_prices):
        difference = new_prices[k] - old_prices[k]
        if difference != 0:
            print k, difference
    return 0

if __name__ == '__main__':
    sys.exit(main())
