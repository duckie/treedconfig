#!/usr/bin/python2
# -*- Encoding:UTF-8 -*-
# Code for python 3.x will be provided later

import argparse
import ConfigParser
import os, sys

class Logger:
    I = 0 # I stands for 'Info'
    W = 1 # W stands for 'Warning'
    E = 2 # E stands for 'Error'
    F = 3 # F stands for 'Fatal'
    verbosity = False

    def __init__(self, verbosity):
        self.verbosity = verbosity
 
    def log(self, message, errlevel = 3):
        if(self.verbosity or self.F == errlevel):
            prefix = 'tconf'
            if self.verbosity:
                if self.I == errlevel:
                    prefix += ' info'
                if self.W == errlevel:
                    prefix += ' warning'
                if self.E == errlevel:
                    prefix += ' error'
                if self.F == errlevel:
                    prefix += ' fatal'

            prefix += ': '
            print(prefix + message)

        if self.F == errlevel:
            sys.exit(1)


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
    while('/' != localpath and None == name):
        if(os.path.isfile(localpath + '/' + confname)):
            name = localpath + '/' + confname

        localpath = os.path.dirname(localpath)

    return name


def main():
    lg = Logger(False)
    parser = argparse.ArgumentParser(description='Tree configuration tool')
    parser.add_argument('cmd', metavar='command', nargs=1, help='The command to execute. Type \'tconf help\' to get a list.')
    parser.add_argument('args', metavar='arguments', nargs='*', help='Command parameters. Type \'tconf help [cmd]\' to get some help.')
    parser.add_argument('-v', '--verbose', nargs='*', help='Display traces. Useful to understand what happens when it sucks.')
    cmdline_args = parser.parse_args()
    cmd = cmdline_args.cmd[0]
    args = cmdline_args.args
    print(cmd)
    if 'get' == cmd or 'g' == cmd:
        if 0 == len(args):
            lg.log('Hey', lg.I)
            lg.log('What u doin')
        #print(get(args[]))


main()
#config = ConfigFile('roger')


