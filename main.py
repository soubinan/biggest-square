#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
import os
import sys
import logging

from map_gen import map_gen

# Logging definition
handler = logging.StreamHandler()
log_format = logging.Formatter(f'[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler.setFormatter(log_format)
logger.addHandler(handler)


class Map:
    def __init__(self, input=''):
        self.parsed = True if isinstance(input, list) else False
        self.lines = input
        self._empty_symbol = ''
        self._obstacle_symbol = ''
        self._filled_symbol = ''
        self._content = []

        try:
            if not self.parsed:
                with open(input, encoding="utf8", errors='ignore') as f:
                    self.lines = f.readlines()

            if len(self.lines) >= 2:
                firs_line = self.lines[0] # First line
                content_lines = self.lines[1:] # Ignore the last line

                try:
                    *_, \
                        self._empty_symbol, \
                            self._obstacle_symbol, \
                                self._filled_symbol, _ = firs_line
                except (TypeError, ValueError) as e:
                    pass

                for line in content_lines:
                    self._content.append(line)

        except FileNotFoundError as e:
            logger.critical(f'Error: {e}')


    def validate_map(self, verbose=True):
        is_valid = True
        symbols_rules = {self._empty_symbol, 
                         self._obstacle_symbol, 
                         self._filled_symbol
                         }
        # Check content
        if is_valid and \
        (not self._empty_symbol or not self._obstacle_symbol \
        or not self._filled_symbol or not self._content): 
            is_valid = False

        # Check if all lines have the same length
        if is_valid and self._content \
            and any((len(i) != len(self._content[0]) for i in self._content)):
            is_valid = False

        # Check if all lines have newline charactere
        if is_valid and self._content \
            and any((i[-1] != '\n' for i in self._content)):
            is_valid = False

        # Check if symbols rules are respected
        if is_valid:
            symbols = set()

            for line in self._content:
                symbols.update(set(line[:-1]))

            if any(symbol not in symbols_rules for symbol in symbols):
                is_valid = False

        # Write on stderr if Map not valid
        if not is_valid and verbose: logger.error('Map Error\n')

        return is_valid


    def print_map(self, map=None):
        printable = ''

        map_ = map or self._content

        for line in map_:
            printable += line
        print('\n' + printable)
        return printable


    def detect_biggest_square(self):
        if self.validate_map(verbose=False):
            rows_number = len(self._content)
            columns_number = len(self._content[0][:-1])

            size_map = [[0 for m in range(columns_number)] \
                for n in range(rows_number)]

            # Detect the biggest size possible
            for i in range(rows_number): 
                for j in range(columns_number): 
                    if (self._content[i][j] == self._empty_symbol): 
                        size_map[i][j] = min(
                            size_map[i][j-1], 
                            size_map[i-1][j], 
                            size_map[i-1][j-1]
                            ) + 1
                    else: 
                        size_map[i][j] = 0

            maximums = list(max(row) for row in size_map)
            max_of_max = max(maximums)
            max_row = maximums.index(max_of_max)
            max_column = size_map[max_row].index(max_of_max)
            return max_of_max, max_row, max_column # Size, End row, End Column
        return None


    def fill_map(self):
        if self.validate_map():
            size, end_row, end_col = self.detect_biggest_square()
            start_row = end_row + 1 - size
            start_col = end_col + 1 - size
            transformation = []
            print('\n')
            print('-------Input:', self.lines[0])
            self.print_map()

            for i, row in enumerate(self._content):
                transformation.append(list(row))
                if start_row <= i <= end_row:
                    transformation[i][start_col:end_col+1] = self._filled_symbol * size

            result = [''.join(t) for t in transformation]
            print('-------Output')
            self.print_map(result)

            return result


# Context manager to capture stdout from any function in a list
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def generate_map_file(column_number=0, row_number=0, density=0):
    with Capturing() as output:
        map_gen(column_number, row_number, density)

    return list(l + '\n' for l in output)


def run(arg=None):

    if arg:
        return Map(arg).fill_map()

    processing_queue = []

    if len(sys.argv) > 1:
        processing_queue = sys.argv[1:]
    else:
        for root, _, files in os.walk(os.path.abspath('./tests/samples/')):
            for file in files:
                processing_queue.append(os.path.join(root, file))

    for entry in processing_queue:
        Map(entry).fill_map()


if __name__ == '__main__':
    run()
