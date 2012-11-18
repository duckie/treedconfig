#!/usr/bin/python2
# -*- Encoding:UTF-8 -*-
# Code for python 3.x will be provided later

import argparse
import ConfigParser
import os, sys, re

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

def printHelp(command = None):
    if(None == command):
        print("""
Tconf commands

help    : displays this help or a command's one
get     : reads a value
set     : sets a value
""")
    else:
        print('To do')


def getConfigFileName():
    name = '.tconf'
    if(os.environ.__contains__('TCONFFILE')):
        envname = os.environ['TCONFFILE']
        if (0 < len(envname)):
            name = envname

    return name


def getExecutionPath():
    return os.getcwd()


def findLocalConfigFile(path):
    confname = getConfigFileName()
    name = None
    localpath = path
    while('/' != localpath and None == name):
        if(os.path.isfile(localpath + '/' + confname)):
            name = localpath + '/' + confname

        localpath = os.path.dirname(localpath)

    return name

def resolveTconfFiles():
    files = []
    local = findLocalConfigFile(getExecutionPath())
    if None != local:
        current = local
        while None != current:
            if os.path.isdir(current):
                    current = current + '/' + getConfigFileName()
            if os.path.isfile(current):
                    files.append(current)

            cfg = ConfigParser.ConfigParser()
            cfg.readfp(open(current))
            if cfg.has_option('tconf','parent'):
                current = os.path.expanduser(cfg.get('tconf','parent'))
            else:
                current = findLocalConfigFile(os.path.dirname(os.path.dirname(current)))

    for current in [os.path.expanduser('~/.config/tconf.cfg'), '/etc/tconf.cfg']:
        if os.path.isfile(current):
            files.append(current)

    return files


def main():
    parser = argparse.ArgumentParser(description='Tree configuration tool')
    parser.add_argument('cmd', metavar='command', nargs=1, help='The command to execute. Type \'tconf help\' to get a list.')
    parser.add_argument('args', metavar='arguments', nargs='*', help='Command parameters. Type \'tconf help [cmd]\' to get some help.')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Display traces. Useful to understand what happens when it sucks.')
    cmdline_args = parser.parse_args()
    lg = Logger(cmdline_args.verbose)
    cmd = cmdline_args.cmd[0]
    args = cmdline_args.args
    if 'help' == cmd:
        printHelp()
        sys.exit(0)

    if 'get' == cmd or 'g' == cmd:
        if 0 == len(args):
            lg.log('\"get\" needs at least one argument, the name of the key to be read')

        category = ''
        key = ''
        if 1 == len(args):
            expr = re.compile(r'^([^\/\.]+)[\.|\/](.+)$')
            result = expr.match(args[0])
            if None == result:
                lg.log('the key \"' + args[0] + '\" is ill-formed.')

            category = result.group(1)
            key = result.group(2)

        else:
            category = args[0]
            key = args[1]


        print(resolveTconfFiles())        
        sys.exit(0)

    lg.log('\"' + cmd + '\" is unknown. Type tconf help to get a list.')

main()
#config = ConfigFile('roger')


