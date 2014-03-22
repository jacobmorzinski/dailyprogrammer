#! /usr/bin/python
'''
http://www.reddit.com/r/dailyprogrammer/comments/20l2it/17042014_challenge_153_easy_pascals_pyramid/
'''

import argparse
import sys
import collections
import logging
#logging.basicConfig(level=logging.DEBUG)

def triangle(n):
    '''Return a Pascal's Triangle'''
    # For generation N,
    # child[i] = parent[i-1] + parent[i]

    rows = []
    for row in xrange(n):
        if row==0:
            child = collections.defaultdict(int)
            child[0] = 1
        else:
            parent = rows[row-1]
            child = collections.defaultdict(int)
            for i in xrange(row+1):
                child[i] = parent[i] + parent[i-1]
            # Child is done.  Remove zeros that were created in parent.
            for k in parent.keys():
                if parent[k] == 0:
                    del(parent[k])
        rows.append(child)
        # end: for row in xrange(n)

    output = []
    for row in rows:
        fmt = lambda x: '{:4}'.format(x) # pad input into 4-wide string
        output.append( ' '.join(map(fmt,row.values())) )
    return '\n'.join(output)
    

def dict_int_factory():
    return collections.defaultdict(int)

def dict_dict_int_factory():
    return collections.defaultdict(dict_int_factory)

def pyramid(n):
    '''Return a Pascal's Pyramid'''
    # For generation N,
    # child[x,y] = parent[x,y] + parent[x,y-1] + parent[x-1,y-1]


    planes = []
    for plane in xrange(n):
        if plane==0:
            child = dict_dict_int_factory()
            child[0][0] = 1
        else:
            parent = planes[plane-1]
            child = dict_dict_int_factory()
            for i in xrange(plane+1):
                logging.debug("i is {}".format(i))
                logging.debug(parent)
                for j in xrange(i+1):
                    child[j][i] = parent[j][i] + parent[j][i-1] + parent[j-1][i-1]
                logging.debug(child)
            # Child is done.  Remove zeros that were created in parent.
            for i in parent.keys():
                for j in parent[i].keys():
                    if parent[i][j] == 0:
                        del(parent[i][j])
                if parent[i] == {}:
                    del(parent[i])
        logging.debug(child.items())
        planes.append(child)
        # end: for plane in xrange(n)

    output = []
    result = planes[-1]
    for i in xrange(n):
        fmt = lambda x: '{:4}'.format(x) # pad input into 4-wide string
        output.append( ' '.join(map(fmt,result[i].values())) )
    output.reverse()
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number', nargs='?', type=int,
                        help='Size of triangle or pyramid')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--triangle', action='store_const',
                      dest='mode', const='triangle',
                      help='Triangle mode')
    mode.add_argument('--pyramid', action='store_const',
                      dest='mode', const='pyramid',
                      help='Pyramid mode')
    parser.set_defaults(mode='pyramid')
    res = parser.parse_args()
    logging.debug(res)

    n = res.number
    if n is None:
        prompt = "What is N: " if sys.stdin.isatty() else ""
        n = int(raw_input(prompt))

    if res.mode == 'triangle':
        print triangle(n)
    elif res.mode == 'pyramid':
        print pyramid(n)
    else:
        raise Exception("Unknown mode: {}".format(res.mode))

    return 0

if __name__ == '__main__':
    sys.exit(main())
