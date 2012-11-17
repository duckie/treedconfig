#!/usr/bin/python2
# -*- Encoding:UTF-8 -*-
# Code for python 3.x will be provided later

import argparse


class ConfigFile:
    """Class to read and edit a given config file"""
    def __init__(self, filename):
        self.file = filename

    def __del__(self):
        print('delete')



def main():
    parser = argparse.ArgumentParser(description='Tree configuration tool')
    parser.add_argument('cmd', metavar='command', nargs=1, help='The command to execute. Type \'tconf help\' to get a list.')
    parser.add_argument('args', metavar='arguments', nargs='*', help='Command parameters. Type \'tconf help [cmd]\' to get some help.')
    cmdline_args = parser.parse_args()

main()
config = ConfigFile('roger')




