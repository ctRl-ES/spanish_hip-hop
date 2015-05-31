#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@file:      find_repeated.py
"""

# Python version: >= 2.7 & <3
import difflib
import os
import re
import signal
import string
import sys

FILE_NAME = "lista trabajos hip-hop español.csv"
MATCH_THRESHOLD = 0.90  # Seems a reasonable threshold


class Disk():
    """
    Represents a file entry
    """

    artist = None
    title = None
    year = None
    type = None

    def __init__(self, line):
        l_line = line.split(',')
        self.artist = l_line[0].strip()
        self.title = l_line[1].strip()
        self.year = l_line[2].strip()
        self.type = l_line[3].strip()

    def to_string(self):
        return '{0} {1} {2} {3}'.format(self.artist, self.title, self.year,
                                        self.type).replace("\"", '')


def signal_handler(signal, frame):
    """
    signal_handler(signal, frame)
        Sets handlers for asynchronous events.
    Arguments:
        - signal: Signal number.
        - frame:  Current stack frame.
    """

    print '\nStopping...'
    sys.exit(0)


def __clear_screen():
    """
    __clear_screen()
        Clears the screen.
    """

    if 'nt' in os.name:
        os.system('cls')
    elif 'posix' in os.name:
        os.system('clear')


def __get_match_ratio(disk1, disk2):
    """
    __get_match_ratio(str_disk1, str_disk2)
        Compares two Disk objects.
    Arguments:
        - disk1: (Disk) item one.
        - disk2: (Disk) item two.
    """

    # Normalization
    str_disk1 = "{0} {1}".format(disk1.artist, disk1.title)
    str_disk2 = "{0} {1}".format(disk2.artist, disk2.title)

    for p in string.punctuation:
        str_disk1.replace(p, '')
        str_disk2.replace(p, '')

    # Replace multiple spaces for one space
    str_disk1 = re.sub('\s+', str_disk1, ' ')
    str_disk2 = re.sub('\s+', str_disk2, ' ')

    # Get match ratio
    match_ratio = difflib.SequenceMatcher(None, str_disk1, str_disk2).ratio()

    return match_ratio


def __compare_lists_items(l1, l2):
    """
    __compare_lists_items(l1, l2)
        Searchs if exists every element of l1 in l2
    Arguments:
        - l1: (list) List one.
        - l2: (list) List two.
    """

    for i1 in l1:
        matches = 0
        for i2 in l2:
            match_ratio = __get_match_ratio(i1, i2)
            if(match_ratio > MATCH_THRESHOLD):
                matches = matches + 1
                """
                matches > 1
                We are searching on the same list.
                There's always be 1 match.
                """
                if(matches > 1):
                    if(match_ratio == 1):
                        print 'Duplicated!: \'{0}\''.format(i1.to_string())
                    else:
                        print 'Possible duplicated: \'{0}\' ({1}% coincidence with \'{2}\')'.format(i1.to_string(), round((match_ratio * 100), 2), i2.to_string())
                    l2.remove(i2)


def __get_file_list():
    """
    __get_file_list(file_name)
        Gets file content as a list of objects
    """

    l_file = []

    f = open(FILE_NAME)
    for line in f:
        # TODO: COGER OBJETOS Y TRABAJARLOS
        # l_entry = line.split(',')
        # disk = Disk(l_entry[0], l_entry[1])
        disk = Disk(line)
        l_file.append(disk)

    f.close()

    return sorted(l_file)


def __search_repeated():
    """
    __search_repeated
        Searchs for repeated lines inside the file.
    """

    l_lines_in_file = __get_file_list()
    l_lines_in_file_copy = l_lines_in_file[:]
    __compare_lists_items(l_lines_in_file, l_lines_in_file_copy)


if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)

    if(os.path.isfile(FILE_NAME)):
        __clear_screen()
        print 'Searching for repeated entries in \'{0}\'...'.format(FILE_NAME)
        __search_repeated()
    else:
        print '{0} is not a file.'.format(FILE_NAME)
