#!/usr/bin/python2
# -*- Encoding:UTF-8 -*-
# Code for python 3.x will be provided later

import argparse
import ConfigParser
import os

#
def getConfigFileName():
    name = '.tconf'
    if(os.environ.__contains__('TCONFFILE')):
        envname = os.environ['TCONFFILE']
        if (0 < len(envname)):
            name = envname

    return name


def getExecutionPath():
    return os.getcwd()

def findLocalConfigFile():
    confname = getConfigFileName()
    name = None
    localpath = getExecutionPath()
    while('/' is not localpath and None is name):
        if(os.path.isfile(localpath + '/' + confname)):
            name = localpath + '/' + confname

        localpath = os.path.dirname(localpath)

    return name

def main():
    parser = argparse.ArgumentParser(description='Tree configuration tool')
    parser.add_argument('cmd', metavar='command', nargs=1, help='The command to execute. Type \'tconf help\' to get a list.')
    parser.add_argument('args', metavar='arguments', nargs='*', help='Command parameters. Type \'tconf help [cmd]\' to get some help.')
    cmdline_args = parser.parse_args()

print(findLocalConfigFile())
main()
#config = ConfigFile('roger')


