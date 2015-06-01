#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      capitalize/capitalize.py
"""

# Python version: >= 2.7 & <3
import os
import signal
import sys


FILE_NAME = "lista trabajos hip-hop español.csv"


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
        Limpia la consola.
    """

    if 'nt' in os.name:
        os.system('cls')
    elif 'posix' in os.name:
        os.system('clear')


def __capitalize_lines():
    """
    __capitalize_lines()
        Pasa a mayúsculas cada línea del fichero.
    """

    f_name, f_ext = os.path.splitext(FILE_NAME)
    output_file = '{0} - Capitalized{1}'.format(f_name, f_ext)

    f = open(FILE_NAME, 'r')
    fo = open(output_file, 'w+')

    for line in f:
        fo.write(line.title())

    f.close()
    fo.close()


if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)

    if(os.path.isfile(FILE_NAME)):
        __clear_screen()
        print 'Capitalizing \'{0}\'...'.format(FILE_NAME)
        __capitalize_lines()
    else:
        print '{0} is not a file.'.format(FILE_NAME)
