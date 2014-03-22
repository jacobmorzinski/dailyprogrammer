#! /usr/bin/python
'''
http://www.reddit.com/r/dailyprogrammer/comments/20l2it/17042014_challenge_153_easy_pascals_pyramid/
'''

import argparse
import sys
import collections
import logging
logging.basicConfig(level=logging.DEBUG)

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

    

class AutoViviDict(dict):
    def __getitem__(self,item):
        try:
            return dict.__getitem__(self,item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def pyramid(n):
    '''Return a Pascal's Pyramid'''
    # For generation N,
    # child[x,y] = parent[x,y] + parent[x,y-1] + parent[x-1,y-1]

    return 0
    #crash and burn
    planes = []
    for plane in xrange(n):
        if plane==0:
            child = AutoViviDict()
            child[0] = 1
        else:
            parent = planes[plane-1]
            child = AutoViviDict()
            for i in xrange(plane+1):
                child[i] = parent[i] + parent[i-1]
            # Child is done.  Remove zeros that were created in parent.
            for k in parent.keys():
                if parent[k] == 0:
                    del(parent[k])
        print child
        planes.append(child)
        # end: for plane in xrange(n)

    output = []
    for plane in planes:
        fmt = lambda x: '{:4}'.format(x) # pad input into 4-wide string
        output.append( ' '.join(map(fmt,plane.values())) )
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
        n = raw_input(prompt)

    if res.mode == 'triangle':
        print triangle(n)
    elif res.mode == 'pyramid':
        print pyramid(n)
    else:
        raise Exception("Unknown mode: {}".format(res.mode))

    return 0

if __name__ == '__main__':
    sys.exit(main())
