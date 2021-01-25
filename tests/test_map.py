#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any
import unittest

from main import Map

class TestMapValidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.map_01 = Map('./tests/samples/bad-1')
        cls.map_02 = Map('./tests/samples/bad-2')
        cls.map_03 = Map('./tests/samples/bad-3')
        cls.map_04 = Map('./tests/samples/bad-4')
        cls.map_05 = Map('./tests/samples/bad-5')
        cls.map_06 = Map('./tests/samples/bad-6')

        cls.map_07 = Map('./tests/samples/easy-1')
        cls.map_08 = Map('./tests/samples/easy-2')
        cls.map_09 = Map('./tests/samples/easy-3')

        cls.map_10 = Map('./tests/samples/normal-1')
        cls.map_11 = Map('./tests/samples/normal-2')
        cls.map_12 = Map('./tests/samples/normal-3')

        cls.map_13 = Map('./tests/samples/hard-1')
        cls.map_14 = Map('./tests/samples/hard-2')
        cls.map_15 = Map('./tests/samples/hard-3')
        cls.map_16 = Map('./tests/samples/hard-4')
        cls.map_17 = Map('./tests/samples/hard-5')
        cls.map_18 = Map('./tests/samples/hard-6')

        cls.map_19 = Map('./tests/samples/exercise-test-input')


    def test_validate_map(self):
        self.assertEqual(self.map_01.validate_map(), False)
        self.assertEqual(self.map_02.validate_map(), False)
        self.assertEqual(self.map_03.validate_map(), False)
        self.assertEqual(self.map_04.validate_map(), False)
        self.assertEqual(self.map_05.validate_map(), False)
        self.assertEqual(self.map_06.validate_map(), False)

        self.assertEqual(self.map_07.validate_map(), True)
        self.assertEqual(self.map_08.validate_map(), True)
        self.assertEqual(self.map_09.validate_map(), True)

        self.assertEqual(self.map_10.validate_map(), True)
        self.assertEqual(self.map_11.validate_map(), True)
        self.assertEqual(self.map_12.validate_map(), True)

        self.assertEqual(self.map_13.validate_map(), True)
        self.assertEqual(self.map_14.validate_map(), True)
        self.assertEqual(self.map_15.validate_map(), True)
        self.assertEqual(self.map_16.validate_map(), True)
        self.assertEqual(self.map_17.validate_map(), True)
        self.assertEqual(self.map_18.validate_map(), True)

        self.assertEqual(self.map_19.validate_map(), True)


    def test_detect_biggest_square(self):
        self.assertEqual(self.map_01.detect_biggest_square(), None)
        self.assertEqual(self.map_02.detect_biggest_square(), None)
        self.assertEqual(self.map_03.detect_biggest_square(), None)
        self.assertEqual(self.map_04.detect_biggest_square(), None)
        self.assertEqual(self.map_05.detect_biggest_square(), None)
        self.assertEqual(self.map_06.detect_biggest_square(), None)

        self.assertEqual(self.map_07.detect_biggest_square(), (8, 7, 7))
        self.assertEqual(self.map_08.detect_biggest_square(), (1, 1, 1))
        self.assertEqual(self.map_09.detect_biggest_square(), (1, 0, 0))

        self.assertEqual(self.map_10.detect_biggest_square(), (6, 9, 9))
        self.assertEqual(self.map_11.detect_biggest_square(), (3, 4, 4))
        self.assertEqual(self.map_12.detect_biggest_square(), (6, 9, 7))

        self.assertEqual(self.map_13.detect_biggest_square(), (2, 1, 1))
        self.assertEqual(self.map_14.detect_biggest_square(), (2, 5, 4))
        self.assertEqual(self.map_15.detect_biggest_square(), (1, 1, 3))
        self.assertEqual(self.map_16.detect_biggest_square(), (1, 1, 3))
        self.assertEqual(self.map_17.detect_biggest_square(), (1, 1, 3))
        self.assertEqual(self.map_18.detect_biggest_square(), (1, 1, 3))

        self.assertEqual(self.map_19.detect_biggest_square(), (7, 6, 11))

