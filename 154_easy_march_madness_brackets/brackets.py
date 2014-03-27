#!/usr/bin/python
'''
Looks for nested bracked wordlists, to solve the challenge posted at:
http://www.reddit.com/r/dailyprogrammer/comments/217klv/4242014_challenge_154_easy_march_madness_brackets/
'''

import argparse
import sys
import logging
import pyparsing as p

wordlist = []

def removeAndSaveTokens(s,loc,toks):
    logging.debug( "string={} loc={} tokens={}".format(s,loc,toks) )
    wordlist.extend(toks)
    return []

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phrase', type=str)
    parser.add_argument('--debug', action='store_true')
    names = parser.parse_args()
    if names.debug:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(names)

    phrase = names.phrase
    if phrase is None:
        prompt = ""
        if sys.stdin.isatty() and sys.platform != 'cli':
            prompt = "What is the phrase: "
        phrase = raw_input(prompt)
    logging.debug("phrase is {}".format(phrase))

    # a word consists of alphabetical letters
    word = p.Word(p.alphas)
    # bookkeeping: name the 'subsection' entity, but don't define it yet
    subsection = p.Forward()
    # a group can be one or more words or sub-sections
    group = p.OneOrMore(word | subsection)
    # groups are bounded by () or [] or {}
    # brackets are parsed but suppressed from the token stream.
    lparen   = p.Literal("(").suppress()
    rparen   = p.Literal(")").suppress()
    lbracket = p.Literal("[").suppress()
    rbracket = p.Literal("]").suppress()
    lbrace   = p.Literal("{").suppress()
    rbrace   = p.Literal("}").suppress()
    parengroup   = lparen   + group + rparen
    bracketgroup = lbracket + group + rbracket
    bracegroup   = lbrace   + group + rbrace
    # a subsection is a bounded group
    subsection <<= (parengroup | bracketgroup | bracegroup)

    # when a bounded subsection is parsed, remove and save its tokens
    subsection.addParseAction(removeAndSaveTokens)

    # All set; we now have a parser that looks for nested bracketed wordlists
    bracketParser = subsection
    try:
        tokens = bracketParser.parseString(phrase)
        # The parseAction collected the tokens into the wordlist
        print " ".join(wordlist)
    except p.ParseBaseException as err:
        print err.line
        print err
    return 0

if __name__ == '__main__':
    sys.exit(main())
