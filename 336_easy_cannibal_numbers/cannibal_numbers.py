#! /usr/bin/python

# https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

'''
given two integers, i and j, on the first line
read i numbers from the second line
read j queries from the third line

for each query, determine how many numbers can eat and grow
to have a value of at least the query
'''

from __future__ import unicode_literals, print_function, division, absolute_import

import argparse
import sys
import logging

def count_vals_fulfilling_query(v, query): # pylint: disable=C0103
    "Given value list v, determine the number of items fulfilling query q"

    fulfilled = 0
    working_values = list(reversed(sorted(v)))

    # dangerously and foolishly mutate the list in place,
    # will loop forever if you forget a pop()
    while working_values:
        # print(fulfilled, working_values)
        if working_values[0] >= query:
            fulfilled += 1
            working_values.pop(0) # winner
        else:
            working_values[0] += 1
            working_values.pop() # consumed
    # print(fulfilled)

    return fulfilled

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

    counts = sys.stdin.readline()
    (how_many_values, number_of_queries) = list(map(int, counts.split()))

    valuestring = sys.stdin.readline()
    values = list(map(int, valuestring.split()))
    if len(values) != how_many_values:
        raise ValueError("wrong number of inputs (expected {})".format(how_many_values))

    queriestring = sys.stdin.readline()
    queries = list(map(int, queriestring.split()))
    if len(queries) != number_of_queries:
        raise ValueError("wrong number of queries (expected {})".format(number_of_queries))

    results = []
    for q in queries:
        c = count_vals_fulfilling_query(values, q)
        results.append(str(c))

    return " ".join(results)

if __name__ == '__main__':
    sys.exit(main())
