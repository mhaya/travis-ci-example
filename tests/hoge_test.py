# coding:utf-8

import unittest
from hoge import Hoge

class HogeTest(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_first(self):
        print('test_first')

    def test_hoge(self):
        hoge = Hoge()
        self.assertTrue(hoge.index())


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite

