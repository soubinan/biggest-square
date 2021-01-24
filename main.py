#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

def find_square():
    print('Find square')


class Map:
  def __init__(self, map_file_path=''):
    print(os.getcwd(), os.path.abspath(map_file_path))
    try:
        with open(map_file_path) as f:
            [print(line) for line in f.readlines()]
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    find_square()
