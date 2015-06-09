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
import re
import signal
import sys


FILE_NAME = "lista trabajos hip-hop español.csv"
FIRST_CHAR_PATTERN = re.compile("(\"[0-9 ]*[a-zA-Z])", re.UNICODE)
STR_EXCEPTIONS = ['BBoy', 'BCM', 'BLK', 'BLS', 'BZN', 'BeatKraken', 'CD',
                  'CHR', 'CLS', 'CPV', 'CQD', 'DCP', 'DG', 'DJ', 'DLux', 'DNI',
                  'DPC', 'DVD', 'DVTZ', 'DaCream', 'DobleJota', 'EP', 'EUPMC',
                  'ElSucio', 'FBeats', 'FJ Ramos', 'FK Crew', 'Ferran MDE',
                  'GT Castellano', 'GranPurismo', 'HC', 'HDC', 'HR', 'IFE',
                  'JHT', 'JML', 'JNK', 'JP', 'JPelirrojo', 'JotaJota', 'KAOS',
                  'KFS & Ochoa', 'LG', 'LJDA', 'LP', 'LSK', 'LaFé', 'LaOdysea',
                  'MC', 'MCB', 'MDE', 'NH', 'NeOne', 'NomadaSquaD',
                  'NonDuermas', 'Nora LaRock', 'PFG', 'PGP', 'RCA', 'RNE3',
                  'RdM', 'SDJ', 'SDave', 'SFDK', 'SH', 'SHN', 'SKL69', 'Sr',
                  'Sr.', 'TCap', 'TDK', 'THX', 'TNGHT', 'TV', 'URS', 'VPS',
                  'VSK', 'VV.AA.', 'XChent', 'XL', 'XXL', 'XXX', 'ZNP', 'vs',
                  'yOSEguiré']
ALPHA_MATCH = re.compile("[a-zA-Z \"\(\)]*")


def signal_handler(signal, frame):
    """
    signal_handler(signal, frame)
        Sets handlers for asynchronous events.
    Argumentos:
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


def __repl_str_exc(line):
    """
    __repl_str_ex
        Reemplaza las excepciones de cadena en una línea
    Argumentos:
        - line (string): Línea
    """

    lline = line.split(',')
    result_line = ''

    for field in lline:
        alpha_match = ALPHA_MATCH.search(field)
        if(alpha_match):
            if(alpha_match.group(0) != ''):
                lfield = field.split()
                for word in lfield:
                    for ex in STR_EXCEPTIONS:
                        if(ex.lower() in word.lower()):
                            clean_word = re.search("[a-z]+", word.lower())
                            if(clean_word.group(0) == ex.lower()):
                                field = field.replace(word, ex)
        # Reassembling the string
        result_line = '{0},{1}'.format(result_line, field)

    return result_line.lstrip(',')


def __repl_func(m):
    """
    __repl_func(m)
        Procesa una expresión regular.
    Argumentos:
        - m (regex): expresión regular
    """

    return m.group(1).upper()


def __capitalize_line(line):
    """
    __capitalize_line()
        Pasa a mayúsculas una línea
    Argumentos:
        - line (string): Línea
    """

    capitalized_line = re.sub(FIRST_CHAR_PATTERN, __repl_func, line)

    return (capitalized_line)


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
        capitalized_line = __capitalize_line(line).rstrip('\n')
        formatted_line = __repl_str_exc(capitalized_line)
        fo.write('{0}\n'.format(formatted_line))

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
