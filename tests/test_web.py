#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests

import app


class TestMapValidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.req01 = requests.get('http://localhost:8080')
        cls.req02 = requests.get('http://localhost:8080/test')
        cls.req03 = requests.get('http://localhost:8080?map1=12-12-5')
        cls.req04 = requests.get('http://localhost:8080/path?map1=15-15-8')


    def test_response(self):
        self.assertEqual(self.req01.status_code, 200)
        self.assertEqual(self.req02.status_code, 404)
        self.assertEqual(self.req03.status_code, 200)
        self.assertEqual(self.req04.status_code, 404)


    def test_content(self):
        self.assertEqual('<h1>Biggest Square</h1>' in self.req01.text, True)
        self.assertEqual('404 Not Found' in self.req02.text, True)
        self.assertEqual('<h1>Biggest Square</h1>' in self.req03.text, True)
        self.assertEqual('404 Not Found' in self.req04.text, True)
