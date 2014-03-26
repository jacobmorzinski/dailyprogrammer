#!/usr/bin/python
'''
Remove vowels from input text.
http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
'''

import argparse
import sys
import logging
import re

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--debug', action='store_true')
    names = parser.parse_args()
    if names.debug:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(names)

    phrase = None
    if phrase is None:
        prompt = ""
        if sys.stdin.isatty() and sys.platform != 'cli':
            prompt = "What is the phrase: "
        phrase = raw_input(prompt)
    logging.debug("phrase is {}".format(phrase))

    pattern_dev = re.compile(r'[aeiou]| ',  re.IGNORECASE)
    pattern_v   = re.compile(r'[^aeiou]| ', re.IGNORECASE)
    devoweled = re.sub(pattern_dev, '', phrase)
    voweled   = re.sub(pattern_v,   '', phrase)

    print devoweled
    print voweled
    return 0

if __name__ == '__main__':
    sys.exit(main())
