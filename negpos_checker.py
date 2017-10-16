#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

import os
from six.moves import urllib


SOURCE_URL = "http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/"
DICT_DIR = 'jp_negpos_dict'
NOUN_FILE = 'pn.csv.m3.120408.trim'
VERB_FILE = 'wago.121808.pn'


class NegPosChecker(object):

    def __init__(self):
        noun_filepath = self._maybe_download(NOUN_FILE)
        verb_filepath = self._maybe_download(VERB_FILE)
        self.noun_dict = self._create_noun_dict(noun_filepath)
        self.verb_dict = self._create_verb_dict(verb_filepath)

    def _maybe_download(self, filename):
        if not os.path.isdir(DICT_DIR):
            os.makedirs(DICT_DIR)
        filepath = os.path.join(DICT_DIR, filename)
        if not os.path.isfile(filepath):
            filepath, _ = urllib.request.urlretrieve(SOURCE_URL + filename, filepath)
            size = os.path.getsize(filepath)
            print('Successfully downloaded', filename, size, 'bytes.')
        return filepath

    def _create_noun_dict(self, filepath):
        noun_dict = {}
        with open(filepath) as f:
            for line in f:
                cols = line.split('\t')
                if cols[1] == 'p':
                    noun_dict[cols[0]] = 1
                elif cols[1] == 'n':
                    noun_dict[cols[0]] = -1
                elif cols[1] == 'e':
                    noun_dict[cols[0]] = 0
        return noun_dict

    def _create_verb_dict(self, filepath):
        verb_dict = {}
        with open(filepath) as f:
            for line in f:
                line = line.rstrip()
                cols = line.split('\t')
                if len(cols) < 2:
                    continue
                word = cols[1].replace(' ', '')
                if 'ポジ' in cols[0]:
                    verb_dict[word] = 1
                elif 'ネガ' in cols[0]:
                    verb_dict[word] = -1
        return verb_dict

    def check(self, target, category='unknown'):
        if isinstance(target, list):
            for word in target:
                ret = self._check(word, category)
                if ret is not None:
                    return ret
            return None
        else:
            return self._check(target, category)


    def _check(self, word, category):
        if category == 'noun':
            if word in self.noun_dict:
                return self.noun_dict[word]
            return None
        elif category == 'verb':
            if word in self.verb_dict:
                return self.verb_dict[word]
            return None
        elif category == 'unknown':
            if word in self.noun_dict:
                return self.noun_dict[word]
            elif word in self.verb_dict:
                return self.verb_dict[word]
            return None


