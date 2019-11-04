# -*- coding: utf-8 -*-

from re import sub
from sys import stdin

class PunctuationCleaner:
    def __init__(self, text):
        self.text = text

    def clean(self):
        edited = ''
        for line in self.text:
            edited += sub('\W', ' ', line)
            edited += '\n'
        return edited


if __name__ == '__main__':
    print(PunctuationCleaner(stdin).clean())

