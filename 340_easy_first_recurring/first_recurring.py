#! /usr/bin/python

# https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

'''
a program that outputs the first recurring character in a string
'''

from __future__ import unicode_literals, print_function, division, absolute_import

import argparse
import sys
import logging

def determine_first_recurring(s): # pylint: disable=C0103
    "Given string s, determine the first recurring character"

    counts = {}
    answer = None
    for char in s:
        counts[char] = 1 + counts.get(char, 0)
        logging.debug("char: %s, count: %d", char, counts[char])
        if counts[char] > 1:
            answer = char
            break
    return answer

def main(args=None):
    "Main entry point"
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--debug', action="store_true")
    args_ns = parser.parse_args(args)
    if args_ns.debug is True:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(args_ns)

    for line in sys.stdin:
        answer = determine_first_recurring(line.strip())
        print(answer)

    return 0

if __name__ == '__main__':
    sys.exit(main())
