#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging


# Logging definition
handler = logging.StreamHandler()
log_format = logging.Formatter(f'[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler.setFormatter(log_format)
logger.addHandler(handler)


def find_square():
    print('Find square')


class Map:
    def __init__(self, map_file_path=''):
        self.location = map_file_path
        self._empty_symbol = ''
        self._obstacle_symbol = ''
        self._filled_symbol = ''
        self._content = []

        try:
            with open(self.location) as f:
                lines = f.readlines()

                if len(lines) >= 2:
                    firs_line = lines[0] # First line
                    content_lines = lines[1:] # Ignore the last line

                    try:
                        lines_number, \
                            self._empty_symbol, \
                                self._obstacle_symbol, \
                                    self._filled_symbol, *_ = firs_line
                    except (TypeError) as e:
                        pass

                    for line in content_lines:
                        self._content.append(line)

        except FileNotFoundError as e:
            logger.critical(f'Error: {e}')


    def validate_map(self):
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
        if not is_valid: logger.error('Map Error\n')

        return is_valid


if __name__ == '__main__':
    m = Map('./tests/samples/bad-4')
    m.validate_map()
