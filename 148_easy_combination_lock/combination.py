#!/usr/bin/python
'''
Print the total rotation increments you've had to rotate to open the lock with the given code:
http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/
'''

import argparse
import sys
import logging

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--debug', action='store_true')
    names = parser.parse_args()
    if names.debug:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(names)

    parameters = raw_input()
    logging.debug("parameters are {}".format(parameters))
    digits,first,second,third = [int(x) for x in parameters.split()]

    travel = 2*digits                 # two full spins to start
    travel += first                   # then spin to first
    travel += digits                  # then one full reverse
    travel += (first-second)%digits   # then reverse spin to second 
    travel += (third-second)%digits   # then forward spin to third
    print travel
    return 0

if __name__ == '__main__':
    sys.exit(main())
