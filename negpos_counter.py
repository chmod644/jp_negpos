#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

import os
import argparse
import sys

from janome.tokenizer import Tokenizer
from negpos_checker import NegPosChecker


def main():
    args = parse_args()

    if args.str is None and args.file is None:
        print("Error: str or file must be assigned.", file=sys.stderr)
        sys.exit(-1)

    if args.str is not None:
        target_str = args.str
    else:
        with open(args.file) as f:
           target_str = f.read(f)

    count = count_negpos(target_str)

    print(count)


def tokenize(target_str):
    target_str = target_str.decode('utf-8')
    t = Tokenizer()
    tokens = t.tokenize(target_str)
    return tokens


def count_negpos(target_str):
    tokens = tokenize(target_str)
    negpos_dict = {
            'positive': 0,
            'negative': 0,
            'neutral': 0
            }

    checker = NegPosChecker()

    for token in tokens:
        base_form = token.base_form.encode('utf-8')
        base_form = token.base_form.encode('utf-8')
        result = checker.check([token.base_form.encode('utf-8')])
        if result == 1:
            negpos_dict['positive'] += 1
        elif result == -1:
            negpos_dict['negative'] += 1
        elif result == 0:
            negpos_dict['neutral'] += 1
    return negpos_dict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', '-s', type=str, required=False, default=None, help="input string")
    parser.add_argument('--file', '-f', type=str, required=False, default=None, help="input file")
    return parser.parse_args()


if __name__ == '__main__':
    main()

