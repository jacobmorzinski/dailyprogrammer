#!/usr/bin/python
'''
A program to validate spoit points, to solve the challenge posted at:
http://www.reddit.com/r/dailyprogrammer/comments/1undyd/010714_challenge_147_easy_sport_points/
'''

import argparse
import sys
import logging

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('score', nargs='?', type=int,
                        help='Score')
    parser.add_argument('--debug', action='store_true')
    names = parser.parse_args()
    if names.debug:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(names)

    score = names.score
    if score is None:
        prompt = ""
        if sys.stdin.isatty() and sys.platform != 'win32':
            prompt = "What is the score: "
        score = int(raw_input(prompt))
    logging.debug("score is {}".format(score))

    if score in (1,2,4,5):
        print "Invalid Score"
    else:
        print "Valid Score"
    return 0

if __name__ == '__main__':
    sys.exit(main())
