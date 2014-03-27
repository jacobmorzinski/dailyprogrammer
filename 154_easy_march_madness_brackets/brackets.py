#!/usr/bin/python
'''
A program to validate spoit points, to solve the challenge posted at:
http://www.reddit.com/r/dailyprogrammer/comments/1undyd/010714_challenge_147_easy_sport_points/
'''

import argparse
import sys
import logging
import pyparsing as p

def printToken(s,loc,toks):
    logging.debug( "{} {} {}".format(s,loc,toks) )
    print toks
    return []

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

    nest = p.Forward()
    lparen = p.Literal("(").suppress()
    rparen = p.Literal(")").suppress()
    lbracket = p.Literal("[").suppress()
    rbracket = p.Literal("]").suppress()
    lbrace = p.Literal("{").suppress()
    rbrace = p.Literal("}").suppress()
    word = p.Word(p.alphas)
    words = p.OneOrMore(word | nest)
    parenwords = lparen + words + rparen
    bracketwords = lbracket + words + rbracket
    bracewords = lbrace + words + rbrace
    nest <<= (parenwords | bracketwords | bracewords)
    nest.addParseAction(printToken)
    parser = nest
    try:
        tokens = parser.parseString(phrase)
        tokenlist = tokens.asList()
        print "tokens = " + str(tokens)
        print "tokenlist = " + str(tokenlist)
    except p.ParseBaseException as err:
        print err.line
        print err
    return 0

if __name__ == '__main__':
    sys.exit(main())
