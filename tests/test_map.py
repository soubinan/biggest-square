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
        self.assertEqual(self.map_01.validate_map, False)
        self.assertEqual(self.map_02.validate_map, False)
        self.assertEqual(self.map_03.validate_map, False)
        self.assertEqual(self.map_04.validate_map, False)
        self.assertEqual(self.map_05.validate_map, False)
        self.assertEqual(self.map_06.validate_map, False)

        self.assertEqual(self.map_07.validate_map, True)
        self.assertEqual(self.map_08.validate_map, True)
        self.assertEqual(self.map_09.validate_map, True)

        self.assertEqual(self.map_10.validate_map, True)
        self.assertEqual(self.map_11.validate_map, True)
        self.assertEqual(self.map_12.validate_map, True)

        self.assertEqual(self.map_13.validate_map, True)
        self.assertEqual(self.map_14.validate_map, True)
        self.assertEqual(self.map_15.validate_map, True)
        self.assertEqual(self.map_16.validate_map, True)
        self.assertEqual(self.map_17.validate_map, True)
        self.assertEqual(self.map_18.validate_map, True)

        self.assertEqual(self.map_19.validate_map, True)


    def test_get_maximum_possible_size(self):
        self.assertEqual(self.map_01.get_maximum_possible_size, 0)
        self.assertEqual(self.map_02.get_maximum_possible_size, 0)
        self.assertEqual(self.map_03.get_maximum_possible_size, 0)
        self.assertEqual(self.map_04.get_maximum_possible_size, 0)
        self.assertEqual(self.map_05.get_maximum_possible_size, 0)
        self.assertEqual(self.map_06.get_maximum_possible_size, 0)

        self.assertEqual(self.map_07.get_maximum_possible_size, 8)
        self.assertEqual(self.map_08.get_maximum_possible_size, 2)
        self.assertEqual(self.map_09.get_maximum_possible_size, 1)

        self.assertEqual(self.map_10.get_maximum_possible_size, 10)
        self.assertEqual(self.map_11.get_maximum_possible_size, 10)
        self.assertEqual(self.map_12.get_maximum_possible_size, 10)

        self.assertEqual(self.map_13.get_maximum_possible_size, 9)
        self.assertEqual(self.map_14.get_maximum_possible_size, 8)
        self.assertEqual(self.map_15.get_maximum_possible_size, 9)
        self.assertEqual(self.map_16.get_maximum_possible_size, 10)
        self.assertEqual(self.map_17.get_maximum_possible_size, 10)
        self.assertEqual(self.map_18.get_maximum_possible_size, 10)

        self.assertEqual(self.map_19.get_maximum_possible_size, 9)

