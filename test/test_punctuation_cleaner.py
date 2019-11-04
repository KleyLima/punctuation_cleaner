# -*- coding: utf-8 -*-

import unittest
from source.punctuation_cleaner import PunctuationCleaner


class TestCleaner(unittest.TestCase):
    def setUp(self):
        self.to_format = open('./test/fixtures/basic.txt')
        self.result = open('./test/fixtures/basic_formtd.txt')
        self.test = PunctuationCleaner(self.to_format)
        print('Testing basic.txt')

    def test_clean(self):
        self.assertEqual(self.test.clean(), self.result.read())

    def tearDown(self):
        self.to_format.close()
        self.result.close()

if __name__ == '__main__':
    unittest.main()
